#coding:utf-8
import re
import commands
from nltk.corpus import wordnet
import csv
import os

pattern = r"[A-Z]"
addition_verb = [
    "new",
    "setup",
    "cleanup",
    "to",
    "as"
]
short_verb = {
    "analyse": "analyze",
    "attr": "attribute",
    "attrib": "attribute",
    "calc": "calculate",
    "eval": "evaluate",
    "exec": "execute",
    "gen": "generate",
    "init": "initialize",
    "initialise": "initialize",
    "sync": "synchronize"
}


class VerbPicker:
    def pick(self, method):
        if (method == "main" or method == "<init>" or method == "<clinit>"):
            return ""
        if ("$" in method) or ("_" in method): # $の入ってるものは除く
            return ""

        word = str()
        match = re.finditer(pattern, method) # パターンを取り出す
        exist = False

        for m in match:
            s = m.start()
            if s != 0:
                exist = True
                word = method[0:s]
                break

        if not exist: # 大文字が入っていない場合はそのまま
            word = method

        word = word.lower()

        if word in addition_verb:
            return word

        if word in short_verb:
            return short_verb[word]

        # 動詞の確認
        wn = wordnet.synsets(word, pos="v")
        if len(wn) < 1:
            return ""


        return wordnet.morphy(word)
