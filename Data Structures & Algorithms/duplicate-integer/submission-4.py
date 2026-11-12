class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        group = set()
        for i in nums:
            if i in group:
                return True
            group.add(i)

        return False