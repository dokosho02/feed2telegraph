from joef2t.utils.web import webCode
from joef2t.utils.html import removeAttrExceptHrefSrc

from bs4 import BeautifulSoup


class AVItem():
    def __init__(self, link):
        # super().__init__(link, title, config, lang)
        self.link = link

        self.title   = ""
        self.text    = ""
        self.actress = []
        self.date    = ""
        self.series  = []
        self.genre   = []
        # self.director= None
        self.number  = ""
        self.time    = ""
        # self.price   = None
        self.videoUrl= ""
        self.imgUrls = []
        
        self.contents = ""
        self.keyWords = []
    # -----------------------------------------------
    def getNumber(self):
        self.number = self.link.split("/")[-1]
    # -----------------------------------------------
    def parse(self):
        self.getNumber()

        code = webCode(self.link)
        soup = BeautifulSoup(code, "html.parser")
        contents = soup.select("div.p-workPage.l-wrap")

        sp = BeautifulSoup(str(contents), "html.parser")
        self.title = sp.select("h2")[0].text.strip()

        self.text = sp.select("p[class=p-workPage__text]")[0].text.strip()

        links = sp.select("a")

        dates = []
        keys   = ["actress", "date", "series", "genre"]
        values = [self.actress, dates, self.series, self.genre]
        for lk in links:
            for (k,v) in zip(keys, values):
                if k in str(lk):
                    v.append(lk.text)

        self.date = dates[0]

        # video
        try:
            self.videoUrl = sp.select("video")[0].get("src")
        except:
            print(f"No video for {self.number}")
            self.videoUrl = None

        # images
        swiper = soup.select("div[class=swiper-container]")
        sp = BeautifulSoup(str(swiper), "html.parser")

        imgs = sp.select("img")
        for ig in imgs:
            self.imgUrls.append( ig.get("data-src") )

        # output
        if self.videoUrl:
            self.contents +=f"""
            <p><a href="{self.videoUrl}">Video</a></p>\n
            """

        self.contents += f"{self.text}\n\n"
        for asg in [self.actress, self.series, self.genre]:
            self.add2Contents(asg)
        
        self.contents += f"\n{self.number}\n\n"

        for ig in self.imgUrls:
            self.contents +=f"""<p><img src="{ig}"></p>\n"""

        self.keyWords = self.actress + self.series + self.genre

        print(self.title)
        print(self.contents)
    # -----------------------------------------------
    def getVideoUrlOutside(self):
        pass
    # -----------------------------------------------
    def add2Contents(self, lst):
        if len(lst) >0:
            for i in lst:
                self.contents +=f"{i}, "

            self.contents = self.contents.rstrip(", ")
            self.contents += "\n"
    # -----------------------------------------------

    def run(self):
        self.parse()