'''
7 kyu - Beginner Series #3 Sum of Numbers
https://www.codewars.com/kata/55f2b110f61eb01779000053/train/python
Python

Given two integers a and b, which can be positive or negative, find the sum of all the integers between and including them and return it.
If the two numbers are equal return a or b.

Note: a and b are not ordered!
'''

def get_sum(a,b):
    start = min(a,b)
    finish = max(a,b)
    return sum([i for i in range(start, finish+1)])

print(get_sum(1,2))
print(get_sum(-1,2))
print(get_sum(1,1))
print(get_sum(-3,0))