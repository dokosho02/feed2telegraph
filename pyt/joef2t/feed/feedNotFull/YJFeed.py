# from joef2t.feed.Feed import Feed
from joef2t.feed.feedNotFull.NotFullFeed import NotFullFeed

from joef2t.setttings import config as cfg
from joef2t.setttings.Languages import Translated as tsl
from joef2t.setttings.Languages import Languages as lang

from joef2t.utils.web import webCode
from joef2t.utils.html import removeAttrExceptHrefSrc

from bs4 import BeautifulSoup

class YJFeed(NotFullFeed):
    def __init__(self,link, title, config, lang, translated ):
        super().__init__(link, title, config, lang, translated)
    # -------------------------------
    def getItemContents(self, entry):
        # title
        entryTitle  = entry["title"]
        entryLink   = self.getItemLink(entry) if "topics" in self.link else entry["link"].replace("?source=rss", "")    # remove `?source=rss` for multi-page
        entryContent, entryAuthors, entryTags = self.getItemFull(entryLink)

        return (entryTitle, entryContent, entryLink, entryAuthors, entryTags)
    # -------------------------------
    def getItemLink(self, entry):
        # link
        entryLink = ""
        middleLink = entry["link"]
        code = webCode(middleLink)
        soup = BeautifulSoup(code, "html.parser")
        links = soup.select("a")
        for lk in links:
            if lk.text.strip() == "記事全文を読む":
                entryLink = lk.get("href")
        
        return entryLink
    # -------------------------------
    def getItemFull(self, entryLink):
        # full page
        code = webCode(entryLink)
        soup = BeautifulSoup(code, "html.parser")

        # h1 title
        title = ""
        h1s = soup.select("h1")
        for h in h1s:
            if h.text.strip() != "Yahoo!ニュース":
                title = f"<h1>{h.text}</h1>"
        print(title)
        
        # author
        authors = []
        footers = soup.select("footer")
        for ft in footers:
            if "最終更新" in ft.text.strip():
                author = removeAttrExceptHrefSrc(str(ft)).replace("<footer>", "").replace("</footer>", "").replace("<!-- --> <!-- -->", " ")
                authors.append(author)
                print(author)


        # multi-page
        pages = 1
        try:
            pn = soup.select("span.pagination_number_text")[0].text.replace("ページ" , "")
            pages = int(pn)
        except:
            pass
        print(pages)
        
        selectKeyworld = ""
        if "articles" in entryLink:
            selectKeyworld = "div[class*=article_body]"
        if "byline" in entryLink:
            selectKeyworld = "section[class=articleBody]"
        
        # first page
        articleBody = ""
        artbody = soup.select(selectKeyworld)[0]
        articleBody += removeAttrExceptHrefSrc(str(artbody))

        # other pages
        # https://news.yahoo.co.jp/articles/b17ec8c63100e0cebd662deebbbd4ea632b4ef87?page=2
        if pages > 1:
            for i in range(1, pages):
                moreCode = webCode(f"{entryLink}?page={i+1}")
                moreSoup = BeautifulSoup(moreCode, "html.parser")
                artbody = moreSoup.select(selectKeyworld)[0]
                articleBody += removeAttrExceptHrefSrc(str(artbody))
        
        # print(articleBody)
        # articleBody = articleBody.replace("<a>","\n<a>").replace("</a>","</a>\n")
        return (f"{title}\n{articleBody}", authors, [])
# --------------------------

# --------------------------
def main():
    # YJFeed("https://news.yahoo.co.jp/rss/categories/domestic.xml", "yj_domestic", cfg.yjn)
    YJFeed("https://news.yahoo.co.jp/rss/categories/local.xml","yj_local", cfg.yjnl, lang.jpn, tsl.n).run()

# --------------------------

if __name__ == '__main__':
    main()