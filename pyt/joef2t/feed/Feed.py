import feedparser
import os
from datetime import datetime
from tqdm import tqdm
from pprint import pprint

from joef2t.feed.Item import Item
from joef2t.utils.file import createFile, readText
from joef2t.utils.terminal import TerminalColors
from joef2t.utils.html import removeAttrExceptHrefSrc, retainText
import joef2t.utils.sqliteBind as sqliteBind

import joef2t.setttings.config as cfg
from joef2t.dictionary.Lookup import Lookup
from joef2t.setttings.Languages import Languages as langue
from joef2t.setttings.Languages import Translated as tsl

import telegram_send as ts
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
        
        print(f"feed - conf - {self.conf}")
        # 
    # --------------------------
    def run(self):
        self.createFolders()
        self.getBackups()

        self.getEntries()
        self.removeOldItems()
        
        self.write2sql()
        self.processNewItems()


    # --------------------------
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
    def getEntries(self):
        self.feed = feedparser.parse(self.link)
        # print(self.link)
        # pprint(self.feed)
        self.entries = self.feed["entries"]
        # print( f"\t{TerminalColors.OKBLUE}{len(self.entries)}{TerminalColors.ENDC} - entries amount in current session" )
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
        print(f"\tlast file --> {self.lastPath}")

        # create backup file
        self.backupString = ""
        try:
            for lk in self.lastLinks1:
                self.backupString += f"{lk}\n"
            createFile(self.backupPath, self.backupString)
            print(f"\tlast backup file --> {self.backupPath}")
        except Exception as e:
            print(f"{TerminalColors.FAIL}no last backup file - {e}{TerminalColors.ENDC}")

    # -------------------------------
    def getNewItems(self):
        if len(self.lastLinks) > 0:
            for et in self.entries:
                temp = et["link"]
                if temp not in self.lastLinks:
                    self.newItems.append(et)
        else:
            self.newItems = self.entries
    # -------------------------------
    def removeOldItems(self):
        self.getLastLinks()
        now = datetime.now()
        self.getNewItems()

        updateNo = len(self.newItems)
        self.updateInfo = f"\t{TerminalColors.OKCYAN}{updateNo}{TerminalColors.ENDC}/{TerminalColors.OKBLUE}{len(self.entries)}{TerminalColors.ENDC} - {TerminalColors.HEADER}{self.title}{TerminalColors.ENDC}\n\tat {now}"
        self.updateLog = f"{updateNo}/{len(self.entries)} ({self.title})\nat {now}\nfrom Feed2Telegraph"

        print(self.updateInfo)
        if updateNo > 0:
            ts.send(messages=[self.updateLog],conf=cfg.logChannel)
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
                #time = datetime.strptime(dt, "%a, %d %b %Y %H:%M:%S %z")
                # print(dt.strftime("%z"))
                # 	Tue, 20 Sep 2022 07:49:57 +0000

        entryContent = removeAttrExceptHrefSrc(entryContent)
        entryContent = self.refineContents(entryContent)

                # if (self.lang == langue.eng):
                #     lookup = Lookup(cfg.glossaryEng, self.lang, retainText(entryContent) )
                #     entryContent += lookup.results
                
                # pass value

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
    def refineContents(self, cont):
        # if (self.link == "https://rss.huxiu.com/"):
        cont = cont.replace("""&nbsp;""", "").replace("<p><br/></p>", "").replace("<p></p>", "")
        if ( (self.link == "https://chinadigitaltimes.net/chinese/feed/") or (self.link == "https://chinadigitaltimes.net/feed/") ):
            cont = cont.replace("<blockquote>", "").replace("</blockquote>", "")

        return cont
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
    # Feed("https://rsshub.app/dapenti/tugua")
    Feed("https://rss.huxiu.com/", "huxiu", cfg.huxiu, langue.zhs, tsl.n).run()
    #Feed("https://biz.trans-suite.jp/feed")
# --------------------------

if __name__ == '__main__':
    main()
