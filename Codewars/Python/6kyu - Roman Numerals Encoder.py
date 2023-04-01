'''
6 kyu - Roman Numerals Encoder
https://www.codewars.com/kata/51b62bf6a9c58071c600001b/train/python
Python

Create a function taking a positive integer between 1 and 3999 (both included) as its parameter and returning a string containing the Roman Numeral representation of that integer.

Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero.

* 1990 in Roman numerals  is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 
* 2008 is written as 2000 = MM; 8 = VIII; or MMVIII.
* 1666 uses each Roman symbol in descending order: MDCLXVI.

Help:
Symbol    Value
I          1
V          5
X          10
L          50
C          100
D          500
M          1,000
Remember that there can't be more than 3 identical symbols in a row.

More about roman numerals - http://en.wikipedia.org/wiki/Roman_numerals
'''

def solution(n):
    roman_numerals = {
        '1':'I',
        '4':'IV',
        '5':'V',
        '9':'IX',
        '10':'X',
        '40':'XL',
        '50':'L',
        '90':'XC',
        '100':'C',
        '400':'CD',
        '500': 'D',
        '900':'CM',
        '1000': 'M',
    }
    key_list = sorted([int(k) for k in roman_numerals.keys()], reverse=True)
    roman_number = ''
    for i, value in enumerate(key_list):
        while(n // value > 0):
            roman_number += roman_numerals.get(str(key_list[i]), '?')
            n -= key_list[i]
    return roman_number

print('1 - ' + solution(1))
print('9 - '+ solution(9))
print('41 - ' + solution(41))
print('45 - ' + solution(45))
print('1990 - ' + solution(1990))
print('1666 - ' + solution(1666))