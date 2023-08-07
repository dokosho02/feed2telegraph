from joef2t.feed.Feed import Feed
from joef2t.feed.feedNotFull.YJFeed import YJFeed
from joef2t.feed.feedNotFull.WXOAFeed import WXOAFeed
from joef2t.feed.feedNotFull.BillBoardJa import BillBoardJa

from joef2t.setttings.journals import journalRSS
from joef2t.setttings import config as cfg
from joef2t.setttings.Languages import Languages as lang
from joef2t.setttings.Languages import Translated as tsl

from joef2t.feed.scrape.av.AVFeed import AVFeed

# -----------------------------------------

# -----------------------------------------
infoTech = [
    ["https://rsshub.app/sspai/index",             "sspai", cfg.daily, lang.zhs, tsl.n],
    ["https://rsshub.app/geekpark/breakingnews","geekPark", cfg.daily, lang.zhs, tsl.n],
    # ["https://feeds.feedburner.com/bookfere",   "bookfere", cfg.daily, lang.zhs, tsl.n],
    # ["https://www.techradar.com/rss",            "techRadar", cfg.tcr, lang.eng, tsl.y],
    # ["https://www.xda-developers.com/feed/",           "xda", cfg.xda, lang.eng, tsl.n],
    ["https://rsshub.app/zhihu/daily",         "zhihu_daily", cfg.zhd, lang.zhs, tsl.n],
    ["https://www.ithome.com/rss/",                 "ithome", cfg.ith, lang.zhs, tsl.n],
    # ["https://www.chongdiantou.com/feed",          "charger", cfg.chg, lang.zhs],
    
]
    # -----------------------------------------

newsZhs = [
    ["https://rss.huxiu.com/",               "huxiu",          cfg.huxiu, lang.zhs, tsl.n],
    ["https://rsshub.app/thepaper/featured", "paper_featured", cfg.tpf,   lang.zhs, tsl.n],
    # ["https://rsshub.app/dapenti/tugua",      "penti_tugua",    cfg.daily, lang.zhs, tsl.n],
    # ["https://rsshub.app/dapenti/subject/184","penti_fushihui", cfg.daily, lang.zhs, tsl.n],
]
# -----------------------------------------
wsj = [
    ["https://rsshub.app/wsj/en-us/opinion",     "wsj-opinion",   cfg.wsj, lang.eng, tsl.n],
    ["https://rsshub.app/wsj/en-us/world_news",  "wsj-world",     cfg.wsj, lang.eng, tsl.n],       #  WSJ world
    ["https://rsshub.app/wsj/en-us/technology",  "wsj-tech",      cfg.wsj, lang.eng, tsl.n],    # WSJ tech
    ["https://rsshub.app/wsj/en-us/lifestyle",   "wsj-lifestyle", cfg.wsj, lang.eng, tsl.n],#      // WSJ lifestyle
    ["https://rsshub.app/wsj/en-us/market_news", "wsj-market",    cfg.wsj, lang.eng, tsl.n], #        // WSJ market
    ["https://rsshub.app/wsj/en-us/us_bussiness","wsj-bussiness", cfg.wsj, lang.eng, tsl.n], #       // WSJ bussiness us
]
# -----------------------------------------
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

