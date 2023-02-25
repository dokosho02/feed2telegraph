from joef2t.feed.Feed import Feed

url = "https://s1s1s1.com/works/date"

class ScrapeFeed(Feed):
    def __init__(self,link, title, config, lang, translated ):
        super().__init__(link, title, config, lang, translated)
        
        self.urls = []
        self.workUrls = []
    # -------------------------------