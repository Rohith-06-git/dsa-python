class Solution:
    def trap(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        l_max = 0
        r_max = 0
        total_water = 0
        while left < right :
            if height[left] < height[right] :
                if l_max <= height[left] :
                    l_max = height[left]
                else :
                    total_water += l_max - height[left]
                left += 1
            else :
                if r_max <= height[right] :
                    r_max = height[right]
                else :
                    total_water += r_max - height[right]
                right -= 1
        return total_water