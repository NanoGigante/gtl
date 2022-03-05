def readfile(filename):
    try:
        with open(filename,'r') as infile:
            return infile.readlines()
    except Exception as e:
        print("invalid file name")
        print(e)

# test
def save(strin,out='out2.txt',mode='w'):
    with open(out,mode) as outfile:
        outfile.write(strin)

def parse(rawlist):
    firstline = rawlist[0]
    langs = {}
    letters=[x for x in 'abcdefghijklmnopqrstuvwxyz']

    for i in firstline.split(","):
        langs[i.strip()] = {}

    del rawlist[0]

    for line, letter in zip(rawlist, letters):
        vals = line.split(",")
        #inserisce una sola lettere per tutte lingue
        # key , value = float val
        for key, value in zip(langs.keys(),vals[1:]):
            langs[key][letter] = float(value)

    return langs

'''
struttura dizionario
{
    "lang1" : { 'a' : X.XX , 'b' : X.XX , ...},
    "lang1" : { 'a' : X.XX , 'b' : X.XX , ...},
    "lang1" : { 'a' : X.XX , 'b' : X.XX , ...},
    ....
}

struttura dataset

langname1,langname2,langname3,...
a,freq1,freq2,freq3,...
b,freq1,freq2,freq3,...
c,freq1,freq2,freq3,...
...

'''

def betterparse(rawlist):
    firstline = rawlist[0]
    langs = {}
    for i in firstline.split(","):
        langs[i.strip()] = {}

    del rawlist[0]

    for line in rawlist:
        vals = line.split(",")
        for key, value in zip(langs.keys(),vals[1:]):
            langs[key][vals[0]] = float(value)

    return langs

def empty_dict(rawlist):
    del rawlist[0]

    letters = {}
    for s in rawlist:
        letters[s[0]] = 0

    return letters
