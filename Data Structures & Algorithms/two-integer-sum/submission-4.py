class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        group = {}
        for i, j in enumerate(nums):
            if target - j in group:
                return [group[target - j], i]
            group[j] = i