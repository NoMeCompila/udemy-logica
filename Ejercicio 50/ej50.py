def get_loops(num: int) -> int:
    b_nums = [0, 6, 8, 9]

    listed_num = list(map(lambda x:int(x), list(str(num))))
    loops = 0

    for i in listed_num:
        if i in b_nums:
            loops += 1
    
    return loops


print(get_loops(19980445))