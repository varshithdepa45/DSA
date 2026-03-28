class Solution(object):
    def twoSum(self, nums, target):
        d = {}  
        for i, n in enumerate(nums):
            d[n] = i
        for i, n in enumerate(nums):
            diff = target - n
            if diff in d and d[diff] != i:
                return [i, d[diff]]        