from joe_feed.setting import config as cfg
from joe_feed.setting.Languages import Languages as lang
from joe_feed.setting.Languages import Translated as tsl


infoTech = [
    ["https://rsshub.app/sspai/index",             "sspai", cfg.daily, lang.zhs, tsl.n],
    ["https://rsshub.app/geekpark/breakingnews","geekPark", cfg.daily, lang.zhs, tsl.n],
    ["https://feeds.feedburner.com/bookfere",   "bookfere", cfg.daily, lang.zhs, tsl.n],
    ["https://www.techradar.com/rss",          "techRadar",   cfg.tcr, lang.eng, tsl.y],
    ["https://www.xda-developers.com/feed/",         "xda",   cfg.xda, lang.eng, tsl.n],
    ["https://rsshub.app/zhihu/daily",       "zhihu_daily",   cfg.zhd, lang.zhs, tsl.n],
    ["https://www.ithome.com/rss/",               "ithome",   cfg.ith, lang.zhs, tsl.n],
    # ["https://www.chongdiantou.com/feed",          "charger", cfg.chg, lang.zhs],
]

zaobao = [
    ["https://rsshub.app/zaobao/realtime/china",    "zaobao_cn", cfg.zbcg, lang.zhs, tsl.n],
    ["https://rsshub.app/zaobao/realtime/singapore","zaobao_sg", cfg.zbcg, lang.zhs, tsl.n],
]

politics = [
    ["https://rsshub.app/rfa", "rfa", cfg.rfa, lang.eng, tsl.y],
]

sputnik = [
    ["https://rsshub.app/sputniknews/world/japanese", "sputnik_jpn", cfg.sputnik, lang.jpn, tsl.n],
    ["https://rsshub.app/sputniknews/world/english",  "sputnik_eng", cfg.sputnik, lang.eng, tsl.y],
]

newsZhs = [
    # ["https://rss.huxiu.com/",               "huxiu",          cfg.huxiu, lang.zhs, tsl.n],    # text and video
    ["https://rsshub.app/thepaper/featured", "paper_featured", cfg.tpf,   lang.zhs, tsl.n],
    # ["https://rsshub.app/dapenti/tugua",      "penti_tugua",    cfg.daily, lang.zhs, tsl.n],
    # ["https://rsshub.app/dapenti/subject/184","penti_fushihui", cfg.daily, lang.zhs, tsl.n],
]

cdt = [
    ["https://chinadigitaltimes.net/chinese/feed/","cdt_zhs", cfg.cdt, lang.zhs, tsl.n ],
    ["https://chinadigitaltimes.net/feed/",        "cdt_eng", cfg.cdt, lang.eng, tsl.y ],
]

bbc = [
    ["https://rsshub.app/bbc/world-asia", "bbc_asia", cfg.bbc, lang.eng, tsl.y],
]

reu = [
    ["https://rsshub.app/reuters/world/china",        "reuters_china",        cfg.reu_cn, lang.eng, tsl.y],
    ["https://rsshub.app/reuters/world/asia-pacific", "reuters_asia_pacific", cfg.reu_cn, lang.eng, tsl.y],
]

nyt = [
    ["https://rsshub.app/nytimes/dual-traditionalchinese", "nyt_zht_eng", cfg.nyt, lang.eng, tsl.n],
]
# lang
langLearn = [
    ["https://biz.trans-suite.jp/feed",                    "biz-trans", cfg.jpn, lang.jpn, tsl.n],
    ["https://www.haru-no-nihongo.com/blog-feed.xml",       "haru_jpn", cfg.jpn, lang.jpn, tsl.n],
    # ["https://nihongonosensei.net/?feed=rss2", "leisurely_teacher_jpn", cfg.jpn, lang.jpn],
    ["https://kyoto-koshoken.com/feed/",           "koshoken", cfg.koshoken, lang.jpn, tsl.n],
]

# coding
codings = [
    ["https://rustcc.cn/rss",               "Rust_CC",        cfg.cgd, lang.zhs, tsl.n ],
    # ["http://www.oschina.net/news/rss",     "OSCHINA社区_新闻",cfg.cgd, lang.zhs ],
    # ["http://www.oschina.net/project/rss",  "OSCHINA社区_软件",cfg.cgd, lang.zhs ],
    # ["https://rsshub.app/yuque/doc/75258",  "Egg-Node-js",    cfg.cgd, lang.zhs, tsl.n ],
    ["https://blog.kotlin-academy.com/feed","Kotlin_Academy", cfg.cgd, lang.eng, tsl.n ],
    # ["https://www.raywenderlich.com/android/feed/","Kodeco",  cfg.cgd, lang.eng, tsl.n ],
    ["https://feeds.feedblitz.com/baeldung/kotlin","BaeldungKotlin",  cfg.cgd, lang.eng, tsl.n ],
]

university = [
    ["http://www.kyoto-u.ac.jp/ja/RSS","ktu", cfg.ktu, lang.jpn, tsl.n ],
]


# 
bbj = [
    ["https://www.billboard-japan.com/d_news/doc.xml", "billboard_ja", cfg.bbj, lang.jpn, tsl.n],
]

basics = infoTech + bbc