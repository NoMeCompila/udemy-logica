sentence = "fernando juan antonio caballero"

def capitalize_all(w : str):
    l1 = w.split(' ')
    l2 = []
    for i in l1:
        l2.append(i.capitalize())
    return " ".join(l2)

print(capitalize_all(sentence))