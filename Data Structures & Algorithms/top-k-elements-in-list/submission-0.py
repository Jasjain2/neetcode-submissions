class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        groups = {}
        for n in nums:
            groups[n] = groups.get(n,0)+1
        
        output = sorted(groups, key=groups.get, reverse=True)[:k]

        return output

