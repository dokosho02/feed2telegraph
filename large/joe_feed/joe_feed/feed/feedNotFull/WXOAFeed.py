from joef2t.feed.feedNotFull.NotFullFeed import NotFullFeed
from joef2t.utils.terminal import TerminalColors

from joef2t.setttings import config as cfg
from joef2t.setttings.Languages import Translated as tsl
from joef2t.setttings.Languages import Languages as lang

from joef2t.utils.web import webCode
from joef2t.utils.html import removeAttrExceptHrefSrc

from bs4 import BeautifulSoup
from pprint import pprint

class WXOAFeed(NotFullFeed):
    def __init__(self,link, title, config, lang, translated ):
        super().__init__(link, title, config, lang, translated)
    # -------------------------------
    #  override
    def getItemFull(self, entryLink):
        articleBody = ""
        # full page
        code = webCode(entryLink)
        soup = BeautifulSoup(code, "html.parser")
        
        contentResult = soup.select("div#js_content")
        print( len(contentResult) )
        if (len(contentResult) > 0):
            articleBody = removeAttrExceptHrefSrc( str(contentResult[0]) ).replace("data-src", "src")

            pprint(articleBody)

        return (articleBody, [], [])
# --------------------------
def main():
    WXOAFeed("https://api.feeddd.org/feeds/61f3d472dca58a380c4fc131","old_driver_business", cfg.wxoa, lang.zhs, tsl.n).run()

# --------------------------

# if __name__ == '__main__':
#     main()