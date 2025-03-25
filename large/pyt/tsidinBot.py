from joef2t.tgBot.tgBot import tgBot

from joef2t.dictionary.Lookup import Lookup
import joef2t.setttings.config as cfg
from joef2t.setttings.Languages import Languages as langue

from joef2t.utils.html import retainText
from joef2t.utils.telegra import write2Telegraph

import asyncio
import telegram_send as ts
from telegram.ext import CommandHandler

from datetime import datetime
import os

class TsiDinBot(tgBot):
    def __init__(self, token, startWord, helpWord):
        super().__init__(token, startWord, helpWord)
        self.resUrl = ""
    # ------------------------------------
    def wiktionary(self, update, context):
        convert_parameter = ' '.join(context.args)
        now = datetime.now()

        res = ""
        if convert_parameter!=None:
            lookup = Lookup(cfg.glossaryEng, langue.eng, retainText(convert_parameter) )
            res += lookup.results

        self.resUrl = asyncio.run(
             write2Telegraph(
                title=f"vocabulary-{now}",
                content = res,
                author = "",
            )
        )
        update.message.reply_text(text=self.resUrl)
    # ------------------------------------
    def advancedCommands(self):
        adv =[
            ["wk", self.wiktionary],
        ]
        for a in adv:
            self.pairs.append(a)
# ---------------------------------

token = os.environ["TsiDin_Bot_Token"]
startWord = """I'm ready to work.\nYou can use `/help` command to learn how to use me."""
helpWord = "I'm a dictionary bot.\n\n\tIf you have any questions, please contact @hk\\_tobeno1."

# -------------------------------------
def main():
    TsiDinBot(token, startWord, helpWord).run()

# --------------------------------------
if __name__ == '__main__':
    # --------------
    main()
    # --------------
