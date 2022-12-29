# Palindromos
def is_palindrome(w):
    if(w[::-1] == w):
        print("es un palíndromo")
    else:
        print("no es un palíndromo")

def exe():
    word = input("Ingrese una palabra: ")
    is_palindrome(word)

exe()