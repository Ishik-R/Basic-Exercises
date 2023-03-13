def solution(nums):
    if nums:
        return sorted(nums)
    else:
        return []

sol1 = solution([1,2,3,10,5])
print(sol1) # should return [1,2,3,5,10]
print(solution(None)) # should return []
 
