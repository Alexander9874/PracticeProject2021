import nltk
import pymorphy2
from tkinter.filedialog import *
import tkinter as tk
import fileinput

m = pymorphy2.MorphAnalyzer()

def Analise():
    text = str(input("> "))
    s = " "
    for i in text:
        if i != "." and i != ")" and i != "(":
            s = s + i
    words = nltk.tokenize.word_tokenize(s)
    y = [w for w in words if len(w) > 0]
    fdist = nltk.FreqDist(y)

    vocab = list(fdist.keys())
    for v in vocab:
        try:
            parse = m.parse(v)[0]
            print("\nparse = m.parse:")
            print(parse)
            
            print("\n  0.  parse.word: " + str(parse.word))
            print("1. parse.tag.POS: " + str(parse.tag.POS))
            print("2. parse.tag.animacy: " + str(parse.tag.animacy))
            print("3. parse.tag.aspect: " + str(parse.tag.aspect))
            print("4. parse.tag.case: " + str(parse.tag.case))
            print("5. parse.tsg.gender: " + str(parse.tag.gender))
            print("6. parse.tag.involvement: " + str(parse.tag.involvement))
            print("7. parse.tag.mood: " + str(parse.tag.mood))
            print("8. parse.tag.number: " + str(parse.tag.number))
            print("9. parse.tag.person: " + str(parse.tag.person))
            print("10. parse.tag.tense: " + str(parse.tag.tense))
            print("11. parse.tag.trasistivity: " + str(parse.tag.transitivity))
            print("12. parse.tag.voice: " + str(parse.tag.voice))
#            print(parse.inflect({'plur', 'nomn'}).word)
            print(parse.tag)
        except:
            print("\nexcept!")
            pass
Analise()
