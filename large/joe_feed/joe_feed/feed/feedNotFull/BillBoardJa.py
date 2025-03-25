from joef2t.feed.feedNotFull.NotFullFeed import NotFullFeed
from joef2t.utils.terminal import TerminalColors

from joef2t.setttings import config as cfg
from joef2t.setttings.Languages import Translated as tsl
from joef2t.setttings.Languages import Languages as lang

from joef2t.utils.web import webCode
from joef2t.utils.html import removeAttrExceptHrefSrc

from bs4 import BeautifulSoup
from pprint import pprint

class BillBoardJa(NotFullFeed):
    def __init__(self,link, title, config, lang, translated ):
        super().__init__(link, title, config, lang, translated)
    # -------------------------------
    #  override
    def getItemFull(self, entryLink):
        articleBody = ""
        # full page
        code = webCode(f"{entryLink}/2")
        soup = BeautifulSoup(code, "html.parser")
        
        contentResult = soup.select("div[class=newsArticle]")
        print( len(contentResult) )
        if (len(contentResult) > 0):
            articleBody = removeAttrExceptHrefSrc( str(contentResult[0]) )

            pprint(articleBody)

        return (articleBody, [], [])

# --------------------------
def main():
    BillBoardJa("https://www.billboard-japan.com/d_news/doc.xml","billboard_ja", cfg.bbj, lang.jpn, tsl.n).run()
