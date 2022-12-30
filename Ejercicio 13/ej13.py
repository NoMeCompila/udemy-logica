# mirando
arr = [1,2,3,4]
n = 2
sub_arr = []

for i in arr:
    l = []
    if(len(l) == n):
        l.clear()
    else:
        l.append(i)
        sub_arr.append(l)
    

print(sub_arr)