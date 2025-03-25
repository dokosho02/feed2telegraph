from html_telegraph_poster import TelegraphPoster

def write2Telegraph(title, content, author=""):
    t = TelegraphPoster(use_api=True)
    t.create_api_token('FeedBot')
    res = t.post(
        title=title,
        author="",
        text=content,
    )
    return res["url"]

"""
async def write2Telegraph0(title, content, author):
    from telegraph_api import Telegraph

    telegraph = Telegraph()
    # Creating new account
    await telegraph.create_account(
        "FeedBot",
        author_name=author
    )
    # Creating new page
    new_page = await telegraph.create_page(
        title,
        content_html= content,
    )
    # Printing page url into console
    print(new_page.url)
    return new_page.url
"""
