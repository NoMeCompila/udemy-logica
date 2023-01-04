days = 920

def calculate_days(d):
    years = d // 365
    d = d % 365
    print(f"años: {years}", end=" ")
    months = d // 30
    print(f"meses: {months}", end=" ")
    d = d % 30
    print(f"días: {d}", end=" ")

calculate_days(days)