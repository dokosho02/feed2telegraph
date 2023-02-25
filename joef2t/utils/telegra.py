
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