# -*- coding: utf-8 -*-
import json
import sys
import MeCab
import random
import os 
import nltk
import re


def bot_sentence():
	dirname = "mononoke_out"
	eboshi_path = os.path.join(dirname, "エボシ.txt")
	f = open(eboshi_path, "rb")
	data = f.read()
	f.close()

	mt = MeCab.Tagger("-Owakati")
	wordlist = mt.parse(data)

	markov = {}
        w1 = ""
        w2 = ""
        w3 = ""
        w4 = ""

        for word in wordlist:
            if w1 and w2 and w3 and w4:
                if (w1,w2,w3,w4) not in markov:
                    markov[(w1,w2,w3,w4)] = []
                markov[(w1,w2,w3,w4)].append(word)
            w1,w2,w3,w4 = w2,w3,w4,word
        count = 0
        sentence = ""
        w1,w2,w3,w4 = random.choice(markov.keys())

        while count < 100:
            if markov.has_key((w1,w2,w3,w4)) == True:
                tmp = random.choice(markov[(w1,w2,w3,w4)])
                sentence += tmp
                w1,w2,w3,w4 = w2,w3,w4,tmp
                count +=1
            if " " in sentence:
                sentence = sentence.split(" ", 1)[0]

        sentence = re.sub("^.+?\?", "", sentence)
        p = re.compile("[!-/:-@[-`{-~]")
        sus = p.sub("", sentence)
        eboshi_voice = re.sub(re.compile("[!-~]"),"",sus)



        print eboshi_voice

bot_sentence()
