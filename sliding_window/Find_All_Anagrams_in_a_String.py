class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:

        count = []
        left = 0
        p_dict = {}
        s_dict = {}
        for i in range(len(p)) :
            p_dict[p[i]] = p_dict.get(p[i] , 0) + 1
        for right in range(len(s)) :
            s_dict[s[right]] = s_dict.get(s[right] , 0) + 1
            
            while left <= right and (s[right] not in p_dict or s_dict[s[right]] > p_dict[s[right]]):
                s_dict[s[left]] -= 1
                if s_dict[s[left]] == 0:
                    del s_dict[s[left]]
                left += 1
            if right - left + 1 == len(p) :
                count.append(left)
        return count