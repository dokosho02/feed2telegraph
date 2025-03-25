from joef2t.setttings import config
from joef2t.setttings.Languages import Languages as lang
from joef2t.setttings.Languages import Translated as tsl

head = "https://rsshub.app/wechat/ershicimi/"

# link, name, channel, language, translation
ershicimi = [
    # selected
    ["N3WgvL3M",       "thatNG"],
]

ershicimiRSS = list(
    map(lambda i: [f"{head}/{i[0]}", i[1], cfg.wxsl, lang.zhs, tsl.n], ershicimi)
)

journalRSS = elsevierRSS # + springerRSS
# ------------------------------------------------
def main():    
    [print(rl) for rl in ershicimiRSS]

    
# ------------------------------------------------

if __name__ == '__main__':
    main()
