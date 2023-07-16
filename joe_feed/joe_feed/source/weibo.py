from joe_feed.setting import config as cfg
from joe_feed.setting.Languages import Languages as lang
from joe_feed.setting.Languages import Translated as tsl

head = "https://rsshub.app/weibo/user/"

usa_embassy_cn = [
    [f"{head}1743951792",    "usa_embassy_cn", cfg.usaEmCN, lang.zhs, tsl.n],
]

follow_sim = [
    ["6629766915", "Zweig_yesterday"], # 茨威格死于昨日世界
    ["6629766915", "li_snore"],        # 李小呼噜
]

# 
follow   = list( map(lambda i: [f"{head}{i[0]}", i[1], cfg.wxsl, lang.zhs, tsl.n], follow_sim) )


# ------------------------------------------------
weiboRSS = usa_embassy_cn # + 
# ------------------------------------------------
def main():
    [print(rl) for rl in weiboRSS]

# ------------------------------------------------

if __name__ == '__main__':
    main()
