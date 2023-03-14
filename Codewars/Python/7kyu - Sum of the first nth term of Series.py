'''
7 kyu - Sum of the first nth term of Series
https://www.codewars.com/kata/555eded1ad94b00403000071/train/python
Python

Your task is to write a function which returns the sum of following series upto nth term(parameter).
# Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 +...

* You need to round the answer to 2 decimal places and return it as String.
* If the given value is 0 then it should return 0.00
* You will only be given Natural Numbers as arguments.
'''

def series_sum(n):
    total = 0
    for i in range(0, n):
        total += 1/(1+(i*3))
    return "{:.2f}".format(round(total,2))

print(series_sum(0))
print(series_sum(1))
print(series_sum(2))
print(series_sum(3))
print(series_sum(4))
print(series_sum(5))
