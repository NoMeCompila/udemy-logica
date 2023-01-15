def calculator(x,y):
    print(f"{x} + {y} = {x+y}")
    print(f"{x} - {y} = {x-y}")
    print(f"{x} * {y} = {x*y}")
    if y == 0:
        print("no se acepta divisison por 0")
    else:
        print(f"{x} / {y} = {x/y}")

calculator(6,3)
print("------------")
calculator(2,0)