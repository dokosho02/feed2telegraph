from joe_feed.utils.core.terminal import TerminalColors
# from joe_feed.utils.core.html import retainText

import joe_feed.utils.core.sqliteBind as sqliteBind
# from joe_feed.utils.telegra.telegra import write2Telegraph
from joe_feed.setting.Languages import Languages as langue
import joe_feed.setting.config as cfg

# from joef2t.utils.kanaJPN import kanaConvert
# import asyncio
# import telegram_send as ts

# from pygtrans import Translate
# import html2text
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
        # self.resUrl    = ""

        print(f"item - conf - {self.conf}")

        print(f"""\t{self.chapterNo}\t{TerminalColors.OKCYAN}{self.title}{TerminalColors.ENDC}\n\t{self.link}\n\t{self.time}""")

        # ---------------
        try:
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


    # #  -------------------------------------
    # def translate(self):


    #     # convert
    #     h = html2text.HTML2Text()
    #     # Ignore converting links from HTML
    #     h.ignore_links = True
    #     plainText = retainText(self.contents).split("\n")

    #     self.converted = [self.title]
    #     for pt in plainText:
    #         self.converted.append( h.handle(pt) )
    #     print("--------")
    #     # translate
    #     client = Translate()
    #     texts = client.translate(self.converted)

    #     for t in texts:
    #         self.contents += f"""\n<p>{t.translatedText.replace("&gt;", ">")}</p>\n"""

# ---------------------
