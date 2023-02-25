# from config import huxiu_channel_conf
# import telegram_send as ts

# ts.send(messages=["test"],conf=huxiu_channel_conf)


from bs4 import BeautifulSoup

from joef2t.utils.web import webCode
from joef2t.utils.html import removeAttrExceptHrefSrc

def main():

    # link
    code = webCode("https://news.yahoo.co.jp/pickup/6441951?source=rss")
    soup = BeautifulSoup(code, "html.parser")
    links = soup.select("a")
    entryLink = ""

    for lk in links:
        if lk.text.strip() == "記事全文を読む":
            entryLink = lk.get("href")

    print(entryLink)

    # full page
    fullCode = webCode("https://news.yahoo.co.jp/articles/47a0b3713fd0dc1c6109b7f9427a54b73a3cb0cd?source=rss")
    fullSoup = BeautifulSoup(fullCode, "html.parser")

    # title
    title = ""
    h1s = fullSoup.select("h1")

    for h in h1s:
        if h.text.strip() != "Yahoo!ニュース":
            title = f"<h1>{h.text}</h1>"

    print(title)

    # author
    author = ""
    footers = fullSoup.select("footer")
    for ft in footers:
        if "最終更新" in ft.text.strip():
            author = removeAttrExceptHrefSrc(str(ft)).replace("<footer>", "").replace("</footer>", "").replace("<!-- --> <!-- -->", " ")
    print(author)

    # multi-page
    pages = 1
    try:
        pn = fullSoup.select("span.pagination_number_text")[0].text.replace("ページ" , "")
        # print(pn)
        pages = int(pn)
    except:
        pass
    print(pages)

    # first page
    articleBody = ""
    artbody = fullSoup.select("div[class*=article_body]")[0]
    articleBody += removeAttrExceptHrefSrc(str(artbody))

    # other pages
    # https://news.yahoo.co.jp/articles/b17ec8c63100e0cebd662deebbbd4ea632b4ef87?page=2
    if pages > 1:
        for i in range(1, pages):
            moreCode = webCode(f"{entryLink}?page={i+1}")
            moreSoup = BeautifulSoup(moreCode, "html.parser")
            artbody = moreSoup.select("div[class*=article_body]")[0]
            articleBody += removeAttrExceptHrefSrc(str(artbody))
    
    print(articleBody)

# --------------------------

if __name__ == '__main__':
    main()