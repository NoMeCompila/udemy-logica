word1 = "Lapicero"
word2 = "Copiarle"

word3 = "Fer"
word4 = "Asd"

def limpiar(p: str):
    return p.lower()

def transform_to_list(p: str):
    lista = sorted(list(p))
    return lista

def are_anagrams(p1, p2):
    if transform_to_list(limpiar(p1)) == transform_to_list(limpiar(p2)):
        print("son anagramas")
    else:
        print("no son anagramas")

are_anagrams(word1, word2)
are_anagrams(word3, word4)


