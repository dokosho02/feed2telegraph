from joe_feed.source.basic import basics
from joe_feed.feed.Feed import Feed

from joe_feed.source.yj_news import yj_news


def hourly():
    for rss in basics:
        try:
            Feed(
                link  =rss[0],
                title =rss[1],
                config=rss[2],
                lang  =rss[3],
                translated =rss[4],
            ).run()
        except Exception as e:
            print(f"{rss[0]}\n{rss[1]}\n{e}")

def min15():
    yj_news()

if __name__ == '__main__':
    # hourly()
    min15()


