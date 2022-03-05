import parse

#-----------------------------#
#legge dal file, ritorna un unica stringa invece che una lista

def readfile(filename):
    try:
        file = open(filename,"r",encoding="utf-8")
        lines = file.readlines()
        file.close()
        tostr=''
        for i in lines:
            tostr+=i
        return tostr
    except:
        return ''

#-----------------------------#
# rimpiazzi contiene tutti i caratteri proibiti e i loro rimpiazzi
# il for itera in ogni carattere della stringa 
# se un char è proibito (contenuto in una key) viene rimpiazziato, altrimenti viene lasciato invariato

def cleanString(strin,keepAccents=False): #strin = string input
    
    rimpiazzi = {
        "[$&+:;=?@#|'<>^*()%!-].,\"" : "",
        "áâäàã" : "a" , "ÁÂÄÀÃĀ" : "A",
        "éêëè" : "e" , "ÉÊËÈ" : "E",
        "íîïì" : "i" , "ÍÎÏÌ" : "I", 
        "óôöòõ" : "o" , "ÕÒÖÔÓ" : "O", 
        "úûüù" : "u" , "ÙÜÛÚ" : "U" 
    }
    
    if keepAccents:
        rimpiazzi = { list(rimpiazzi.keys())[0] : "" }

    newstring=''    
    
    for c in strin:
        trovato=False
        for i,j in rimpiazzi.items():
            if c in i:
                newstring += j
                trovato=True
        if not trovato:
            newstring+=c

    return newstring

#-----------------------------#
# conta i new line per ottenere il numero di righe

def rowsCount(strin):
    return strin.count("\n") + 1

#-----------------------------#

def charCount(string,char=""):
    if char == "":
        return len(string)
    
    cnt=0
    for i in string:
        if i == char:
            cnt+=1
    return cnt

#-----------------------------#
# conta le lettere
# da per scontato che la string contenga solo lettere, spazi, newline e numeri

def lettersCount(strin : str):
    num = len(strin)
    num -= strin.count("\n")
    num -= strin.count(" ")

    for i in range(10):
        num -= strin.count(str(i))
        
    return num

#-----------------------------#
# conta le parole usado string.split
# il primo for serve per eliminare elementi nulli (generati a causa di doppi spazi)

def wordCount(strin,word=""):
    strin2=strin.replace("\n"," ")
    parole=strin2.split(" ")
    
    for i in parole: 
        if len(i) < 1:
            parole.remove(i)
    
    if word == "":
        return len(parole)

    cnt=0

    for i in parole:
        if i == word:
            cnt+=1
    return cnt

#-----------------------------#

def charAbsFreq(strin):
    cfreq={}

    for i in strin:
        if not i in cfreq:
            cfreq[i] = 1
        else:
            cfreq[i] += 1
    
    return cfreq

#-----------------------------#
# conta la frequenza delle lettere
# prima di contare popola il dizionario con ogni lettera in modo che compaiano nel dict 
# anche lettere che nella stringa di input non sono presenti

def lettersAbsFreq(strin):
    lettere = "abcdefghijklmnopqrstuwxyz"
    lfreq = {}

    for i in lettere:
        lfreq[i] = 0
    
    for i in strin.lower():
        if i in lettere:
            lfreq[i] += 1
    
    return lfreq

#-----------------------------#
# test

def save(strin):
    with open("out.txt",'w') as outfile:
        outfile.write(strin)

#-----------------------------#

def reportOut(strin,outfile):
    try:
        with open(outfile,"w") as outfile:
            outfile.write(
                "total number of rows: " + str(rowsCount(strin)) +
                "\ntotal number of chars: " + str(charCount(strin)) + 
                "\ntotal number of letters: " + str(lettersCount(strin)) +
                "\ntotal number of words: " + str(wordCount(strin)) + 
                "\nabsolute frequency of chars: " + str(charAbsFreq(strin)) +
                "\nabsolute frequency of letters: " + str(lettersAbsFreq(strin))
            )
    except Exception as e:
        print("invalid file name")
        #print(e)
