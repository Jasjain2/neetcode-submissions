class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        group = {}
        for ch in s:
            group[ch] = group.get(ch, 0) + 1
        for ch in t:
            group[ch] = group.get(ch, 0) - 1

        for count in group.values():
            if count != 0:
                return False
        return True