economist = [
    ["https://rsshub.app/economist/the-world-this-week",   "economist_world",                 cfg.ecn, lang.eng, tsl.n],
    ["https://rsshub.app/economist/letters",               "economist_letters",               cfg.ecn, lang.eng, tsl.n],
    ["https://rsshub.app/economist/leaders",               "economist_leaders",               cfg.ecn, lang.eng, tsl.n],
    ["https://rsshub.app/economist/briefing",              "economist_briefing",              cfg.ecn, lang.eng, tsl.n],
    ["https://rsshub.app/economist/special-report",        "economist_special-report",        cfg.ecn, lang.eng, tsl.n],
    ["https://rsshub.app/economist/britain",               "economist_britain",               cfg.ecn, lang.eng, tsl.n],
    ["https://rsshub.app/economist/europe",                "economist_europe",                cfg.ecn, lang.eng, tsl.n],
    ["https://rsshub.app/economist/united-states",         "economist_united-states",         cfg.ecn, lang.eng, tsl.n],
    ["https://rsshub.app/economist/the-americas",          "economist_the-americas",          cfg.ecn, lang.eng, tsl.n],
    ["https://rsshub.app/economist/middle-east-and-africa","economist_middle-east-and-africa",cfg.ecn, lang.eng, tsl.n],
    ["https://rsshub.app/economist/asia",                  "economist_asia",                  cfg.ecn, lang.eng, tsl.n],
    ["https://rsshub.app/economist/china",                 "economist_china",                 cfg.ecn, lang.eng, tsl.y],
    ["https://rsshub.app/economist/international",         "economist_international",         cfg.ecn, lang.eng, tsl.n],
    ["https://rsshub.app/economist/business",              "economist_business",              cfg.ecn, lang.eng, tsl.n],
    ["https://rsshub.app/economist/finance-and-economics", "economist_finance-and-economics", cfg.ecnfe, lang.eng, tsl.y],
    ["https://rsshub.app/economist/science-and-technology","economist_science-and-technology",cfg.ecn, lang.eng, tsl.n],
    ["https://rsshub.app/economist/books-and-arts",        "economist_books-and-arts",        cfg.ecn, lang.eng, tsl.n],
    ["https://rsshub.app/economist/obituary",              "economist_obituary",              cfg.ecn, lang.eng, tsl.n],
    ["https://rsshub.app/economist/graphic-detail",        "economist_graphic-detail",        cfg.ecn, lang.eng, tsl.n],
    ["https://rsshub.app/economist/economic-and-financial-indicators", "economist_indicators",cfg.ecn, lang.eng, tsl.n],
]

# -----------------------------------------
langLearn = [
    ["https://biz.trans-suite.jp/feed",                    "biz-trans", cfg.jpn, lang.jpn, tsl.n],
    ["https://www.haru-no-nihongo.com/blog-feed.xml",       "haru_jpn", cfg.jpn, lang.jpn, tsl.n],
    # ["https://nihongonosensei.net/?feed=rss2", "leisurely_teacher_jpn", cfg.jpn, lang.jpn],
    # ["https://kyoto-koshoken.com/feed/",           "koshoken", cfg.koshoken, lang.jpn, tsl.n],
]

bbj = [
    ["https://www.billboard-japan.com/d_news/doc.xml", "billboard_ja", cfg.bbj, lang.jpn, tsl.n],
]
# -----------------------------------------
# -----------------------------------------
politics = [
    ["https://rsshub.app/rfa", "rfa", cfg.rfa, lang.eng, tsl.n],
]
    # -----------------------------------------
sputnik = [
    ["https://rsshub.app/sputniknews/world/japanese", "sputnik_jpn", cfg.sputnik, lang.jpn, tsl.n],
    ["https://rsshub.app/sputniknews/world/english",  "sputnik_eng", cfg.sputnik, lang.eng, tsl.y],
]

# -----------------------------------------
zaobao = [
    ["https://rsshub.app/zaobao/realtime/china",    "zaobao_cn", cfg.zbcg, lang.zhs, tsl.n],
    # ["https://rsshub.app/zaobao/realtime/singapore","zaobao_sg", cfg.zbcg, lang.zhs, tsl.n],
]
# -----------------------------------------
bbc = [
    ["https://rsshub.app/bbc/world-asia", "bbc_asia", cfg.bbc, lang.eng, tsl.y],
]
# -----------------------------------------
nyt = [
    ["https://rsshub.app/nytimes/dual-traditionalchinese", "nyt_zht_eng", cfg.nyt, lang.eng, tsl.n],
]
# -----------------------------------------
reu = [
    ["https://rsshub.app/reuters/world/china",        "reuters_china",        cfg.reu_cn, lang.eng, tsl.y],
    ["https://rsshub.app/reuters/world/asia-pacific", "reuters_asia_pacific", cfg.reu_cn, lang.eng, tsl.y],
]

