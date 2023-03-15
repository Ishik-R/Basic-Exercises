'''
7 kyu - Money, Money, Money
https://www.codewars.com/kata/563f037412e5ada593000114/train/python
Python

Mr. Scrooge has a sum of money 'P' that he wants to invest.

Before he does, he wants to know how many years 'Y' this sum 'P' has to be kept in the bank in order for it to amount to a desired sum of money 'D'.

The sum is kept for 'Y' years in the bank where interest 'I' is paid yearly.

After paying taxes 'T' for the year the new sum is re-invested.

Note to Tax: not the invested principal is taxed, but only the year's accrued interest.

Your task is to complete the method provided and return the number of years 'Y' as a whole in order for Mr. Scrooge to get the desired sum.
'''

def calculate_years(principal, interest, tax, desired):
    years = 0
    while principal <= desired:
        principal += (principal*interest) - (principal*interest*tax)
        years += 1
    return years

print(calculate_years(1000, 0.05, 0.18, 1100))
print(calculate_years(1000, 0.01625, 0.18, 1000))