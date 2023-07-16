from joe_feed.utils.core.terminal import TerminalColors
# from joe_feed.utils.core.html import retainText

import joe_feed.utils.core.sqliteBind as sqliteBind
# from joe_feed.utils.telegra.telegra import write2Telegraph
from joe_feed.setting.Languages import Languages as langue
import joe_feed.setting.config as cfg

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
        feed_id,
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
        self.feed_id   = feed_id
        self.au = ""
        self.kw = ""
        # self.resUrl    = ""

        print(f"item - conf - {self.conf}")

        print(f"""\t{self.chapterNo}\t{TerminalColors.OKCYAN}{self.title}{TerminalColors.ENDC}\n\t{self.link}\n\t{self.time}""")

        if len(self.authors) >0:
            self.au = ", ".join(self.authors)

        if len(self.keyWords) >0:
            self.kw = ", ".join(self.keyWords)
        # ---------------
        try:
            self.write2sql()
        except Exception as e:
            print(f"{self.link}\n{e}")
    # ----------------------
    def write2sql(self):
        conn = sqliteBind.create_connection(cfg.database)
        if conn is not None:
            articleElement = (
                self.title,  # title
                self.link,   # link
                self.time,    # date, later to modify
                self.contents, # contents
                self.au,      # authors
                self.lang,    # lang
                self.kw,      # tags
                "",           # type
                "",           # iv link
                0,            # read
                0,            # starred
                self.feed_id
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
