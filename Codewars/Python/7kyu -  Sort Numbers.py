'''
7 kyu - Sort Numbers
https://www.codewars.com/kata/5174a4c0f2769dd8b1000003
Python

Finish the solution so that it sorts the passed in array of numbers.

If the function passes in an empty array or null/nil value then it should return an empty array.
'''

def solution(nums):
    if nums:
        return sorted(nums)
    else:
        return []

sol1 = solution([1,2,3,10,5])

print(sol1) # should return [1,2,3,5,10]
print(solution(None)) # should return []
