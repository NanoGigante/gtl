import funz
import parse as parse_data

def guess_the_language():
    
    input_dict = get_input_dict()

    lang_data = parse_data.parse(parse_data.readfile("dataset"))

    #dizionario con come key ogni lingua e come val 0
    dists = {x : 0 for x in lang_data}

    #per ogni lingua nel dataset
    for langname,lang in lang_data.items():
        #per ogni lettera e la sua frequenza in una lingua
        for letter,letterf in lang.items():
            #aggiungi a dists la differenza tra le 2 frequenze
            if letter in input_dict:
                dists[langname] += abs(input_dict[letter] - letterf)
            #se la lettera non è in inputdict vuol dire che è 0
            else:
                dists[langname] += letterf


    result = list(dists.keys())[0]

    #scorre tutte le distanze e trova la minore
    for lang,freq in dists.items():
        #print( lang + " : " + str(freq))
        if freq < dists[result]:
            result = lang

    return result

def get_input_dict():
    input_file= input("che file si vuole leggere [default: input.txt]: ")

    input_txt = funz.readfile(input_file if input_file is not "" else "input.txt")
    input_txt = funz.cleanString(input_txt,keepAccents=True)
    input_dict= funz.lettersAbsFreq(input_txt)
    lettercnt = funz.lettersCount(input_txt)

    if lettercnt is 0: #se il file è vuoto o inesistente termina
        print("file insesistente")
        exit()

    #converti da frequenza assoluta a 0-100
    for i in input_dict: 
        input_dict[i] /= lettercnt / 100
    
    return input_dict

#MAIN
print(guess_the_language())