class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        l = len(s2)
        if k > l :
            return False
        s1_dict = {}
        s2_dict = {}
        for i in range(k) :
            s1_dict[s1[i]] = s1_dict.get(s1[i] , 0) + 1
        left = 0
        for right in range(l) :
            s2_dict[s2[right]] = s2_dict.get(s2[right] , 0 ) + 1
            if left <= right and right - left + 1 == k :
                if s1_dict == s2_dict :
                    return True
                else :
                    s2_dict[s2[left]] -= 1
                    if s2_dict[s2[left]] == 0:
                        del s2_dict[s2[left]]
                left += 1
        return False
