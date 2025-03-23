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
            # print(f"{orig}: {hira}")
            value.append(f"{orig}: {hira}\n")
    
    res = remove_duplicates_ordered(value)

    strFinal = ""
    for vl in res:
        strFinal +=vl

    return strFinal

def remove_duplicates_ordered(input_list):
    seen = set()
    result = []
    
    for item in input_list:
        if item not in seen:
            seen.add(item)
            result.append(item)
    
    return result

# original_list = [1, 2, 2, 3, 4, 4, 5, 1, 6]
# unique_list = remove_duplicates_ordered(original_list)
# print(unique_list)  # Output: [1, 2, 3, 4, 5, 6]



"""
https://blog.csdn.net/gixome/article/details/123249482
https://www.geeksforgeeks.org/python-remove-punctuation-from-string/
"""