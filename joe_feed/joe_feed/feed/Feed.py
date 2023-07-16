import feedparser
import os
from datetime import datetime
from tqdm import tqdm
from pprint import pprint

# import telegram_send as ts

from joe_feed.feed.Item import Item
from joe_feed.utils.core.file import createFile, readText
from joe_feed.utils.core.terminal import TerminalColors
from joe_feed.utils.core.html import removeAttrExceptHrefSrc, retainText
import joe_feed.utils.core.sqliteBind as sqliteBind

import joe_feed.setting.config as cfg
from joe_feed.setting.Languages import Languages as langue
from joe_feed.setting.Languages import Translated as tsl

# --------------------------
class Feed():
    def __init__(self, link, title, config, lang, translated):
        self.link  = link
        self.title = title
        self.confSimple = config
        self.conf  = cfg.getFilepath(config)
        self.lang  = lang
        self.translated = translated

        self.lastLinks1 = []
        self.lastLinks2 = []
        self.newItems  = []

        # folders
        self.lastFolder = "last"
        # self.jsonFolder = "json"
        
        print(f"feed - conf/n{self.conf}")
        print(f"database path - {cfg.database}")
        #
    # --------------------------
    def run(self):
        self.createFolders()
        self.getBackups()

        self.getEntries()
        self.removeOldItems()
        self.write2sql()

        self.processNewItems()


    # -------------------------------
    # preparation
    def createFolders(self):
        for fd in [
            self.lastFolder,
        ]:
            if (os.path.exists(fd) == False ):
                os.mkdir(fd)
    # -------------------------------
    def getBackups(self):
        self.titleProcessed = self.title.replace(".", "_")
        
        self.lastPath   = os.path.join(self.lastFolder, f"last_{self.titleProcessed}.md")
        self.backupPath = os.path.join(self.lastFolder, f"last_{self.titleProcessed}_bp.md")
    # -------------------------------
    # core
    def getEntries(self):
        self.feed = feedparser.parse(self.link)
        self.entries = self.feed["entries"]
        print( f"\t{TerminalColors.OKBLUE}{len(self.entries)}{TerminalColors.ENDC} - entries amount in current session" )
    # -------------------------------
    def removeOldItems(self):
        self.getLastLinks()
        now = datetime.now()
        self.getNewItems()

        updateNo = len(self.newItems)
        self.updateInfo = f"\t{TerminalColors.OKBLUE}{updateNo} - update(s){TerminalColors.ENDC} of {TerminalColors.OKBLUE}{len(self.entries)} ({self.title}){TerminalColors.ENDC}\n\t\tat {now}"
        self.updateLog = f"{updateNo}/{len(self.entries)} ({self.title})\nat {now}\nfrom Feed2Telegraph"

        print(self.updateInfo)
        # if updateNo > 0:
        #     ts.send(messages=[self.updateLog],conf=cfg.logChannel)
    # -------------------------------
    def getLastLinks(self):
        # self.lastPath
        try:
            g = readText(self.lastPath)
            self.lastLinks1 = g.split("\n")
        except Exception as e:
            print(f"{TerminalColors.FAIL}{self.lastPath}\n{e}{TerminalColors.ENDC}")
        # self.backupPath

        try:
            g = readText(self.backupPath)
            self.lastLinks2 = g.split("\n")
        except Exception as e:
            print(f"{TerminalColors.FAIL}{self.backupPath}\n{e}{TerminalColors.ENDC}")

        self.lastLinks = self.lastLinks1 + self.lastLinks2

        print(f"{len(self.lastLinks)} item(s) in last files.")

    # -------------------------------
    def getNewItems(self):
        if len(self.lastLinks) > 0:
            for et in self.entries:
                temp = et["link"]
                if temp not in self.lastLinks:
                    self.newItems.append(et)
        else:
            self.newItems = self.entries
    # ----------------------------------------------------------------------
    # sqlite
    def write2sql(self):
        # insert template
        feedElement = (self.title, self.link, self.lang, self.confSimple, self.translated)
        terminalWord = f"""\t{TerminalColors.OKCYAN}inserted - {feedElement}{TerminalColors.ENDC}"""
        # check if db exists
        if (os.path.isfile(cfg.database) == False ):
            self.createTables()

            conn = sqliteBind.create_connection(cfg.database)
            sqliteBind.insert_item(conn, cfg.feed_insert_sql, feedElement)

            print(terminalWord)
        else:
            # connect to db
            conn = sqliteBind.create_connection(cfg.database)
        # read old feeds, get feed url and compare
        # if not in then insert it
            if conn is not None:
                rows = sqliteBind.select_items(conn, cfg.feed_table_name)

                feeds = []
                if len(rows) > 0:
                    for ro in rows:
                        feeds.append(ro[2])

                if self.link not in feeds:
                    # insert new
                    sqliteBind.insert_item(conn, cfg.feed_insert_sql, feedElement)
                    print(terminalWord)
    # --------------------------
    def getLinksFromEntries(self):
        self.lastString = ""
        for et in self.entries:
            self.lastString += f"""{et["link"]}\n"""
    # --------------------------
    def write2LastFiles(self):
        self.getLinksFromEntries()

        # create file
        createFile(self.lastPath, self.lastString)
        print(f"last file has been written to {self.lastPath}")

        # create backup file
        self.backupString = ""
        try:
            for lk in self.lastLinks1:
                self.backupString += f"{lk}\n"
            createFile(self.backupPath, self.backupString)
            print(f"last backup file has been written to {self.backupPath}")
        except Exception as e:
            print(f"{TerminalColors.FAIL}no last backup file - {e}{TerminalColors.ENDC}")
    # -------------------------------
    def processSingleItem(self, i):
        # contents string
        entry = self.newItems[i]
        entryTitle, entryContent, entryLink, entryAuthors, entryTags = self.getItemContents(entry)

        # time
        dt = ""
        try:
            dt = entry["published"]
        except Exception as e:
            print(f"{e}\nNo time label")
        
        entryContent = removeAttrExceptHrefSrc(entryContent)
        entryContent = self.refineContents(entryContent)

        return (entryTitle, entryContent, entryLink, entryAuthors, entryTags, dt)
    # -------------------------------
    def processNewItems(self):
        if (len(self.newItems) > 0):
            self.newItems.reverse()

            for i in tqdm( range(len(self.newItems))):
                entryTitle, entryContent, entryLink, entryAuthors, entryTags, dt = self.processSingleItem(i)
                
                print(f"before item - {self.conf}")

                item = Item(
                title     = entryTitle,
                chapterNo = str(i+1),
                time      = dt, # time,
                contents  = entryContent,
                link      = entryLink,
                authors   = entryAuthors,
                keyWords  = entryTags,
                feedName  = self.title,
                feedLink  = self.link,
                lang      = self.lang,
                translated= self.translated,
                conf      = self.conf,
                )
            self.write2LastFiles()
            print(f"complete - {self.updateInfo}")
    # -------------------------------
    def getItemContents(self, entry):
        entryTitle = entry["title"]
        entryLink  = entry["link"]
        
        entryAuthors = []
        entryTags    = []

        try:
            entryTags     = [tag.term for tag in entry.tags]
        except:
            pass
        try:
            entryAuthors  = [author.name for author in entry.authors]
        except:
            pass

        # contents string
        entryContent = entry["summary"]
        for k in entry.keys():
            if k != "content":
                continue
            if (len(str(entry["summary"])) < len(str(entry["content"][0]["value"])) ):
                entryContent = entry["content"][0]["value"]
                print(f"""\t{TerminalColors.OKCYAN}content -> 0 -> value{TerminalColors.ENDC}""") 
            else:
                print(f"""\t{TerminalColors.OKCYAN}summary{TerminalColors.ENDC}""")
        
        return (entryTitle, entryContent, entryLink, entryAuthors, entryTags)

    # -------------------------------
    def refineContents(self, cont):    # for basics
        # if (self.link == "https://rss.huxiu.com/"):
        cont = cont.replace("""&nbsp;""", "").replace("<p><br/></p>", "").replace("<p></p>", "")
        if ( (self.link == "https://chinadigitaltimes.net/chinese/feed/") or (self.link == "https://chinadigitaltimes.net/feed/") ):
            cont = cont.replace("<blockquote>", "").replace("</blockquote>", "")

        return cont

# --------------------------------------------------------------------
    def createTables(self):
            # create a database connection
        conn = sqliteBind.create_connection(cfg.database)
            # create tables
        if conn is not None:
            # create projects table
            sqliteBind.create_table(conn, cfg.sql_create_feeds_table)

            # create tasks table
            sqliteBind.create_table(conn, cfg.sql_create_articles_table)
        else:
            print("Error! cannot create the database connection.")

# --------------------------
def main():
    Feed(
        link       = "https://rsshub.app/geekpark/breakingnews",
        title      = "geekpark",
        config     = cfg.daily,
        lang       = langue.zhs,
        translated = tsl.n,
    ).run()
# --------------------------

if __name__ == '__main__':
    main()
