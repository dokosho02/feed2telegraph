from joe_feed.setting import config as cfg
from joe_feed.setting.Languages import Languages as lang
from joe_feed.setting.Languages import Translated as tsl

head = "https://rsshub.app/yomiuri/"

yomiuri = [
    ["f{head}national","yomiuri_national", cfg.yomi_n, lang.jpn, tsl.n ],
    ["f{head}world",   "yomiuri_world",    cfg.yomi_w, lang.jpn, tsl.n ],
    ["f{head}local",   "yomiuri_local",    cfg.yomi_l, lang.jpn, tsl.n ],
    ["f{head}economy", "yomiuri_economy",  cfg.yomi_e, lang.jpn, tsl.n ],
]

# wsj = list( map(lambda i: [f"{head}{i[0]}", i[1], cfg.wsj, lang.eng, tsl.y], wsj_sim) )

# ------------------------------------------------
def main():
    [print(rl) for rl in yomiuri]
# ------------------------------------------------

if __name__ == '__main__':
    main()
