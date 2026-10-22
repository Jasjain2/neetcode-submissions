class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        groups = {}
        for n in nums:
            groups[n] = groups.get(n,0)+1

        buckets = [[] for _ in range(len(nums)+1)]
        for num, count in groups.items():
            buckets[count].append(num)

        res = []
        for i in range(len(buckets)-1,0,-1):
            for j in buckets[i]:
                res.append(j)
                if len(res) == k:
                    return res
                