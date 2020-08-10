"""
Given an array nums of n integers, are there elements a, b, c in nums
such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

from typing import List
import time
import random


# classic two-pointer solution
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                current_sum = nums[i] + nums[l] + nums[r]
                if current_sum < 0:
                    l += 1
                elif current_sum > 0:
                    r -= 1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1

        return result


sol = Solution()
start_time = time.time()
# print(sol.threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]))
# print(sol.threeSum([-1, 0, 1, 2, -1, -4]))
print(sol.threeSum([random.randint(-1000, 1000) for _ in range(300)]))
print("--- %s seconds ---" % (time.time() - start_time))

"""
RESULT 

Runtime: 704 ms, faster than 94.23% of Python3 online submissions for 3Sum.
Memory Usage: 17.2 MB, less than 60.63% of Python3 online submissions for 3Sum.
"""
