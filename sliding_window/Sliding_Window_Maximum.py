from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        max_arr = []
        left = 0
        q = deque()
        for right in range(len(nums)) :
            while q and nums[q[-1]] < nums[right] :
                q.pop()
            q.append(right)
            if q[0] < left :
                q.popleft()
            if left <= right and right - left + 1 == k :
                max_arr.append(nums[q[0]])
                left += 1
        return max_arr