cdt = [
    ["https://chinadigitaltimes.net/chinese/feed/","cdt_zhs", cfg.cdt, lang.zhs, tsl.n ],
    ["https://chinadigitaltimes.net/feed/",        "cdt_eng", cfg.cdt, lang.eng, tsl.y ],
]

yomiuri = [
    ["https://rsshub.app/yomiuri/national","yomiuri_national", cfg.yomi_n, lang.jpn, tsl.n ],
    ["https://rsshub.app/yomiuri/world",   "yomiuri_world",    cfg.yomi_w, lang.jpn, tsl.n ],
    ["https://rsshub.app/yomiuri/local",   "yomiuri_local",    cfg.yomi_l, lang.jpn, tsl.n ],
    ["https://rsshub.app/yomiuri/economy", "yomiuri_economy",  cfg.yomi_e, lang.jpn, tsl.n ],

]

# -----------------------------------------

yjnews  = [
    ["https://news.yahoo.co.jp/rss/media/bbc/all.xml","BBC_News", cfg.bbc, lang.jpn, tsl.n ],
    ["https://news.yahoo.co.jp/rss/media/kyodonews/all.xml","kyodo_News", cfg.kyodo, lang.jpn, tsl.n ],
    ["https://news.yahoo.co.jp/rss/media/rescuenow/all.xml","rescuenow", cfg.rescue, lang.jpn, tsl.n ],
    ["https://news.yahoo.co.jp/rss/media/tenki/all.xml","tenki", cfg.rescue, lang.jpn, tsl.n ],

    # it
    ["https://news.yahoo.co.jp/rss/media/zdn_m/all.xml",   "zdn_m", cfg.yjni, lang.jpn, tsl.n ],
    ["https://news.yahoo.co.jp/rss/media/impress/all.xml", "impress_watch", cfg.yjni, lang.jpn, tsl.n ],
    ["https://news.yahoo.co.jp/rss/media/krjapan/all.xml", "36Kr_ja", cfg.yjni, lang.jpn, tsl.n ],

    # world
    ["https://news.yahoo.co.jp/rss/media/cnn/all.xml",      "cnn_jpn", cfg.yjn, lang.jpn, tsl.n ],

    # life
    ["https://news.yahoo.co.jp/rss/media/it_nlab/all.xml",     "nlab", cfg.yjnb, lang.jpn, tsl.n ],


    # entertainment
    # ["https://news.yahoo.co.jp/rss/media/nksports/all.xml", "nksports", cfg.yjne, lang.jpn, tsl.n ],
    ["https://news.yahoo.co.jp/rss/media/oric/all.xml", "oric", cfg.yjne, lang.jpn, tsl.n ],
    ["https://news.yahoo.co.jp/rss/media/bunshun/all.xml", "bunshun", cfg.yjne, lang.jpn, tsl.n ],
    ["https://news.yahoo.co.jp/rss/media/exp/all.xml", "bbj_exp", cfg.yjne, lang.jpn, tsl.n ],



    # ["https://news.yahoo.co.jp/rss/topics/top-picks.xml",  "yj_top_picks", cfg.yjt ], # delete
    # ["https://news.yahoo.co.jp/rss/categories/domestic.xml","yj_domestic", cfg.yjn, lang.jpn, tsl.n ],
    # ["https://news.yahoo.co.jp/rss/categories/world.xml",      "yj_world", cfg.yjn, lang.jpn, tsl.n ],
    # ["https://news.yahoo.co.jp/rss/categories/business.xml","yj_business", cfg.yjnb, lang.jpn, tsl.n ],
    # ["https://news.yahoo.co.jp/rss/categories/life.xml",        "yj_life", cfg.yjnb, lang.jpn, tsl.n ],
    # ["https://news.yahoo.co.jp/rss/categories/it.xml",            "yj_it", cfg.yjni, lang.jpn, tsl.n ],
    # ["https://news.yahoo.co.jp/rss/categories/science.xml",  "yj_science", cfg.yjni, lang.jpn, tsl.n ],
]

