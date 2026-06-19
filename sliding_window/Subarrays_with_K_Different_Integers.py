class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        left = 0 
        count = {}
        dist_count = 0 
        required = 0 
        prefix_num = 0
        for right in range(len(nums)) :
            rk = str(nums[right])
            if count.get(rk , 0) == 0 :
                dist_count += 1
            count[rk] = count.get(rk , 0) + 1
            while dist_count > k :
                lk = str(nums[left])
                count[lk] -= 1
                if count[lk] == 0 :
                    dist_count -= 1
                left += 1
                prefix_num = 0
            while count[str(nums[left])] > 1 :
                lk = str(nums[left])
                count[lk] -= 1
                left += 1
                prefix_num += 1
            if dist_count == k :
                required += 1 + prefix_num

        return required 