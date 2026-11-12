class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        group = {}
        for n in nums:
            group[n] = group.get(n, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in group.items():
            buckets[count].append(num)

        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res