num1, num2 = 2002, 1234
def capi(num):
    original = str(num)[::-1]
    reversed = str(num)
    return original == reversed
print(capi(num1))
print(capi(num2))