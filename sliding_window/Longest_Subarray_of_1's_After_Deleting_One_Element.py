class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        max_len = 0
        left = 0 
        num_sum = 0
        for right in range(len(nums)) :
            num_sum += nums[right]
            while left <= right and num_sum < right - left :
                num_sum -= nums[left]
                left += 1
            max_len = max(max_len , right - left )
        return max_len