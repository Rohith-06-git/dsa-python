class Solution:
    def minWindow(self, s: str, t: str) -> str:
        a = len(s)
        b = len(t)
        if b > a :
            return ""
        min_size = 0
        left = 0
        t_data = {}
        s_data = {}
        min_range = (0,0)
        min_size = float("inf")
        for i in range(b) :
            t_data[t[i]] = t_data.get(t[i] , 0 ) + 1
        c = len(t_data)
        count = 0
        for right in range(a) :
            s_data[s[right]] = s_data.get(s[right] , 0 ) + 1
            if s[right] in t_data and s_data[s[right]] == t_data[s[right]] :
                count += 1

            while left <= right and count == c :
                if s[left] not in t_data or s_data[s[left]] - 1 >= t_data[s[left]] :
                    s_data[s[left]] -= 1
                else :
                    if right - left + 1 < min_size:
                        min_size = right - left + 1
                        min_range = (left, right)

                    s_data[s[left]] -= 1
                    count -= 1

                left += 1
        left_idx , right_idx = min_range
        if min_size != float("inf") :
            return s[left_idx : right_idx + 1] 
        else :
            return ""