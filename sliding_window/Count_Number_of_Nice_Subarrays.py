class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        left = 0 
        count = 0
        even_no = 0
        odd_no = 0 

        for right in range(len(nums)) :
            if nums[right] % 2 != 0 :
                odd_no += 1
            while left < right and nums[left] % 2 != 0 and odd_no > k :
                odd_no -= 1
                left += 1
                even_no = 0
            while left <= right and nums[left] % 2 == 0 and odd_no == k :
                even_no += 1
                left += 1
            if odd_no == k :
                count += 1 + even_no
        return count 

            
        



                
            
            
        