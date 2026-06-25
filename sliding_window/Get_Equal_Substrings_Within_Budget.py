class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        count = 0
        left = 0
        max_len = 0 
        for right in range(len(s)) :
            count += abs( ord(s[right]) - ord(t[right]) )
            while left <= right and count > maxCost :
                count -= abs( ord(s[left]) - ord(t[left]) )
                left += 1
            if left <= right :
                max_len = max(max_len , right - left + 1)
        return max_len 