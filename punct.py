import dictionary

class Word:

    def __init__(self):

#       self.IID = []
        self.word = []
#       self.code = []
#       self.code_parent = []
        self.POS = []
        self.type_sub = []
        self.type_ssub = []
        self.plural = []
        self.gender = []
        self.case = []
        self.comp = []
        self.soul = []
        self.transit = []
        self.perfect = []
        self.face = []
        self.kind = []
        self.time = []
        self.inf =  []
        self.vozv = []
        self.nakl = []
        self.short = []

    def Fill_Word(self, info):
    
#       self.IID.append(info[0])
        self.word.append(info[1])
#       self.code.append(info[2])
#       self.code_parent.append(info[3])
        self.POS.append(info[4])
        self.type_sub.append(info[5])
        self.type_ssub.append(info[6])
        self.plural.append(info[7])
        self.gender.append(info[8])
        self.case.append(info[9])
        self.comp.append(info[10])
        self.soul.append(info[11])
        self.transit.append(info[12])
        self.perfect.append(info[13])
        self.face.append(info[14])
        self.kind.append(info[15])
        self.time.append(info[16])
        self.inf.append(info[17])
        self.vozv.append(info[18])
        self.nakl.append(info[19])
        self.short.append(info[20])


def Get_Words():
    text = str(input("Enter your sentence.\n>> "))
    script = dictionary.Find(text)
    j = -1
    array = []
    for i in range(len(script)):
        if (i == 0 or script[i][1] != script[i - 1][1]):
            array.append(Word())
            j = j + 1
        array[j].Fill_Word(script[i])
    return array
def main():
    array = Get_Words()

if (__name__ == "__main__"):
    main()
