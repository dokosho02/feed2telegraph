from os.path import join
from pathlib import Path
import os

from joe_feed.utils.core.time import get_current_utc0
# ------------

odf = os.environ['odf']
parentFolder = join(odf, "apps", "feed2tele")

# ph = join( Path.home(), "cfg")
ph = join( parentFolder, "cfg")

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
wxsl = "wxsl"  # wxoa selected
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

# generate filename with current year and month
current = get_current_utc0()
database =join( parentFolder, "data", f"feeds_{str(current.year).zfill(4)}_{str(current.month).zfill(2)}.db" )
last_folder = join( parentFolder, "last" )

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
    date integer,
    contents text,
    authors text,
    language text,
    tags text,
    type text,
    iv_link text,
    read integer,
    starred integer,
    feed_id integer,
    FOREIGN KEY (feed_id) REFERENCES feeds (id)
);"""

    # feed_name text,
    # feed_link text,
    # feed_id integer,
    # translation text,
    # kakasi text,


# question_feed = "?"

feed_insert_sql = f"""INSERT INTO {feed_table_name}(title, link, language, channel, translated)
VALUES(?,?,?,?,?)
    """

article_insert_sql = f"""INSERT INTO {article_table_name}(title, link, date, contents, authors, language, tags, type, iv_link, read, starred, feed_id)
VALUES(?,?,?,?,?,?,?,?,?,?,?,?)
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

