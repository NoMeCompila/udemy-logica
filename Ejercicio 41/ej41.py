def triangle(n:int):
    for i in range(1, n):
        for k in range(1, n-i):
            print(" ", end="")
        for j in range(1, (2*i)):
            print("*", end="")
        print("")

triangle(4)