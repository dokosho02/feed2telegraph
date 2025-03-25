from joe_feed.setting import config as cfg
from joe_feed.setting.Languages import Languages as lang
from joe_feed.setting.Languages import Translated as tsl

# head = "https://rsshub.app/wsj/en-us/"
kbs = [
    ["https://rsshub.app/kbs/today",   "kbs_eng", cfg.kbs, lang.eng, tsl.y],
    ["https://rsshub.app/kbs/today/r", "kbs_rus", cfg.kbs, lang.rus, tsl.n],
    ["https://rsshub.app/kbs/today/s", "kbs_spa", cfg.kbs, lang.spa, tsl.n],
    ["https://rsshub.app/kbs/today/f", "kbs_fra", cfg.kbs, lang.fra, tsl.n],
    ["https://rsshub.app/kbs/today/j", "kbs_jpn", cfg.kbs, lang.jpn, tsl.n],
    ["https://rsshub.app/kbs/today/k", "kbs_kor", cfg.kbs, lang.kor, tsl.n],
    ["https://rsshub.app/kbs/today/v", "kbs_vie", cfg.kbs, lang.vie, tsl.n],
    ["https://rsshub.app/kbs/today/g", "kbs_deu", cfg.kbs, lang.deu, tsl.n],
]

# wsj = list( map(lambda i: [f"{head}{i[0]}", i[1], cfg.wsj, lang.eng, tsl.y], wsj_sim) )

# ------------------------------------------------
def main():
    [print(rl) for rl in kbs]
# ------------------------------------------------

if __name__ == '__main__':
    main()
