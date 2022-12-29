def horizon(n):
    print("* "*n)

#horizon(6)

def vertic(n):
    for i, numero in enumerate(range(n)):
    # Si es la última iteración, imprimimos un mensaje
        if(i == 0):
            print("*", end=" ")
        elif i == len(list(enumerate(range(n)))) - 1:
            print("*")
        else:
            print(" ", end=" ")



def square(n):
    horizon(n)
    for i in range(n-2):
        vertic(n)
    horizon(n)

square(6)