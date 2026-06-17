class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        left = 0
        total_sum = 0
        count = 0
        prefix_zeros = 0
        
        for right in range(len(nums)):
            total_sum += nums[right]
            
            while left < right and total_sum > goal:
                total_sum -= nums[left]
                left += 1
                prefix_zeros = 0
         
            while left < right and nums[left] == 0 and total_sum == goal:
                prefix_zeros += 1
                total_sum -= nums[left]
                left += 1
             
            if total_sum == goal:
                count += 1 + prefix_zeros
                
        return count

            