word = 'hola'

def get_substring(w:str):
    for i in range(len(w)):
        for j in range(len(w)):
            print(w[i]+w[j])

get_substring(word)