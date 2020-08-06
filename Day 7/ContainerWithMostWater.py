"""
Given n non-negative integers a1, a2, ..., an , 
where each represents a point at coordinate (i, ai). n vertical lines are drawn such 
that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container,
such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49
"""
from typing import List
import time


class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) == 2:
            return min(height)

        _max_area = 0
        l = 0
        r = len(height) - 1
        while l < r:
            current_area = (r - l) * min(height[l], height[r])
            if current_area > _max_area:
                _max_area = current_area

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return _max_area


start_time = time.time()
sol = Solution()
print(sol.maxArea(
    [1, 2, 1]))
print("--- %s seconds ---" % (time.time() - start_time))

"""
RESULT

Runtime: 124 ms, faster than 94.01% of Python3 online submissions for Container With Most Water.
Memory Usage: 15.4 MB, less than 26.74% of Python3 online submissions for Container With Most Water.
"""
