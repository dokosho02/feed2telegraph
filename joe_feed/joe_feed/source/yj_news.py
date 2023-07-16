import joe_feed.setting.channel as ch
from joe_feed.setting.Languages import Languages as lang
from joe_feed.setting.Languages import Translated as tsl

from joe_feed.feed.feedNotFull.YJFeed import YJFeed


"""
- [AERA dot.](https://news.yahoo.co.jp/rss/media/sasahi/all.xml)
- [AERA STYLE MAGAZINE](https://news.yahoo.co.jp/rss/media/asmasahi/all.xml)
- [ALBA TV](https://news.yahoo.co.jp/rss/media/golfnettv/all.xml)
- [All About](https://news.yahoo.co.jp/rss/media/nallabout/all.xml)
- [ALL REVIEWS](https://news.yahoo.co.jp/rss/media/allreview/all.xml)
- [AMP［アンプ］](https://news.yahoo.co.jp/rss/media/ampreview/all.xml)
- [ananweb](https://news.yahoo.co.jp/rss/media/ananweb/all.xml)
- [AP通信](https://news.yahoo.co.jp/rss/media/aptsushinv/all.xml)
- [ＡＴＶ青森テレビ](https://news.yahoo.co.jp/rss/media/atv/all.xml)
- [AUTO BILD JAPAN Web](https://news.yahoo.co.jp/rss/media/autobild/all.xml)
- [AUTOCAR JAPAN](https://news.yahoo.co.jp/rss/media/autocar/all.xml)
- [Auto Messe Web](https://news.yahoo.co.jp/rss/media/amweb/all.xml)
- [Aviation Wire](https://news.yahoo.co.jp/rss/media/awire/all.xml)
- [BARKS](https://news.yahoo.co.jp/rss/media/bark/all.xml)
- [Baseball Geeks](https://news.yahoo.co.jp/rss/media/geeksv/all.xml)
- [BASKET COUNT](https://news.yahoo.co.jp/rss/media/basket/all.xml)
- [BBC News](https://news.yahoo.co.jp/rss/media/bbc/all.xml)
- [BBCびわ湖放送](https://news.yahoo.co.jp/rss/media/bbcbiwakov/all.xml)
- [BBM Sports](https://news.yahoo.co.jp/rss/media/bbmv/all.xml)
- [BCN](https://news.yahoo.co.jp/rss/media/bcn/all.xml)
- [Bezzy](https://news.yahoo.co.jp/rss/media/bezzy/all.xml)
"""


head = "https://news.yahoo.co.jp/rss/media/"
tail = "/all.xml"

follow_sim = [
    ["sasahi", "AERA"], # AERA dot.
]

bbc_sim = [
    ["bbc", "BBC_News"],    # BBC_News
]

# 
bbc   = list( map(lambda i: [f"{head}{i[0]}{tail}", f"yj_{i[1]}", ch.bbc, lang.jpn, tsl.n], bbc_sim) )


# ------------------------------------------------
yj_rss = bbc # + 
# ------------------------------------------------
def main():
    [print(rl) for rl in yjRSS]

def yj_news():
    for rss in yj_rss:
        try:
            YJFeed(
                link  =rss[0],
                title =rss[1],
                config=rss[2],
                lang  =rss[3],
                translated =rss[4],
            ).run()
        except Exception as e:
            print(f"{rss[0]}\n{rss[1]}\n{e}")
# ------------------------------------------------

if __name__ == '__main__':
    main()