yjnews2  = [
    # ["https://news.yahoo.co.jp/rss/categories/entertainment.xml","yj_entertainment", cfg.yjne, lang.jpn, tsl.n ],
    # ["https://news.yahoo.co.jp/rss/categories/local.xml",                "yj_local", cfg.yjnl, lang.jpn, tsl.n ],
    # ["https://news.yahoo.co.jp/rss/categories/sports.xml",              "yj_sports", cfg.yjns, lang.jpn, tsl.n ],
]


university = [
    ["http://www.kyoto-u.ac.jp/ja/RSS","ktu", cfg.ktu, lang.jpn, tsl.n ],
]

codings = [
    ["https://rustcc.cn/rss",               "Rust_CC",        cfg.cgd, lang.zhs, tsl.n ],
    # ["http://www.oschina.net/news/rss",     "OSCHINA社区_新闻",cfg.cgd, lang.zhs ],
    # ["http://www.oschina.net/project/rss",  "OSCHINA社区_软件",cfg.cgd, lang.zhs ],
    ["https://rsshub.app/yuque/doc/75258",  "Egg-Node-js",    cfg.cgd, lang.zhs, tsl.n ],
    ["https://blog.kotlin-academy.com/feed","Kotlin_Academy", cfg.cgd, lang.eng, tsl.n ],
    ["https://www.raywenderlich.com/android/feed/","Kodeco",  cfg.cgd, lang.eng, tsl.n ],
    ["https://feeds.feedblitz.com/baeldung/kotlin","BaeldungKotlin",  cfg.cgd, lang.eng, tsl.n ],
    ["https://rsshub.app/wechat/ershicimi/RjlPAljD", "CoderAlliance", cfg.wxoa, lang.zhs, tsl.n],
]

weibo = [
    ["https://rsshub.app/weibo/user/1743951792",    "usa_embassy_cn", cfg.usaEmCN, lang.zhs, tsl.n],

]

