from joe_feed.setting import config as cfg
from joe_feed.setting.Languages import Languages as lang
from joe_feed.setting.Languages import Translated as tsl

head = "https://rsshub.app/economist/"

economist_sim = [
    ["the-world-this-week",   "economist_world",                 ],
    ["letters",               "economist_letters",               ],
    ["leaders",               "economist_leaders",               ],
    ["briefing",              "economist_briefing",              ],
    ["special-report",        "economist_special-report",        ],
    ["britain",               "economist_britain",               ],
    ["europe",                "economist_europe",                ],
    ["united-states",         "economist_united-states",         ],
    ["the-americas",          "economist_the-americas",          ],
    ["middle-east-and-africa","economist_middle-east-and-africa",],
    ["asia",                  "economist_asia",                  ],
    ["china",                 "economist_china",                 ],
    ["international",         "economist_international",         ],
    ["business",              "economist_business",              ],
    ["science-and-technology","economist_science-and-technology",],
    ["books-and-arts",        "economist_books-and-arts",        ],
    ["obituary",              "economist_obituary",              ],
    ["graphic-detail",        "economist_graphic-detail",        ],
    ["economic-and-financial-indicators", "economist_indicators",],
]

fe = [
    [f"{head}finance-and-economics", "economist_finance-and-economics", cfg.ecnfe, lang.eng, tsl.y],
]

basics = list( map(lambda i: [f"{head}{i[0]}", i[1], cfg.ecn, lang.eng, tsl.y], economist_sim) )
economist = fe + basics
# ------------------------------------------------
def main():
    [print(rl) for rl in economist]
# ------------------------------------------------

if __name__ == '__main__':
    main()
