from joe_feed.setting import config as cfg
from joe_feed.setting.Languages import Languages as lang
from joe_feed.setting.Languages import Translated as tsl

head = "https://rsshub.app/wechat/ershicimi/"

# link, name, channel, language, translation
selected_sim = [
    ["N3WgvL3M",       "thatNG"],
    # ["rQA9kZQZ", "FengXueRong",  cfg.wxsl, lang.zhs, tsl.n],    # remove ad
    ["XQJ4VnOb", "brief_history"],
    ["dOVgBkje", "polar_day_stu"],  
    ["wDOqGBQ4", "old_driver_business"], 
    ["EOd8GKO4", "mylifeano"],
    ["LRjlqAQD", "earth_knowledge"],
    ["mQ4RDeO4", "guokr42"],
    ["vKQ1PKjJ", "wallstreet_cn"],
    ["AQbqbajD", "principle"],
    ["nXQJRNQb", "renwumag1980"],

]
# ------------------------------------------------
daily_sim = [
    ["2jr1rwOY",        "appso" ],
    # ["13oVxvQl",        "szdays"],
    ["Rjl0r2jD",        "douban"],

]


code_garden_sim = [
    ["NjpEdVQB",      "osc_ops" ],
    ["dOVD2m7Q",      "coder_lib"],
    ["nqQBbQz0", "pyt_community"],
    ["vdOVar3e",      "coderHui"],
    ["RjlPAljD", "Coder_alliance"],
]

university_sim = [
    ["dOVlr5Qe",        "whu", cfg.univ, lang.zhs, tsl.n],
    ["23nX61yj",       "hust", cfg.univ, lang.zhs, tsl.n],
    ["NjYk0Rb3",      "hkust", cfg.univ, lang.zhs, tsl.n],
    ["bO9lBdp3",       "xjtu", cfg.univ, lang.zhs, tsl.n],
]

HIMMR_sim = [
    ["4QkVznja",       "HowImetMrRight"],
    ["M3eZ4LlO",        "HIMMRshanghai"],
    ["x30PngL3",          "HIMMRpeking"],
    ["838JB2Mj",        "HIMMRhangchow"],
    ["dOVoKa8j",          "HIMMRcanton"],
    ["N3N7KWvO",         "HIMMRnanking"],
]

selected   = list( map(lambda i: [f"{head}{i[0]}", i[1], cfg.wxsl, lang.zhs, tsl.n], selected_sim) )
cgd        = list( map(lambda i: [f"{head}{i[0]}", i[1],  cfg.cgd, lang.zhs, tsl.n], code_garden_sim) )
daily      = list( map(lambda i: [f"{head}{i[0]}", i[1], cfg.daily,lang.zhs, tsl.n], daily_sim) )
university = list( map(lambda i: [f"{head}{i[0]}", i[1], cfg.univ, lang.zhs, tsl.n], university_sim) )
HIMMR      = list( map(lambda i: [f"{head}{i[0]}", i[1], cfg.HIMMR,lang.zhs, tsl.n], HIMMR_sim) )

# ------------------------------------------------
ershicimiRSS = selected + daily    + cgd + university
# ------------------------------------------------
def main():
    [print(rl) for rl in ershicimiRSS]

# ------------------------------------------------

if __name__ == '__main__':
    main()
