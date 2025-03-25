from joef2t.utils.telegra import write2Telegraph
import asyncio



def main():
    st = """
    have some figure
        have some figure
    have some figure
    have some figure
    have some figure
    have some figure
    have some figure
    have some figure
    have some figure
        have some figure
    have some figure
    have some figure
    have some figure
    have some figure
    have some figure
    have some figure    have some figure
        have some figure
    have some figure
    have some figure
    have some figure
    have some figure
    have some figure
    have some figure    have some figure
        have some figure
    have some figure
    have some figure
    have some figure
    have some figure
    have some figure
    have some figure    have some figure
        have some figure
    have some figure
    have some figure
    have some figure
    have some figure
    have some figure
    have some figure
    <figure><iframe src="/embed/https://cc3001.dmm.co.jp/litevideo/freepv/s/ssi/ssis00579/ssis00579_dm_w.mp4"></iframe></figure>"""
    resUrl = asyncio.run(
        write2Telegraph(
            title=f"test video four",
            content = st,
            author = "joe",
                )
    )
    print(resUrl)

main()