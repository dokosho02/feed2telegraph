from pprint import pprint
from bs4 import BeautifulSoup
import requests, re

imgRegex = '<img (.*?)/>'

# from joef2t.utils.html import removeAttrExceptHrefSrc

def webCode(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'} # This is chrome, you can set whatever browser you like
    response = requests.get(url, headers=headers)
    return response.text

def removeAttrExceptHrefSrc(str2process):


    whitelist = ['a','img']

    soup = BeautifulSoup(str2process, "html.parser")

    for tag in soup.find_all(True):
        if tag.name not in whitelist:
            tag.attrs = {}
        else:
            attrs = dict(tag.attrs)
            for attr in attrs:
                if attr not in ['src','href', "data-src"]:
                    del tag.attrs[attr]
    return str(soup)

link = "https://mp.weixin.qq.com/s/J6sAMm8AP4euBEFURMuDvw"
# link = "https://mp.weixin.qq.com/s/KP8pVMvKVr5d8wpQRGULhg"
code = webCode(link)
soup = BeautifulSoup(code, "html.parser")
contentResult = soup.select("div#js_content")[0]

print(contentResult.text)

str2process = str(contentResult)
# imageTags = re.findall( imgRegex, str2process )

# pprint(imageTags)

# for imgt in imageTags:
#     s = f"<img {imgt}/>"
#     t = f"{s[:-2]}></img>"
#     print(s)
#     print(t)
#     str2process = str2process.replace(s,t)

cont = removeAttrExceptHrefSrc( str2process ).replace("data-src", "src")#.replace("<section><span> </span></section>", "")
#.replace("<span>", "<p>").replace("</span>", "</p>")

print(cont)
