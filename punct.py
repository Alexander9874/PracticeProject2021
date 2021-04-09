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


class Item:

    def __init__(self, item, index):
        self.index = 0          # ??
        self.next = []
        self.same = []
        self.prev = []          # ??
        self.conection = []     # ??

        if item:
#           self.IID = item.IID[index]
            self.word = item.word[index]
#           self.code = item.code(index)
#           self.code_parent = item.code_parent(index)
            self.POS = item.POS[index]
            self.type_sub = item.type_sub[index]
            self.type_ssub = item.type_ssub[index]
            self.plural = item.plural[index]
            self.gender = item.gender[index]
            self.case = item.case[index]
            self.comp = item.comp[index]
            self.soul = item.soul[index]
            self.transit = item.transit[index]
            self.perfect = item.perfect[index]
            self.face = item.face[index]
            self.kind = item.kind[index]
            self.time = item.time[index]
            self.inf = item.inf[index]
            self.vozv = item.vozv[index]
            self.nakl = item.nakl[index]
            self.short = item.short[index]


    def Add_Same(self, new):
        if (self.same.count(new) == 0):
            self.same.append(new)

    def Add_Next(self, new):
        if (self.next.count(new) == 0):
            self.next.append(new)



        # CLASS END



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


	# FUNCTIONS TO CONNECT WORDS


def Subjects(array, root):
    for i in array:
        if((i.POS == "сущ" or i.POS == "сущ,мест") and i.case == "им"):
            root.Add_Next(i)
            for j in array:
                if ((j.POS == "сущ" or j.POS == "сущ,мест") and j.case == "им"):
                    i.Add_Same(j)

def Predicates(array, root):
    for i in array:
        if (i.inf == 0):
            for j in array:
                if((i.POS == "сущ" or i.POS == "сущ,мест") and i.case == "им"):
                    if ((i.face == j.face or i.face == "None" or (i.face == "3-е" and j.face == "None")) and i.plural == j.plural and (i.gender == j.gender or i.gender == "None" or j.gender == "None")):
                        j.Add_Next(i)
                    if(i.plural == 1 and j.plural == 0 and len(j.same) != 0):
                        if(i.face == "None"):
                            j.Add_Next
                        else:
                            if(j.face == i.face or (j.POS == "сущ")):
                                if (j.next.count(i) != 0):
                                    continue
                                j.Add_Next(i)
                                for k in j.same:
                                    k.Add_Next(i)
                if (j.POS == "гл" and j.plural == i.plural and j.gender == i.gender and j.time == i.time and j.face == i.face):
                    i.Add_Same(j)

def Infinitives(array, root):
	for i in array:
		if(i.inf == 1):
			for j in array:
				if (j.inf == 1):
					j.Add_Next(i)
				elif (j.inf == 0):
					i.Add_Sane(j);

def Objects(array, root):
	for i in array:
		if(i.case != "им" and (i.POS == "сущ" or i.POS == "числ" or i.POS == "сущ,мест")):
			for j in array:
				if (j.inf == 0 or j.inf == 1):
					j.Add_Next(i)
				elif (i.case == j.case  and (j.POS == "сущ" or j.POS == "числ" or j.POS == "сущ,мест")):
					i.Add_Same(j)

def Atributes(array, root):		#Определение
	for i in array:
		if(i.POS == "прл" or i.POS == "прч"):
			for j in array:
				if ((j.POS == "прл" or j.POS == "прч") and i.case == j.case and (i.gender == j.gender or i.gender == "None" or j.gender == "None") and i.number == j.number and i != j):
					i.Add_Same(j)
			for j in array:
				if (j.POS == "сущ" or j.POS == "числ" or j.POS == "сущ,мест"):
					if (j.case == i.case and j.gender == i.gender and i.number == j.number):
						j.Add_Next(i)
					if (i.plural == 1 and j.number == 0 and i.case == j.case and len(j.same) != 0):
						j.Add_Next(i)

def Conditions(array, root):	#Обстоятельства
    for i in array:
		if (i.POS == "нар" or i.POS == "дееп"):
			for j in array:
				if (j.inf == 1 or j.inf == 0):
					j.Add_Next(i)
				elif ((j.POS == "нар" or j.POS == "дееп") and i != j):
					i.Add_Same(j)

def Prepositions(array, root):	#Предлоги
	for i in range(len(array)):
		if (array[i].POS == "предл"):
			for j in range(i + 1, len(array, 1)):
				if (array[j].POS == "сущ" or array[j].POS == "числ" or array[j].POS == "сущ,мест" and array[j].case != "им"):
					i.Add_Next(j)
					break

def Conjunctions(array, root):	#Союзы
	for i in range(len(array)):
		if (array[i].POS == "союз"):
			for j in range(i + 1, len(array), 1):
				if (len(array[j]) != 0):
					for k in range(i - 1, -1, -1):
						if (array[j].same.count(array[k]) !=0):
							k.Add_Next(i)
							i.Add_Next(j)



	# end of FUNCTIONS TO CONNECT WORDS



def Execute(array, roots, indexes):
    root = Item(None, None)
    items = []
    #for i in range(len(array)):
    #    items.append(Item(array[i], indexes[i]))

    #Subjects(items, root)
    #Predicates(items, root)
    Infinitives(items, root)
    Objects(items, root)
    Atributes(items, root)
    Conditions(items, root)
    Prepositions(items, root)
    Conjunctions(items, root)

    #roots.append(root)
    roots.append(indexes)

def Cycle(array, roots, indexes, num):
    if (num == len(array) - 1):
        for i in range(len(array[num].POS)):
            indexes.append(i)
            Execute(array, roots, indexes.copy())
            del indexes[-1]
    else:
        for i in range(len(array[num].POS)):
            indexes.append(i)
            Cycle(array, roots, indexes.copy(), num + 1)
            del indexes[-1]

def Cycles(array):
    roots = []
    Cycle(array, roots, [], 0)
    return roots

def main():
    array = Get_Words()
    roots = Cycles(array)
    
    #for root in roots:
    #    for item in root.next:
    #        print(item.word)

    print(roots)

if (__name__ == "__main__"):
    main()
