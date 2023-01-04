l1 = [1,2,3,4,5]
l2 = [1,2,4,5]

n = 5


def is_permutation(lis, num):
    l3 = [i for i in range(1, num+1)]
    if l3 == lis:
        return True
    else:
        return False

print(is_permutation(l1, n))
print(is_permutation(l2, n))