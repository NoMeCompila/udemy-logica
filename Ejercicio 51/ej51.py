def get_odds_even(num: int) -> None:
    list_nums = list(map(lambda x: int(x), list(str(num))))
    odds = list(filter(lambda x:x % 2 != 0, list_nums))
    evens = list(filter(lambda x:x % 2 == 0, list_nums))

    print(f"pares: {evens}")
    print(f"impares: {odds}")

get_odds_even(12345)