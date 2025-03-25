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

        print(f"""  {self.chapterNo}  {TerminalColors.OKCYAN}{self.title}{TerminalColors.ENDC}\n\t{self.link}\n\t{self.time}""")

        # ---------------
        self.html4Telegraph = f"""
        <p><a href="{self.link}">Web</a></p>\n
        <h1>{self.title}</h1>\n
        <p><br/></p>\n
        <p>time: {self.time}</p>\n
        """

        if len(self.authors) >0:
            self.au = ", ".join(self.authors)
            self.html4Telegraph += f"""<p>{self.au}</p>\n"""

        if len(self.keyWords) >0:
            self.kw = ", ".join(self.keyWords)
            self.html4Telegraph += f"""<p>tag(s): {self.kw}</p>\n"""
        
        # japanese
        self.kana_converted = ""
        if (self.lang == langue.jpn):
            self.kana_converted += f"""<p>{kanaConvert(retainText(self.contents))}</p>\n"""
            print("japanese - kanaConvert-ed")

        # translation
        if self.translated!=0:
            # print(f"translate?: {self.translated}")
            try:
                self.translate()
                # print(self.contents)
                print("translated")
            except Exception as e:
                print(f"problem in translation\n{e}")

    
        # final
        try:
            if len(self.kana_converted) > 0:
                self.contents +=  f"""\n<hr>\n{self.kana_converted}\n"""
        except:
            pass
        try:
            if len(self.translated_text) > 0:
                self.contents +=  f"""\n<hr>\n{self.translated_text}\n"""
        except:
            pass                

        self.html4Telegraph += f"""{self.contents}\n"""

        # ---------------
        try:
            # self.write2sql()
            # self.resUrl = asyncio.run(
            self.resUrl = write2Telegraph(
                    title=f"{self.title} - {self.feedName}",
                    content = self.html4Telegraph,
                    author = self.au,
                )
            # )
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
        
        self.translated_text = ""
        for t in texts:
            self.translated_text += f"""\n<p>{t.translatedText.replace("&gt;", ">")}</p>\n"""


# ---------------------
