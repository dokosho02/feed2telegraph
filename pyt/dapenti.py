import feedparser
from pprint import pprint
import telegram_send as ts
import markdownify
import re

import joef2t.setttings.config as cfg

feedUrl = "https://rsshub.app/dapenti/tugua"
feed = feedparser.parse(feedUrl)
last = feed["entries"][1]
title = last["title"]
contents = last["summary"]

pprint(title)

pprint(contents)

print("--------\n")

cs = contents.split("<p>\n【")
for c in cs[1:]:
    t = f"<p>\n【{c}"
    print(f"{t}\n--------\n")

html4Telegraph = """
<p>
【24】<a class="ALink_default_2ibt1" href="https://weibo.com/u/6635013376">@快乐星球宿管阿姨</a> 
</p>
<div class="detail_wbtext_4CRf9">
啊啊啊啊啊啊哈哈哈哈哈哈笑晕
</div>
<p>
<img alt="" src="https://www.dapenti.com:99/dapenti/a63fd778/b905a2c8.jpg" /> 
</p>
"""


# sendWord = markdownify.markdownify(sendWord, heading_style="ATX")
# # sendWord.replace("\n+", "\n")
# sendWord = re.sub('\n+', '\n', sendWord)

# pprint(sendWord)

# ts.send(
#     messages=[sendWord],
#     parse_mode="markdown",
#     conf=cfg.conf,
# )

imgs = []
# for i in range(8):
#     with open(f"{str(i+1).zfill(4)}.png", "rb") as f:
#         imgs.append(f)

f1 = open(f"0001.png", "rb")
imgs.append(f1)
f2 = open(f"0001.png", "rb")
imgs.append(f2)
ts.send(
    images=[imgs],
    conf=cfg.conf
)

# html4Telegraph = removeAttrExceptHrefSrc(html4Telegraph)
# resUrl = asyncio.run(
#     write2Telegraph(
#         title=f"test",
#         content = html4Telegraph,
#         author = "",
#     )
# )
# sendWord = resUrl
# ts.send(
#     messages=[sendWord],
#     parse_mode="markdown",
#     conf=cfg.conf
# )


"""
https://bobbyhadz.com/blog/python-replace-multiple-spaces-with-single-space
https://www.geeksforgeeks.org/how-to-convert-html-to-markdown-in-python/

"""
