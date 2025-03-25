import string
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import sent_tokenize, word_tokenize
import nltk

from nltk.corpus import wordnet as wn
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import word_tokenize, pos_tag
from collections import defaultdict
import re

str2delete = [
    "“", "’s", "”",
]

# ------------------------
# nltk.download('punkt')
# nltk.download('wordnet')
# nltk.download('omw-1.4')
# nltk.download('averaged_perceptron_tagger')
# ------------------------

tag_map = defaultdict(lambda : wn.NOUN)
tag_map['J'] = wn.ADJ
tag_map['V'] = wn.VERB
tag_map['R'] = wn.ADV

# ----------------------------------
def text2vocabulary(text2process):
    textStr = "".join([i for i in text2process if not i.isdigit()])
    textStr = textStr.replace("-", " ")
    for s in str2delete:
        textStr = textStr.replace(s, " ")

    textStr = textStr.translate(str.maketrans('', '', string.punctuation))

    tokens = word_tokenize(textStr)
    print( len(tokens) )
    tokens = [*set(tokens)]
    print( len(tokens) )

    finalRes = []
    lemma_function = WordNetLemmatizer()
    for token, tag in pos_tag(tokens):
        if( len(token) > 3):
            lemma = lemma_function.lemmatize(token, tag_map[tag[0]])
            finalRes.append(lemma)
        
    return [*set(finalRes)]

# ----------------------------------

def removeCJK(str2process):
    linee = re.sub("[\u4e00-\u9fff]", "", str2process)
    return linee
# lk = Lookup(cfg.glossaryEng, "eng")

# vcb = text2vocabulary(engText)
# for v in vcb:
#     print(v)
# print(engText)





# print(engText)


# sentence= engText # "Hello Guru99, You have to build a very good site and I love visiting your site."
# words = word_tokenize(sentence)
# ps = PorterStemmer()
# for w in words:
# 	rootWord=ps.stem(w)
# 	print(rootWord)
"""

text = engText
tokenization = nltk.word_tokenize(text)
print(tokenization)


# wordnet_lemmatizer = WordNetLemmatizer()
# for w in tokenization:
# 	print("Lemma for {} is {}".format(w, wordnet_lemmatizer.lemmatize(w)))



"""
#


# print("-"*20)
# another_word = parser.fetch('test', 'french')
# pprint.pprint(another_word)

# parser.set_default_language('french')
# parser.exclude_part_of_speech('noun')
# parser.include_relation('alternative forms')






# e_words= ["wait", "waiting", "waited", "waits"]
# ps =PorterStemmer()
# for w in e_words:
#     rootWord=ps.stem(w)
#     print(rootWord)