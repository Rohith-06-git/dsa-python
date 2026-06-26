class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        left = 0
        left2 = 0
        words_dict = {}
        for word in words:
            words_dict[word] = words_dict.get(word, 0) + 1

        count = 0
        idx_arr = []
        k = len(words[0])
        w = len(words)
        for i in range(k) :
            left = i
            left2 = i
            s_dict = {}
            count = 0

            for right in range(i,len(s)- k + 1 ,k) :
                sub_s = s[right : right + k]
                
                if sub_s not in words_dict :
                    s_dict.clear()
                    count = 0
                    left = right + k
                    left2 = left
                else :
                    s_dict[sub_s] = s_dict.get(sub_s , 0) + 1
                    count += 1
                    left = right + k
                while sub_s in s_dict and s_dict[sub_s] > words_dict.get(sub_s, 0):
                    sub_s2 = s[left2 : left2 + k]
                    if sub_s2 in s_dict:
                        s_dict[sub_s2] -= 1
                        if s_dict[sub_s2] == 0:
                            del s_dict[sub_s2]
                    left2 += k
                    count -= 1
                if count == w :
                    if s_dict == words_dict :
                        idx_arr.append(left2)

                    sub_s2 = s[left2 : left2 + k]
                    if sub_s2 in s_dict :
                        s_dict[sub_s2] -= 1
                        if s_dict[sub_s2] == 0 :
                            del s_dict[sub_s2]
                    left2 += k
                    count -= 1

        return idx_arr