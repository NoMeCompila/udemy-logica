phrase1 = "Hola Como estas"
phrase2 = "MUCHO MAS CON MAYuscula"

def lower_or_uper(st: str):
    m = 0
    M = 0

    for i in st:
        if i.islower():
            m += 1
        else:
            M += 1

    if m > M:
        new_p = st.lower()
    else:
        new_p = st.upper()
    return new_p

print(lower_or_uper(phrase1))    
print(lower_or_uper(phrase2))