from joef2t.dictionary.Lookup import Lookup
from joef2t.setttings import config as cfg

from joef2t.setttings.Languages import Languages as lang

from joef2t.utils.html import removeAttrExceptHrefSrc, retainText

import re

# s = ['ARTA Travel Group', 'Arta | آرتا', 'ARTAS™ Practice Development', 'ArtBinder', 'Arte Arac Takip App', 'アート建築', 'Arte Brasil Bar & Grill', 'ArtPod Stage', 'Artpollo扫码', 'Artpollo阿波罗-价值最优的艺术品投资电商', '아트홀']


# result = [i for i in s if not re.findall("[^\u0000-\u05C0\u2100-\u214F]+",i)]

# print (result)


t = "Artpollo阿波罗-价值最优的艺术品投资电商 hahahaha"
# result = if not re.findall("[^\u0000-\u05C0\u2100-\u214F]+", t)
linee = re.sub("[\u4e00-\u9fff]", "", t)
print(linee)
# ['ARTA Travel Group', 'ARTAS™ Practice Development', 'ArtBinder', 'Arte Arac Takip App', 'Arte Brasil Bar & Grill', 'ArtPod Stage']



# engText = """
# <p><span style="font-weight: 400;">A Chinese social media user who gave only the pseudonym Hu said posts and photos linked to the flyover protest were being blocked very fast on WeChat.</span></p>
# <p><span style="font-weight: 400;">"I didn't know the entire story of what happened ... but I couldn't enquire too closely in the WeChat group, and nobody dared to explain it to me in detail," Hu told RFA.</span></p>
# <p><span style="font-weight: 400;">"The moment anyone mentions the specifics, the entire group and account get blocked by WeChat. We will find out about it through external channels," Hu said, in a reference to circumventing the Great Firewall to read uncensored news on overseas sites.</span></p>
# <p><span style="font-weight: 400;">Hu said Peng's banner had expressed what many in China are thinking, but have no way to express under widespread censorship and intimidation.</span></p>
# <p><span style="font-weight: 400;">Another social media user who gave the pseudonym Tang said people refer to the incident by saying simply: "I saw it."</span></p>
# <p><span style="font-weight: 400;">Tang said he didn't think the protest was carried out by a lone activist.</span></p>
# """


# engText = retainText(engText)
# print(engText)