ershicimi = [
    # selected
    ["https://rsshub.app/wechat/ershicimi/N3WgvL3M",       "thatNG", cfg.wxsl, lang.zhs, tsl.n],
    ["https://rsshub.app/wechat/ershicimi/rQA9kZQZ", "FengXueRong",  cfg.wxsl, lang.zhs, tsl.n],
    ["https://rsshub.app/wechat/ershicimi/XQJ4VnOb", "briefHistory", cfg.wxsl, lang.zhs, tsl.n],
    ["https://rsshub.app/wechat/ershicimi/dOVgBkje", "polar_day_stu",cfg.wxsl, lang.zhs, tsl.n],    # "https://api.feeddd.org/feeds/619db3b5486e3727fb037fa5"
    ["https://rsshub.app/wechat/ershicimi/wDOqGBQ4", "old_driver_business", cfg.wxsl, lang.zhs, tsl.n], # "https://api.feeddd.org/feeds/61f3d472dca58a380c4fc131"
    ["https://rsshub.app/wechat/ershicimi/EOd8GKO4",        "mylifeano",    cfg.wxsl, lang.zhs, tsl.n],
    ["https://rsshub.app/wechat/ershicimi/LRjlqAQD",        "diqiuzhishiju",cfg.wxsl, lang.zhs, tsl.n],
    # ["https://rsshub.app/wechat/ershicimi/M3ekLwjl",        "Doctor_X",     cfg.wxsl, lang.zhs, tsl.n],    # "https://api.feeddd.org/feeds/613381fa1269c358aa0eafc9"
    ["https://rsshub.app/wechat/ershicimi/mQ4RDeO4",        "guokr42",      cfg.wxsl, lang.zhs, tsl.n],
    # code
    ["https://rsshub.app/wechat/ershicimi/NjpEdVQB",      "osc_ops",  cfg.cgd,  lang.zhs, tsl.n],    # "https://api.feeddd.org/feeds/61514f7e1269c358aa13c8e5"
    # ["https://rsshub.app/wechat/ershicimi/dOVD2m7Q",      "coderLib", cfg.wxoa, lang.zhs, tsl.n],
    # ["https://rsshub.app/wechat/ershicimi/nqQBbQz0", "pyt_community", cfg.wxoa, lang.zhs, tsl.n],
    # ["https://rsshub.app/wechat/ershicimi/vdOVar3e",      "coderHui", cfg.wxoa, lang.zhs, tsl.n],
    # ["https://rsshub.app/wechat/ershicimi/PQDwYGNj",    "readPoems",  cfg.wxoa, lang.zhs, tsl.n],

    # daily
    ["https://rsshub.app/wechat/ershicimi/2jr1rwOY",        "appso",  cfg.daily, lang.zhs, tsl.n],    # "https://api.feeddd.org/feeds/612703b0221f954f5e10f936"
    ["https://rsshub.app/wechat/ershicimi/13oVxvQl",        "szdays", cfg.daily, lang.zhs, tsl.n],
    
    # university
    ["https://rsshub.app/wechat/ershicimi/dOVlr5Qe",        "whu", cfg.univ, lang.zhs, tsl.n],
    ["https://rsshub.app/wechat/ershicimi/23nX61yj",       "hust", cfg.univ, lang.zhs, tsl.n],
    ["https://rsshub.app/wechat/ershicimi/NjYk0Rb3",      "hkust", cfg.univ, lang.zhs, tsl.n],
    ["https://rsshub.app/wechat/ershicimi/bO9lBdp3",       "xjtu", cfg.univ, lang.zhs, tsl.n],

    # humor
    # ["https://rsshub.app/wechat/ershicimi/M3e0nnQl",        "meipinbaike",  cfg.wxhm, lang.zhs, tsl.n],
    # ["https://rsshub.app/wechat/ershicimi/RjGz4zO9",        "hahahabzc",    cfg.wxhm, lang.zhs, tsl.n],
    # ["https://rsshub.app/wechat/ershicimi/23nKB0Ox",        "lengtoo",      cfg.wxhm, lang.zhs, tsl.n],
    # ["https://rsshub.app/wechat/ershicimi/43MxPdQE",        "jokeSelected", cfg.wxhm, lang.zhs, tsl.n],
    # ["https://rsshub.app/wechat/ershicimi/KQ22ADQL",        "ibaoman",      cfg.wxhm, lang.zhs, tsl.n],
    # ["https://rsshub.app/wechat/ershicimi/zQmpE9jN",        "hkspot", cfg.wxoa, lang.zhs, tsl.n],
    # ["https://rsshub.app/wechat/ershicimi/V3LR9YPj",        "oldSongsForBed", cfg.wxoa, lang.zhs, tsl.n],
    # ["https://rsshub.app/wechat/ershicimi/XjZ7R1Qw",        "readingclub_btfx", cfg.wxoa, lang.zhs, tsl.n],
    # ["https://rsshub.app/wechat/ershicimi/DV3LxW3Y",        "zhanhao668", cfg.wxoa, lang.zhs, tsl.n],
    # ["https://rsshub.app/wechat/ershicimi/x30VLyjo",        "DongJian", cfg.wxoa, lang.zhs, tsl.n],
    # ["https://rsshub.app/wechat/ershicimi/emQ4AY34",        "youshucc", cfg.wxoa, lang.zhs, tsl.n],
    
    # HIMMR
    ["https://rsshub.app/wechat/ershicimi/4QkVznja",       "HowImetMrRight", cfg.HIMMR, lang.zhs, tsl.n],
    ["https://rsshub.app/wechat/ershicimi/M3eZ4LlO",        "HIMMRshanghai", cfg.HIMMR, lang.zhs, tsl.n],
    ["https://rsshub.app/wechat/ershicimi/x30PngL3",          "HIMMRpeking", cfg.HIMMR, lang.zhs, tsl.n],
    ["https://rsshub.app/wechat/ershicimi/838JB2Mj",        "HIMMRhangchow", cfg.HIMMR, lang.zhs, tsl.n],
    ["https://rsshub.app/wechat/ershicimi/dOVoKa8j",          "HIMMRcanton", cfg.HIMMR, lang.zhs, tsl.n],
    ["https://rsshub.app/wechat/ershicimi/N3N7KWvO",         "HIMMRnanking", cfg.HIMMR, lang.zhs, tsl.n],
    
    # parenting
    # ["https://rsshub.app/wechat/ershicimi/1rQAAEQZ",        "niangao-mama", cfg.prnt, lang.zhs, tsl.n],
    # ["https://rsshub.app/wechat/ershicimi/4QkP4k3a",        "nverpai",      cfg.prnt, lang.zhs, tsl.n],
    # ["https://rsshub.app/wechat/ershicimi/13oV1oQl",        "boy666dj",     cfg.prnt, lang.zhs, tsl.n],
    # ["https://rsshub.app/wechat/ershicimi/pQaDarjJ",        "kexueyuer2012",cfg.prnt, lang.zhs, tsl.n],
    # ["https://rsshub.app/wechat/ershicimi/kzQmK4ON",        "doctor_DX",    cfg.prnt, lang.zhs, tsl.n],    # "https://api.feeddd.org/feeds/611f0dcc8fae751e236420c0"
    # ["https://rsshub.app/wechat/ershicimi/wDOq8g34",        "MotherDX",     cfg.prnt, lang.zhs, tsl.n],
    # ["https://rsshub.app/wechat/ershicimi/dOVVerOe",        "imingbailema", cfg.prnt, lang.zhs, tsl.n],  #https://api.feeddd.org/feeds/63c2828be1190840774cd9a3
    
    # general
    ["https://rsshub.app/wechat/ershicimi/dOVo5X0j",        "kekesil",      cfg.wxoa, lang.zhs, tsl.n],
    ["https://rsshub.app/wechat/ershicimi/9aj6dN34",        "QbitAI",       cfg.wxoa, lang.zhs, tsl.n],
    ["https://rsshub.app/wechat/ershicimi/XjZqoROw",        "vistaweek",    cfg.wxoa, lang.zhs, tsl.n],
    ["https://rsshub.app/wechat/ershicimi/vKQ1PKjJ",        "wallstreetcn", cfg.wxoa, lang.zhs, tsl.n],
    ["https://rsshub.app/wechat/ershicimi/23nnGy3x",        "chaintruth",   cfg.wxoa, lang.zhs, tsl.n],
    ["https://rsshub.app/wechat/ershicimi/rQAlE6jZ",       "shenrancaijing",cfg.wxoa, lang.zhs, tsl.n],
    ["https://rsshub.app/wechat/ershicimi/Rjl0r2jD",        "douban",       cfg.wxoa, lang.zhs, tsl.n],
    ["https://rsshub.app/wechat/ershicimi/13ox11Ol",        "theLivings",   cfg.wxoa, lang.zhs, tsl.n],    # "https://api.feeddd.org/feeds/615d9e801269c358aa1632b9"
    ["https://rsshub.app/wechat/ershicimi/nXQJRNQb",        "renwumag1980", cfg.wxoa, lang.zhs, tsl.n],
     
    # ["https://rsshub.app/wechat/ershicimi/pQaDarjJ",        "xjtu", cfg.wxoa, lang.zhs, tsl.n],
    # ["https://rsshub.app/wechat/ershicimi/pQaDarjJ",        "xjtu", cfg.wxoa, lang.zhs, tsl.n],
    # ["https://rsshub.app/wechat/ershicimi/pQaDarjJ",        "xjtu", cfg.wxoa, lang.zhs, tsl.n],
    # ["https://rsshub.app/wechat/ershicimi/pQaDarjJ",        "xjtu", cfg.wxoa, lang.zhs, tsl.n],
    # ["https://rsshub.app/wechat/ershicimi/pQaDarjJ",        "xjtu", cfg.wxoa, lang.zhs, tsl.n],

    # ["https://rsshub.app/wechat/ershicimi/M3eJpPGO",        "HYSLBS", cfg.wxoa, lang.zhs, tsl.n],

]

