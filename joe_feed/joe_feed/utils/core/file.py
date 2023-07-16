import codecs
import requests, os

from joe_feed.utils.core.terminal import TerminalColors

def createFile(path, text, mode ="w"):
    f = codecs.open(path, mode, encoding="utf-8"  )
    f.write(text.strip())
    f.close()

def readText(path):
    f = codecs.open(path, "r", encoding="utf-8")
    text = "".join(f.readlines())
    f.close()
    return text

def downloadFile(url, localPath):
    # replace non-ascii characters in url    ?

    # download
    r = requests.get(url, stream = True)
    with open(localPath,"wb") as f:
        for chunk in r.iter_content(chunk_size=1024):
            # writing one chunk at a time to pdf file
            if chunk:
                f.write(chunk)
    print(f"\t{TerminalColors.OKCYAN}{localPath}{TerminalColors.ENDC} file downloaded from link\n{url}")


# ------------------------
if __name__ == '__main__':
    print("file module loaded.")
