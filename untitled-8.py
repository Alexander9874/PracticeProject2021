import sqlite3 
from sqlite3 import Error

PATH = "../words00000.sqlite"

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

connection = create_connection(PATH)


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


  
        

A = list(input().split())


i = 0
while i < (len(A) - 4):
    word_  = A[i] + ' ' + A[i + 1] + ' ' + A[i + 2] + ' ' + A[i + 3] + ' ' + A[i + 4]
    
    select_ = "SELECT * FROM chasti WHERE word = " + "'" + word_ + "'"
    
    words = execute_read_query(connection, select_)
    
    if (words):
        A.pop(i + 1)
        A.pop(i + 1)
        A.pop(i + 1)
        A.pop(i + 1)
        A[i] = word_
    i += 1
   

i = 0
while i < (len(A) - 3):
    word_  = A[i] + ' ' + A[i + 1] + ' ' + A[i + 2] + ' ' + A[i + 3] 
    
    select_ = "SELECT * FROM chasti WHERE word = " + "'" + word_ + "'"
    
    words = execute_read_query(connection, select_)
    
    if (words):
        A.pop(i + 1)
        A.pop(i + 1)
        A.pop(i + 1)
        A[i] = word_
    i += 1


i = 0
while i < (len(A) - 2):
    word_  = A[i] + ' ' + A[i + 1] + ' ' + A[i + 2]
    
    select_ = "SELECT * FROM chasti WHERE word = " +  "'" + word_ + "'"
    
    words = execute_read_query(connection, select_)
    
    if (words):
        A.pop(i + 1)
        A.pop(i + 1)
        A[i] = word_
    i += 1


i = 0
while i < (len(A) - 1):
    word_  = A[i] + ' ' + A[i + 1]
    
    select_ = "SELECT * FROM chasti WHERE word = " + "'" + word_ + "'"
    
    words = execute_read_query(connection, select_)
    
    if (words):
        A.pop(i + 1)
        A[i] = word_
    i += 1




for input_word in A:
    
    input_word = "'" + input_word + "'"
    
    if input_word[1] == 'ю':
        select_word = "SELECT * FROM yu WHERE word = " + input_word
    elif input_word[1] == 'щ':
        select_word = "SELECT * FROM ssh WHERE word = " + input_word
    elif input_word[1] == 'а':
        select_word = "SELECT * FROM a WHERE word = " + input_word
    elif input_word[1] == 'б':
        select_word = "SELECT * FROM b WHERE word = " + input_word
    elif input_word[1] == 'в':
        select_word = "SELECT * FROM v WHERE word = " + input_word
    elif input_word[1] == 'г':
        select_word = "SELECT * FROM g WHERE word = " + input_word
    elif input_word[1] == 'д':
        select_word = "SELECT * FROM d WHERE word = " + input_word
    elif input_word[1] == 'е':
        select_word = "SELECT * FROM e WHERE word = " + input_word
    elif input_word[1] == 'ж':
        select_word = "SELECT * FROM zh WHERE word = " + input_word
    elif input_word[1] == 'з':
        select_word = "SELECT * FROM z WHERE word = " + input_word
    elif input_word[1] == 'и':
        select_word = "SELECT * FROM i WHERE word = " + input_word
    elif input_word[1] == 'й':
        select_word = "SELECT * FROM iy WHERE word = " + input_word
    elif input_word[1] == 'к':
        select_word = "SELECT * FROM k WHERE word = " + input_word
    elif input_word[1] == 'л':
        select_word = "SELECT * FROM l WHERE word = " + input_word
    elif input_word[1] == 'м':
        select_word = "SELECT * FROM m WHERE word = " + input_word
    elif input_word[1] == 'н':
        select_word = "SELECT * FROM n WHERE word = " + input_word
    elif input_word[1] == 'о':
        select_word = "SELECT * FROM o WHERE word = " + input_word
    elif input_word[1] == 'п':
        select_word = "SELECT * FROM p WHERE word = " + input_word
    elif input_word[1] == 'р':
        select_word = "SELECT * FROM r WHERE word = " + input_word
    elif input_word[1] == 'с':
        select_word = "SELECT * FROM s WHERE word = " + input_word
    elif input_word[1] == 'т':
        select_word = "SELECT * FROM t WHERE word = " + input_word
    elif input_word[1] == 'у':
        select_word = "SELECT * FROM u WHERE word = " + input_word
    elif input_word[1] == 'ф':
        select_word = "SELECT * FROM f WHERE word = " + input_word
    elif input_word[1] == 'х':
        select_word = "SELECT * FROM h WHERE word = " + input_word
    elif input_word[1] == 'ц':
        select_word = "SELECT * FROM ce WHERE word = " + input_word
    elif input_word[1] == 'ч':
        select_word = "SELECT * FROM ch WHERE word = " + input_word
    elif input_word[1] == 'ш':
        select_word = "SELECT * FROM sh WHERE word = " + input_word
    elif input_word[1] == 'э':
        select_word = "SELECT * FROM ye WHERE word = " + input_word
    elif input_word[1] == 'я':
        select_word = "SELECT * FROM ya WHERE word = " + input_word

    words = execute_read_query(connection, select_word)
    if (not words):
        print("SLOVA NET V BAZE")
        print()
    else:
        for word in words:
            print(word)
        print()
