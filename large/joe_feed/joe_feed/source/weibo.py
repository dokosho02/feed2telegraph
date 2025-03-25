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
    ["1880927244", "weiphone_wb"],     # 威锋网
    ["5872636712", "water_mount_wb"],  # 水山水山水山

]

star_sim = [
    ["1712335175", "shiga_lam_wb"],    # 連詩雅Shiga
    ["1745697950", "roxanne_tong_wb"], # RoxanneTong湯洛雯
]

friends_sim = [
    ["2462706131","luo_da"],
    ["2311317345","luo_wang"],

]

# 
follow   = list( map(lambda i: [f"{head}{i[0]}", i[1], cfg.weibo, lang.zhs, tsl.n], follow_sim) )


# ------------------------------------------------
weiboRSS = usa_embassy_cn # + 
# ------------------------------------------------
def main():
    [print(rl) for rl in weiboRSS]

# ------------------------------------------------

if __name__ == '__main__':
    main()
