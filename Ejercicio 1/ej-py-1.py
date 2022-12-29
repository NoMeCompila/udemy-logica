def title(n):
    print(f"tabla del {n}")

def table(n):
    for i in range(11):
        print(f"{n} * {i} = {n*i}")

def main():
    num = int(input("Ingrese un número: "))
    title(num)
    table(num)

main()