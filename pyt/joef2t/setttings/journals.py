from joef2t.setttings import config
from joef2t.setttings.Languages import Languages as lang
from joef2t.setttings.Languages import Translated as tsl

elsevier = [
    "journal-of-structural-geology",
    "tectonophysics",
    "earth-and-planetary-science-letters",
    "tribology-international",
    "earth-science-reviews",
    "journal-of-asian-earth-sciences",
    "theoretical-and-applied-fracture-mechanics",
    "computers-and-geosciences",
]
# ------------------------------------------------
springer = [
    10346,
]
# ------------------------------------------------
elsevierLinkHead = "https://rsshub.app/elsevier/"
elsevierLinkEnd  = "/latest"
elsevierRSS = list(map(lambda x: [f"{elsevierLinkHead}{x}{elsevierLinkEnd}", x, config.journals, lang.eng, tsl.y], elsevier) )
# elsevierRSS = list(map(lambda x: [f"{elsevierLinkHead}{x}{elsevierLinkEnd}",x, "test"], elsevier) )

# ------------------------------------------------
# springerLinkHead = "https://rsshub.app/springer/journal/"
# springerRSS = list(map(lambda x: f"{springerLinkHead}{str(x)}" , springer))


journalRSS = elsevierRSS # + springerRSS
# ------------------------------------------------
def main():    
    [print(rl) for rl in journalRSS]

    
# ------------------------------------------------

if __name__ == '__main__':
    main()
