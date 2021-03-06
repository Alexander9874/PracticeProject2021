import nltk
import pymorphy2
from tkinter.filedialog import *
import tkinter as tk
import fileinput

m = pymorphy2.MorphAnalyzer()

class Word:
    def __init__(self, word):
        parse = m.parse(word)[0]

        self.word = word
#        parse = m.parse(word)[0]
        self.POS = str(parse.tag.POS)
        self.animacy = str(parse.tag.animacy)
        self.aspect = str(parse.tag.aspect)
        self.case = str(parse.tag.case)
        self.gender = str(parse.tag.gender)
        self.involvement = str(parse.tag.involvement)
        self.mood = str(parse.tag.mood)
        self.number = str(parse.tag.number)

        if (str(parse.tag.POS) == "NOUN" or str(parse.tag.POS) == "NUMR"):
            self.person = "3per"
        else:
            self.person = str(parse.tag.person)

        self.tense = str(parse.tag.tense)
        self.transitivity = str(parse.tag.transitivity)
        self.voice = str(parse.tag.voice)
        self.next = []
        self.same = []

    def AddNext(self, link):
        self.next.append(link)

    def AddSame(self, buf):
        for i in buf:
            if (i != self):
                self.same.append(i)

#    def PrintSame(self, length):
#        print(self.word + str(length), end = " ")
#        if (len(self.next) == 0):
#            print('\n')
#        
#        for i in self.next:
#
#            i.PrintSame(length + len(self.word))
#        for i in self.same:
#            print(' ' * int(length) + i.word + str(length), end = ' ')
#            if (len(i.next) == 0):
#                print('\n')
#            
#            for j in self.next:
#                j.PrintSame(length + len(j.word))

#    def PrintSame(self, length):
#        print(' ' * length + self.word, end = ' ')
#        if (len(self.next) == 0):
#            print('\n')
#        else:
#            PrintNext(length + len(self.word))
#        
#        for i in self.same:
#            print(' ')

    
    
#    def PrintNext(self, length):
#        print(self.word, end = ' ')
#        if (len(self.next) == 0):
#            print('\n')
#        else:
#            PrintNext(length + 1 + len(self.word))
#        if (len(self.same) != 0):
#            PrintSame(length + 1 + len(self.word))
#
#    def PrintSame(self, length):
#        for i in self.same:
#            print(' ' * length + i.word, end = ' ')
#            if (len(i.next == 0)):
 #               print('\n')
#            else:
#                PrintNext(length + 1 + len(i.word))
#
#    def Print(self, length):
#        print(self.word, end = ' ')
#        length = length + 1 + len(self.word)
#
#        if (len(self.next) == 0):
#            print('\n')
#        else:
#
#            self.next.Print(length + 1 + len(self.word))
#        if (len(self.same) != 0):
#            for i in self.same:
#                print(' ' * length + i.word, end = ' ')
#                if (len(i.next) == 0):
#                    print('\n')
#                else:
#                    i.Print(length + len(i.word) + 1)


            # END CLASS



def PrintMatrix(matrix, length):
    out = ""
    for i in range(length):
        out = out + '\n'
        for j in range(length):
            if (matrix[i][j] != None):
                out = out + '       ' + matrix[i][j].word
            else:
                out = out + '       ' + "...."
        out = out + '\n'
    print(out)

def AddSame(buf):
    for i in buf:
        i.AddSame(buf)

def main():
    text = str(input("> "))
    words = nltk.tokenize.word_tokenize(text)
    
    array = []

    for i in words:
        array.append(Word(i))

    matrix = []
    for i in range(len(array)):
        matrix.append([None]*len(array))

    n = 0
    buf = []
    for i in array:     # сущ,мест,числ в И.П.
        if ((i.POS == "NOUN" or i.POS == "NPRO" or i.POS == "NUMR") and i.case == "nomn"):
            matrix[n][n] = i
            buf.append(i)
            n = n + 1
    AddSame(buf)

    buf = []        
    for i in array:     # гл не в инф.
        if (i.POS == "VERB"):
            matrix[n][n] = i
            m = n - 1
            for j in array:
                if ((j.POS == "NOUN" or j.POS == "NPRO" or j.POS == "NUMR") and j.case == "nomn"):
                    if ((i.person == j.person or i.person == "None") and i.number == j.number and (i.gender == j.gender or i.gender == "None")):
                        matrix[m][n] = j
                        j.AddNext(i)
                        m = m - 1
            n = n + 1

    for i in array:     # гл в инф
        if (i.POS == "INFN"):
            matrix[n][n] = i
            m = n -1
            for j in array:
                if (j.POS == "VERB"):
                    matrix[m][n] = j
                    j.AddNext(i)
                    m = m -1
            n = n + 1

    for i in array:     # сущ,мест,числ не в И.П.
        if ((i.POS == "NOUN" or i.POS == "NPRO" or i.POS == "NUMR") and i.case != "nomn"):
            matrix[n][n] = i
            m = n - 1
            for j in array:
                if (j.POS == "VERB" or j.POS == "INFN"):
                    matrix[m][n] = j
                    j.AddNext(i)
                    m = m - 1
            n = n + 1

    for i in array:     # прил,прич
        if (i.POS == "ADJF" or i.POS == "PRTF"):    #aspect???
            matrix[n][n] = i
            m = n - 1
            for j in array:
                if (j.POS == "NOUN" or j.POS == "NPRO" or j.POS == "NUMR"):
                    if (j.case == i.case and j.gender == i.gender and j.number == i.number):
                        matrix[m][n] = j
                        j.AddNext(i)
                        m = m - 1
            n = n + 1

    for i in array:     # нареч,дееприч
        if (i.POS == "GRND" or i.POS == "ADVB"):
            matrix[n][n] = i
            m = n - 1
            for j in array:
                if (j.POS == "VERB" or j.POS == "INFN"):
                    matrix[m][n] = j
                    j.AddNext(i)
                    m = m - 1
            n = n + 1

    PrintMatrix(matrix, len(array))

    print('\n')
#    matrix[0][0].Print(0)

if (__name__ == "__main__"):
    main()
