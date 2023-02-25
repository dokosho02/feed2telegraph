from joef2t.utils.terminal import TerminalColors
from joef2t.utils.html import retainText
from joef2t.utils.telegra import write2Telegraph
from joef2t.setttings.Languages import Languages as langue

from joef2t.utils.kanaJPN import kanaConvert
import asyncio

import telegram_send as ts

from pygtrans import Translate
import html2text

import joef2t.setttings.config as cfg
import joef2t.utils.sqliteBind as sqliteBind


# ---------------------------------------------
class Item():
    def __init__(self,
        title,
        chapterNo,
        time,
        contents,
        link,
        authors,
        keyWords,
        feedName,
        feedLink,
        lang,
        translated,
        conf
        ):
        self.title     = title
        self.chapterNo = chapterNo
        self.time      = time
        self.contents  = contents#.replace("<article>", "").replace("</article>", "").strip()
        self.link      = link
        self.authors   = authors
        self.keyWords  = keyWords
        self.feedName  = feedName
        self.feedLink  = feedLink
        self.lang      = lang
        self.translated= translated
        self.conf      = conf

        self.au = ""
        self.kw = ""
        self.resUrl    = ""

        print(f"item - conf - {self.conf}")

        print(f"""\t{self.chapterNo}\t{TerminalColors.OKCYAN}{self.title}{TerminalColors.ENDC}\n\t{self.link}\n\t{self.time}""")

        # ---------------
        self.html4Telegraph = f"""
        <p><a href="{self.link}">Web</a></p>\n
        <h1>{self.title}</h1>\n
        <p><br/></p>\n
        <p>{self.time}</p>\n
        """

        if len(self.authors) >0:
            self.au = ", ".join(self.authors)
            self.html4Telegraph += f"""<p>{self.au}</p>\n"""

        if len(self.keyWords) >0:
            self.kw = ", ".join(self.keyWords)
            self.html4Telegraph += f"""<p>tag(s): {self.kw}</p>\n"""
        
        # translation
        if self.translated!=0:
            print(f"translate?: {self.translated}")
            try:
                self.translate()
                print(self.contents)
            except Exception as e:
                print(f"problem in translation\n{e}")

        # japanese
        if (self.lang == langue.jpn):
            self.contents += f"""<p>{kanaConvert(retainText(self.contents))}</p>\n"""

        self.html4Telegraph += f"""{self.contents}\n"""

        # ---------------
        try:
            self.resUrl = asyncio.run(
                write2Telegraph(
                    title=f"{self.title} - {self.feedName}",
                    content = self.html4Telegraph,
                    author = self.au,
                )
            )
            sendWord = ""
            if (len(self.keyWords)>0):
                for k in self.keyWords:
                    sendWord +=f"#{k} "
                sendWord += "\n"
            sendWord += f"{self.resUrl}\n[Web]({self.link})"
            ts.send(
                messages=[sendWord],
                parse_mode="markdown",
                conf=self.conf
            )

            self.write2sql()
        except Exception as e:
            print(f"{self.link}\n{e}")

    # ----------------------
    def write2sql(self):
        conn = sqliteBind.create_connection(cfg.database)
        if conn is not None:
            articles = []
            try:
                rows = sqliteBind.select_items_by_property(conn, cfg.article_table_name, p="feed_link",v=self.feedLink)
                if len(rows) > 0:
                    for ro in rows:
                        articles.append(ro[2])
            except:
                print(f"\tno feed_name - {self.feedLink} in articles")

            if self.link not in articles:
                feed_id = 0
                try:
                    rows = sqliteBind.select_items_by_property(conn, cfg.feed_table_name, p="link",v=self.feedLink)
                    for ro in rows:
                        feed_id = ro[0]
                except:
                    print(f"no title in feeds - {self.feedName}")
                    
                print(feed_id)

                articleElement = (
                    self.title,
                    self.link,
                    "",    # date, later to modify
                    self.contents,
                    self.au,
                    self.lang,
                    self.kw,
                    "",
                    0,
                    0,
                    "",
                    "",
                    self.feedName,
                    self.feedLink,
                    feed_id
                )

                terminalWord = f"""\t{TerminalColors.OKCYAN}article inserted - {self.title}{TerminalColors.ENDC}"""
                sqliteBind.insert_item(conn, cfg.article_insert_sql, articleElement)
                print(terminalWord)


    #  -------------------------------------
    def translate(self):


        # convert
        h = html2text.HTML2Text()
        # Ignore converting links from HTML
        h.ignore_links = True
        plainText = retainText(self.contents).split("\n")

        self.converted = [self.title]
        for pt in plainText:
            self.converted.append( h.handle(pt) )
        print("--------")
        # translate
        client = Translate()
        texts = client.translate(self.converted)

        for t in texts:
            self.contents += f"""\n<p>{t.translatedText.replace("&gt;", ">")}</p>\n"""

# ---------------------
