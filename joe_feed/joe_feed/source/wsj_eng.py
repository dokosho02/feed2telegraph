from joe_feed.setting import config as cfg
from joe_feed.setting.Languages import Languages as lang
from joe_feed.setting.Languages import Translated as tsl

head = "https://rsshub.app/wsj/en-us/"

wsj_sim = [
    ["opinion",     "wsj-opinion"],
    ["world_news",  "wsj-world"  ],       #  WSJ world
    ["technology",  "wsj-tech"   ],    # WSJ tech
    ["lifestyle",   "wsj-lifestyle"],#      // WSJ lifestyle
    ["market_news", "wsj-market"], #        // WSJ market
    ["us_bussiness","wsj-bussiness"], #       // WSJ bussiness us
]

wsj = list( map(lambda i: [f"{head}{i[0]}", i[1], cfg.wsj, lang.eng, tsl.y], wsj_sim) )

# ------------------------------------------------
def main():
    [print(rl) for rl in wsj]
# ------------------------------------------------

if __name__ == '__main__':
    main()
