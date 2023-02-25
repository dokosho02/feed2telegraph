from os.path import join
from pathlib import Path

# ------------



parentFolder = "/Users/user/Library/CloudStorage/OneDrive-mails.ucas.ac.cn/apps/feed2telegraph"

ph = join( Path.home(), "cfg")

glossaryEng = join(ph, "glossary_eng.md")

ext = "configure.text"

# ---------------------------------------------------------
def getFilepath(name_str):
    fullPath = ""
    if name_str!="":
        fullPath =  join(ph, f"{name_str}_{ext}")
    else:
        fullPath =  join(ph, ext)
    return fullPath
# ---------------------------------------------------------
conf  = ""

# log
logChannel = getFilepath("log")

# specific channel
ecn   = "ecn"        # economist
ecnfe ="ecnfe"

huxiu ="huxiu"      # 
tpf ="tpf"          # 澎湃新闻
ith = "ith"          # IT home

bbc   = "bbc"
nyt   = "nyt"

zbcg  = "zbcg"       # zaobao, high F
jpn   = "jpn"
wsj   = "wsj"
tcr   = "techradar"  # tech, high F
xda   = "xda"        # tech, high F
zhd   = "zhd"

reu_cn = "reu_cn"

rfa   = "rfa"
kbs   = "kbs"
cdt   = "cdt"
sputnik="sputnik"

daily = "daily"

yomi_n = "yomi_n"
yomi_w = "yomi_w"
yomi_l = "yomi_l"
yomi_e = "yomi_e"

yjn   = "yjn"
yjnb  = "yjnb"    # business and life
yjni  = "yjni"    # it and science
yjne  = "yjne"
yjnl  = "yjnl"
yjns  = "yjns"

yjt   = "yjt"
bbj   = "bbj"

koshoken = "kshk"
ktu   = "ktu"


# coding

cgd = "cgd"

# weibo
usaEmCN = "usaEmCN"
weibo = "weibo"

# wexin
wxoa = "wxoa"
wxsl = "wxsl"  #z wxoa selected
wxhm = "wxhm"
HIMMR= "himmr"
univ = "univ"
prnt = "prnt"

# important
journals = "journals"

# web
avf = "avf"
# 
# vocabulary = "vcb"



# sql

database = r"feedsArticles.db"
feed_table_name = "feeds"
article_table_name = "articles"

sql_create_feeds_table = f"""CREATE TABLE IF NOT EXISTS {feed_table_name} (
    id integer PRIMARY KEY,
    title text NOT NULL,
    link text,
    language text,
    channel text,
    translated integer
); """

sql_create_articles_table = f"""CREATE TABLE IF NOT EXISTS {article_table_name} (
    id integer PRIMARY KEY,
    title text,
    link text,
    date text,
    contents text,
    authors text,
    language text,
    tags text,
    type text,
    read integer,
    starred integer,
    kakasi text,
    translation text,
    feed_name text,
    feed_link text,
    feed_id integer,
    FOREIGN KEY (feed_id) REFERENCES feeds (id)
);"""

feed_insert_sql = f"""INSERT INTO {feed_table_name}(title, link, language, channel, translated)
VALUES(?,?,?,?,?)
    """

article_insert_sql = f"""INSERT INTO {article_table_name}(title, link, date, contents, authors, language, tags, type,read, starred, kakasi, translation, feed_name, feed_link, feed_id)
VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
"""
select_feed_sql = f"""SELECT * FROM {feed_table_name} WHERE link="""


# ------------------------
def main():
    lst = [conf, huxiu, jpn, wsj, kbs, tcr, journals]
    for l in lst:
        print(l)
# ------------------------
if __name__ == '__main__':
    main()

