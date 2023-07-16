
from telegraph_api import Telegraph

async def write2Telegraph(title, content, author):
    telegraph = Telegraph()
    # Creating new account
    await telegraph.create_account("FeedBot", author_name=author)
    # Creating new page
    new_page = await telegraph.create_page(
        title,
        content_html= content,
    )
    # Printing page url into console
    print(new_page.url)
    return new_page.url




import joe_feed.utils.core.sqliteBind as sqliteBind
import joe_feed.setting.config as cfg
# ------------------------------------------------
def get_updates():
    conn = sqliteBind.create_connection(cfg.database)

    if conn is not None:
        articles = []
        titles = []
        rows = sqliteBind.select_items_by_property(conn, cfg.article_table_name, p="read",v=0)
        if len(rows) > 0:
            for ro in rows:
                articles.append(ro)

        for article in articles:
            # update_read(article[0])

            (   id,
                title,
                link,
                time,
                contents,
                authors,
                lang,
                tags,
                item_type,
                iv_link,
                read,
                starred,
                feed_id
            ) = article

            print(f"title: {title}")
            print(f"link: {link}")
            titles.append(title)

    return titles

from joe_feed.utils.core.html import removeAttrExceptHrefSrc
import asyncio

class DataItem():
    def __init__(self,
        title,
        link,
        time,
        contents,
        authors,
        lang,
        tags,
        item_type,
        iv_link,
        read,
        starred,
        feed_id
    ):
        self.title     = title
        self.link      = link
        self.time      = time
        self.contents  = contents
        self.authors   = authors
        self.lang      = lang
        self.tags      = tags   
        self.type      = item_type
        self.iv_link   = iv_link
        self.read      = read
        self.starred   = starred 
        self.feed_id   = feed_id

        self.html4Telegraph = f"""
        <p><a href="{self.link}">Web</a></p>\n
        <h1>{self.title}</h1>\n
        <p><br/></p>\n
        <p>{self.time}</p>\n
        <p>{self.authors}</p>\n
        <p>tag(s): {self.tags}</p>\n
        """

    def get_feed(self):
        conn = sqliteBind.create_connection(cfg.database)
        feed = sqliteBind.select_items_by_property(conn, cfg.feed_table_name, p="id",v=self.feed_id)
        
        self.feed_link = feed[2]
        self.feed_name = feed[1]

        print(f"{self.feed_name}\n{self.feed_link}")

    def refineContents(self, cont):
        # if (self.link == "https://rss.huxiu.com/"):
        cont = cont.replace("""&nbsp;""", "").replace("<p><br/></p>", "").replace("<p></p>", "")
        if ( (self.feed_link == "https://chinadigitaltimes.net/chinese/feed/") or (self.feed_link == "https://chinadigitaltimes.net/feed/") ):
            cont = cont.replace("<blockquote>", "").replace("</blockquote>", "")

        return cont

    def write2Telegraph(self):
        contents = removeAttrExceptHrefSrc(self.contents)
        cont = self.refineContents(entryContent)


        self.html4Telegraph += f"""{cont}\n"""

        self.iv_link = asyncio.run(
            write2Telegraph(
                title   = f"{self.title} - {self.feed_name}",
                content = self.html4Telegraph,
                author  = self.authors
            )
        )


    def update_database(self):
        pass


# ------------------------
if __name__ == '__main__':
    get_updates()