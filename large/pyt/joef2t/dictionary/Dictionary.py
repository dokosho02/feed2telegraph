from wiktionaryparser import WiktionaryParser

sp2 = "  "


class Dictionary():
    def __init__(self, word, lang):
        self.word  = word
        self.lang  = lang
        self.result = ""

    def wiktionary(self):
        # import

        parser = WiktionaryParser()

        wordResult = parser.fetch(self.word, self.lang)
        res = f"{self.word}\n"
        for w in wordResult:
            pronunciations = w["pronunciations"]["text"]
            for i in pronunciations:
                res+=f"{sp2}{i}\n"
            # [print(i) for i in ipa]
            res+="\n"

            definitions = w["definitions"]
            for d in definitions:
                partOfSpeech = d["partOfSpeech"]
                res+=f"{partOfSpeech}\n"
            # print(partOfSpeech)

                text = d["text"]
                count = 0
                for t in text:
                    res+=f"{sp2}{count}) {t}\n"
                    count+=1
                res+="\n"
            etymology = w["etymology"]
            res+=f"""Etymology\n{sp2}{etymology}\n{"-"*8}\n"""

        self.result = res
        # print(res)
