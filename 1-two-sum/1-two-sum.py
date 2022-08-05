class Solution:
    def twoSum(self, nums, target) :
        pairs = [target - num for num in nums]
        for i, pair in enumerate(pairs):
            if pair in nums and i != nums.index(pair):
                return [i, nums.index(pair)]