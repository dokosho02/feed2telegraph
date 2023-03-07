from joef2t.feed.scrape.ScrapeFeed import ScrapeFeed
from joef2t.feed.scrape.av.AVItem import AVItem
from joef2t.utils.web import webCode

from bs4 import BeautifulSoup

class AVFeed(ScrapeFeed):
    def __init__(self, link, title, config, lang, translated ):
        super().__init__(link, title, config, lang, translated)
    # -------------------------------
    def getEntries(self):
        # catalogue page
        worksPage = f"{self.link}works/date"
        code = webCode(worksPage)
        soup = BeautifulSoup(code, "html.parser")
        contents = soup.select("div[class=content]")
        
        # all links in contents - date pages
        for ct in contents:
            sp = BeautifulSoup(str(ct), "html.parser")
            links = sp.select("a")

            for lk in links:
                (self.urls).append(lk.get("href"))
        
        for url in self.urls[:1]:
            self.parseDayPage(url)

        # [print(i) for i in self.workUrls]
        self.entries = self.workUrls
    # -------------------------------
    def parseDayPage(self, url):
        code = webCode(url)
        soup = BeautifulSoup(code, "html.parser")
        contents = soup.select("div[class=swiper-wrapper]")

        sp = BeautifulSoup(str(contents), "html.parser")
        links = soup.select("a.img.hover")

        # print(len(links))
        for lk in links:
            (self.workUrls).append(lk.get("href"))
    
    # -----------------------------------
    def getNewItems(self):
        if len(self.lastLinks) > 0:
            for et in self.workUrls:
                if et not in self.lastLinks:
                    self.newItems.append(et)
        else:
            self.newItems=self.workUrls
    # -------------------------------
    def processSingleItem(self, i):
        # self.parseDayPage(i)
        
        url = self.newItems[i]
        avt = AVItem(url)
        avt.run()
        
        entryTitle   = avt.title
        entryAuthors = []
        entryLink    = avt.link
        dt           = avt.date
        entryTags    = avt.keyWords
        entryContent = avt.contents

        return (entryTitle, entryContent, entryLink, entryAuthors, entryTags, dt)
    # -------------------------------
    def getLinksFromEntries(self):
        self.lastString = ""
        for et in self.workUrls:
            self.lastString += f"""{et}\n"""
    # -------------------------------
    def top(self):
        self.slides = []
        self.topUrl = f"{self.link}/top"
        code = webCode(self.topUrl)
        soup = BeautifulSoup(code, "html.parser")
        section = soup.select("section[class=l-slider]")

        sp = BeautifulSoup(str(section), "html.parser")

        imgs = sp.select("img")
        for ig in imgs:
            self.slides.append( ig.get("data-src") )
        self.slides = list(set(self.slides))
        
        print(len(self.slides))
        [print(i) for i in self.slides]
    # --------------------------
    # def run(self):
    #     self.createFolders()
    #     self.getBackups()
    #     self.getEntries()
    # #     # self.entries = ["https://s1s1s1.com/works/detail/SSIS646"]
    #     self.removeOldItems()

    #     self.write2sql()
    #     self.processNewItems()
