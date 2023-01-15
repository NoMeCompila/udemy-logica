arabig_nums = [1000,    900,    500,    400,    100,    90,     50,     40,     10,     9,      5,      4,    1 ]
roman_nums =  ['M',    'CM',   'D',    'CD',   'C',    'XC',   'L',    'XL',   'X',    'IX',   'V', '  IV',  'I']

dic_nums = {1000:'M', 
    900:'CM', 500:'D', 400:'CD', 100:'C', 
    90:'XC', 50:'L', 40:'XL', 10:'X', 
    9:'IX', 5:'V', 4:'IV', 1:'I'}

n = 40
roman = ''

for i in arabig_nums:
    if n >= i:
        roman += roman_nums[i]
        n -= i

print(roman)