
from joef2t.dictionary.Dictionary import Dictionary
from joef2t.setttings import config as cfg
from joef2t.utils.file import createFile, readText
from joef2t.utils.word import text2vocabulary, removeCJK

from tqdm import tqdm
# import pprint

# ----------------------------------

class Lookup():
    def __init__(self, glossaryFile, lang, text2process):
        self.glossaryFile  = glossaryFile
        self.lang          = lang
        self.text = removeCJK(text2process)

        self.glossary = []
        self.newVocab = []
        self.results = ""

        self.readGlossary()
        self.vocabulary2process = text2vocabulary(self.text)

        for i in self.vocabulary2process:
            if i not in self.glossary:
                self.newVocab.append(i)

        self.showNewVocab()
        self.lookup()

        self.AllGlossary = self.glossary + self.newVocab
        self.write2Glossary()

    # ----------------------------------
    def readGlossary(self):
        file2read = self.glossaryFile
        try:
            g = readText(file2read)
            self.glossary = g.split()
        except:
            print(f"Read file failed - {file2read}")
    
        for g in self.glossary:
            print(g)
    # ----------------------------------
    def showNewVocab(self):
        print("new vocabulary:\n")
        for i in range(len(self.newVocab)):
            print(f"\t{i+1}. {self.newVocab[i]}")
    # ----------------------------------
    def lookup(self):
        z = len(self.newVocab)
        self.results += f"\n\n\nThere are {z} new words in this article.\n\n"

        for i in tqdm(range(z)):
            d = Dictionary(self.newVocab[i], self.lang)
            d.wiktionary()
            self.results += f"{i+1}. {d.result}"
    # ----------------------------------
    def write2Glossary(self):
        file2write = self.glossaryFile
        str2write = ""
        for v in self.AllGlossary:
            str2write+=f"{v}\n"
        createFile(file2write, str2write)
