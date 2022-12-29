parragraph = "soy la palabra en una frase llena de PALABRA"
word = "palabra"

def count_words(p,w):
    return p.lower().count(w)

print(count_words(parragraph, word))