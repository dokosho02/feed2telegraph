import pykakasi
import re

f = lambda x = "ddd" : sum ([1 if u"\u4e00" <= i <= u"\u9FD0" else 0 for i in x]) > 0


def replacePunc(test_str):
    res = re.sub(r'[^\w\s]', '', test_str)
    # print(type(res))
    return res

def kanaConvert(str2process):
    kks = pykakasi.kakasi()
    result = kks.convert(str2process)
    value = []
    for item in result:
        if (f(item["orig"])):
            orig = replacePunc(item['orig'])
            hira = replacePunc(item['hira'])
            print(f"{orig}: {hira}")
            value.append(f"{orig}: {hira}\n")
    
    res = [*set(value)]

    strFinal = ""
    for vl in res:
        strFinal +=vl

    return strFinal


"""
https://blog.csdn.net/gixome/article/details/123249482
https://www.geeksforgeeks.org/python-remove-punctuation-from-string/
"""