import re

def is_valid_email(mail: str):
    patron_valido = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    return bool(re.search(patron_valido, mail))

print(is_valid_email("cabafer1@gmail.com"))
print(is_valid_email("cabafer1@gmailcom"))


