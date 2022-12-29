x = 1
y = 10

def do_list(init, end):
    return [x for x in range(init,end+1)]

def get_odds(l):
    return len(list(filter(lambda x: x%2 != 0, l)))

def eje7(x, y):
    print(get_odds(do_list(x, y)))