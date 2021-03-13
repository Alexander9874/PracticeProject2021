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

    def AddSame(self, buf):
        for i in buf:
            if (i != self):
                self.same.append(i)



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


    for i in array:     # гл не в инф.
        if (i.POS == "VERB"):
            matrix[n][n] = i
            m = n - 1
            for j in array:
                if ((j.POS == "NOUN" or j.POS == "NPRO" or j.POS == "NUMR") and j.case == "nomn"):
                    if ((i.person == j.person or i.person == "None") and i.number == j.number and (i.gender == j.gender or i.gender == "None" or j.gender == "None")):
                        matrix[m][n] = j
                        j.next.append(i)
                        m = m - 1
                    if (i.number == "plur" and j.number != "plur" and len(j.same) != 0):
                        if(i.person == "None"):
                            matrix[m][n] = j
                            j.next.append(i)
                            m = m -1
                        else:
                            if (j.person == i.person):
                                if (j.next.count(i) != 0):
                                    continue
                                matrix[m][n] = j
                                j.next.append(i)
                                m = m - 1
                                for k in j.same:
                                    matrix[m][n] = k
                                    k.next.append(i)
                                    m = m - 1
                if(j.POS == "VERB" and j.aspect == i.aspect and j.mood == i.mood and j.number == i.number and i.person == j.person and i.tense == j.tense and i.gender == j.gender and i != j):
                    i.same.append(j)
            n = n + 1


    for i in array:     # гл в инф
        if (i.POS == "INFN"):
            matrix[n][n] = i
            m = n -1
            for j in array:
                if (j.POS == "VERB"):
                    matrix[m][n] = j
                    j.next.append(i)
                    m = m -1
                elif (j.POS == "INFN" and j != i):
                    i.same.append(j)
            n = n + 1


    for i in array:     # сущ,мест,числ не в И.П.
        if ((i.POS == "NOUN" or i.POS == "NPRO" or i.POS == "NUMR") and i.case != "nomn"):
            matrix[n][n] = i
            m = n - 1
            for j in array:
                if (j.POS == "VERB" or j.POS == "INFN"):
                    matrix[m][n] = j
                    j.next.append(i)
                    m = m - 1
                elif ((j.POS == "NOUN" or j.POS == "NPRO" or j.POS == "NUMR") and i.case == j.case and i != j):
                    i.same.append(j)
            n = n + 1


    for i in array:     # прил,прич
        if (i.POS == "ADJF" or i.POS == "PRTF"):    #aspect???
            matrix[n][n] = i
            m = n - 1
            for j in array:
                if (j.POS == "NOUN" or j.POS == "NPRO" or j.POS == "NUMR"):
                    if (j.case == i.case and j.gender == i.gender and j.number == i.number):
                        matrix[m][n] = j
                        j.next.append(i)
                        m = m - 1
                    if (i.number == "plur" and j.number == "sing" and j.case == i.case and len(j.same) != 0):
                        matrix[m][n] = j
                        j.next.append(i)
                        m = m - 1
                elif ((j.POS == "ADJF" or j.POS == "PRTF") and i.case == j.case and i.gender == j.gender and i.number == j.number and i != j):
                    i.same.append(j)

            n = n + 1


    for i in array:     # нареч,дееприч
        if (i.POS == "GRND" or i.POS == "ADVB"):
            matrix[n][n] = i
            m = n - 1
            for j in array:
                if (j.POS == "VERB" or j.POS == "INFN"):
                    matrix[m][n] = j
                    j.next.append(i)
                    m = m - 1
                elif ((j.POS == "GRND" or j.POS == "ADVB") and i != j):
                    i.same.append(j)
            n = n + 1


    for i in range(len(array)):     #союзы
        if (array[i].POS == "CONJ"):
            matrix[n][n] = array[i]
            m = n - 1
            for j in range(i + 1, len(array), 1):
                if (len(array[j].same) != 0):                           # MAY WORK WRONG
                    for k in range(i - 1, -1, -1):
                        if (array[j].same.count(array[k]) != 0):
                            matrix[m][n] = array[j]
                            m = m - 1
                            matrix[m][n] = array[k]
                            m = m - 1



    
    PrintMatrix(matrix, len(array))

    print('\n')

    for i in array:
        print('\n' + i.word)
        print("Same: ", end = ' ')
        for j in i.same:
            print(j.word, end = ' ')
        print('\n' + "Next: ", end = ' ')
        for j in i.next:
            print(j.word, end = ' ')
        print('\n')


    output = ''
    for i in range(len(array)):
        if (array[i].POS == "CONJ"):
            if (array[i].word == "а" or array[i].word == "но" or array[i].word == 'однако' or array[i].word == 'зато'):
                output = output + ','
            output = output + array[i].word
            output = output + ' '
            continue         
        output = output + array[i].word
        check = 1
        if (len(array[i].same) != 0):
            for j in range(i + 1, len(array), 1):
                if (array[i].same.count(array[j]) != 0 and check == 1):
                    check = 0
                    output = output + ","
                    for k in range(i + 1, j, 1):
                        if(array[k].POS == "CONJ"):
                            output = output[0:-1]
                            output = output
                            break
        output = output + ' '
    print(output)


if (__name__ == "__main__"):
    main()
