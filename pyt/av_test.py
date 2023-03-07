# from joef2t.feed.scrape.av.AVFeed import AVFeed
# from joef2t.setttings import config as cfg
# from joef2t.setttings.Languages import Languages as lang

# import telegram_send as ts


# url = "https://s1s1s1.com/"
# AVFeed(url,"S1", cfg.avf, lang.jpn).run()

# word = f"""
# #Good
# https://telegra.ph/许家印都把车造出来了贾跃亭的FF91还在冲刺量产---huxiu-12-03
# [Web](https://www.huxiu.com/article/731323.html?f=rss)
# """
# ts.send(messages=[word], parse_mode="markdown", conf=cfg.conf)

from joef2t.utils.html import removeAttrExceptHrefSrc
from joef2t.utils.file import createFile

from joef2t.utils.web import webCode
from bs4 import BeautifulSoup
from pprint import pprint


import feedparser


def main():
    feed  = feedparser.parse("https://www.billboard-japan.com/d_news/doc.xml")

    entries = feed["entries"]
    print( len(entries) )

    for entry in entries:
        entryTitle  = entry["title"]
        entryLink   = entry["link"]
        
        print(entryTitle)

        articleBody = ""
        # full page
        code = webCode(f"{entryLink}/2")
        soup = BeautifulSoup(code, "html.parser")
    
        contentResult = soup.select("div[class=newsArticle]")
        print( len(contentResult) )
        if (len(contentResult) > 0):
            articleBody = removeAttrExceptHrefSrc( str(contentResult[0]) )#.replace("data-src", "src")

            pprint(articleBody)
        # createFile("test.html", articleBody)
# --------------------------

if __name__ == '__main__':
    main()