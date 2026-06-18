class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = { "a": 0, "b": 0 , "c": 0 }
        left = 0
        chars = 0
        for right in range(len(s)) :
            count[s[right]] += 1
            while left <= right and all(v >= 1 for v in count.values()) :
                chars += len(s) - right
                count[s[left]] -= 1
                left += 1

        return chars

