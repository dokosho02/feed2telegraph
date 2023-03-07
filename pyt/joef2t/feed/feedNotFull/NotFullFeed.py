from joef2t.feed.Feed import Feed

class NotFullFeed(Feed):
    def __init__(self,link, title, config, lang, translated ):
        super().__init__(link, title, config, lang, translated)
    # -------------------------------
    def getItemContents(self, entry):
        # title
        entryTitle  = entry["title"]
        entryLink   = entry["link"]

        entryContent, entryAuthors, entryTags = self.getItemFull(entryLink)

        return (entryTitle, entryContent, entryLink, entryAuthors, entryTags)

    # -------------------------------
    def getItemFull(self, entryLink):
        return ("", [], [])

# --------------------------

# --------------------------
def main():
    WeiXinFeed("https://feeddd.org/feeds/61f3d472dca58a380c4fc12e","old_driver_fe", cfg.wxoa, lang.zhs, tsl.n)

# --------------------------

if __name__ == '__main__':
    main()