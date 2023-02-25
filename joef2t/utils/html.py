from bs4 import BeautifulSoup
import pprint



# remove all attributes except some tags(only saving ['href','src'] attr)
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
# ------------------------

def removeParasInImageSrc(str2process):
    pass
# ------------------------
# ------------------------
def retainText(str2process):
    soup = BeautifulSoup(str2process, "html.parser")
    return soup.text

# ------------------------




def main():
    test_str = """
    <img src="01.png" height="600"/>
    <a href="test.html" refer=""></a>
    <p class="01">hi</p>
    <h1 id="01">Test<h1>
    """

    test_str = removeAttrExceptHrefSrc(test_str)
    pprint.pprint(test_str)

# ------------------------
if __name__ == '__main__':
    main()