weixin = [
    # ["https://api.feeddd.org/feeds/6123cf6051e2511a827a370f",        "common_sense", cfg.wxsl, lang.zhs, tsl.n],    # 
    # ["https://api.feeddd.org/feeds/6127a7c0221f954f5e110a8f",          "Cicero_sea", cfg.wxsl, lang.zhs, tsl.n],    # KQ1KZbOJ， 二十
    # ["https://api.feeddd.org/feeds/63c2828be1190840774cd9a3",      "doctor_G_child", cfg.wxoa, lang.zhs, tsl.n],
    # ["https://api.feeddd.org/feeds/612703b0221f954f5e10f936",               "appso", cfg.wxoa, lang.zhs, tsl.n],
    # ["https://api.feeddd.org/feeds/612703b0221f954f5e10f936",               "appso", cfg.wxoa, lang.zhs, tsl.n],
    # ["https://api.feeddd.org/feeds/612703b0221f954f5e10f936",               "appso", cfg.wxoa, lang.zhs, tsl.n],
    # ["https://api.feeddd.org/feeds/612703b0221f954f5e10f936",               "appso", cfg.wxoa, lang.zhs, tsl.n],
    # ["https://api.feeddd.org/feeds/612703b0221f954f5e10f936",               "appso", cfg.wxoa, lang.zhs, tsl.n],
]
# -----------------------------------------
# -----------------------------------------
# -----------------------------------------
# -----------------------------------------
def hourly():
    # YJ News must be YJFeed(), not Feed()!
    links = newsZhs + economist + politics + zaobao + infoTech + langLearn + wsj + kbs + sputnik + bbc + nyt + reu + cdt + journalRSS + university + codings + weibo + yomiuri

    # -----------------------------------------
    for rss in links:
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
    # -----------------------------------------
    for rss in bbj:
        try:
            BillBoardJa(
                link  =rss[0],
                title =rss[1],
                config=rss[2],
                lang  =rss[3],
                translated =rss[4],
            ).run()
        except Exception as e:
            print(f"{rss[0]}\n{rss[1]}\n{e}")
    # -----------------------------------------
    # wexin
    for rss in weixin:
        try:
            WXOAFeed(
                link  =rss[0],
                title =rss[1],
                config=rss[2],
                lang  =rss[3],
                translated =rss[4],
            ).run()
        except Exception as e:
            print(f"{rss[0]}\n{rss[1]}\n{e}")

    for rss in ershicimi:
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
    # -----------------------------------------
    # YJ News must be YJFeed()!
    for rss in yjnews:
        try:
            YJFeed(
                link  =rss[0],
                title =rss[1],
                config=rss[2],
                lang  =rss[3],
                translated =rss[4],
            ).run()
        except Exception as e:
            print(f"{rss[0]}\n{rss[1]}\n{e}")

    # --------------------------
# def minutely():
#     for rss in yjnews2:
#         try:
#             YJFeed(
#                 link  =rss[0],
#                 title =rss[1],
#                 config=rss[2],
#                 lang  =rss[3],
#                 translated =rss[4],
#             ).run()
#         except Exception as e:
#             print(f"{rss[0]}\n{rss[1]}\n{e}")

    
# -----------------------------------------

def daily():
    urls = ["https://s1s1s1.com/"]
    for link in urls:
        try:
            AVFeed(link,"S1", cfg.avf, lang.jpn, tsl.n).run()
        except Exception as e:
            print(f"{link}\n{e}")
# -----------------------------------------

def test():
    links =  bbc
    # -----------------------------------------
    for rss in links:
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

# --------------------------

if __name__ == '__main__':
    # test()

    hourly()
    # minutely()

