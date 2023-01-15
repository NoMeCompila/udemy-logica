import re

def is_vocal(c: str):
    return bool(re.match(r'[áéíóúaeiouAEIOUÁÉÍÓÚ]', c))

def without_spaces(text:str):
    return "".join(list(filter(lambda i: not i.isspace(), list(text))))

def count_type_of_letters(l1: str):
    voc = []
    con = []
    texto_junto = without_spaces(l1)

    for i in texto_junto:
        if(is_vocal(i)):
            voc.append(i)
        else:
            con.append(i)

    print(f"cantidad de vocales: {len(voc)}")
    print(f"cantidad de consonantes: {len(con)}")

count_type_of_letters("Fernándo Caballero")