"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what.
Its maximum jump length is 0, which makes it impossible to reach the last index.
"""
import operator
from typing import List
import time
import random


def findBestJump(nums, current_index, next_index):
    best_jump_tuple = (0, 0)
    length = next_index - current_index
    for i in range(0, length):
        if nums[next_index - i] > 0:
            distance = nums[next_index - i] - i
            if distance > best_jump_tuple[1]:
                best_jump_tuple = ((next_index - i), distance)

    if best_jump_tuple[1] > 0:
        return best_jump_tuple[0]

    return -1


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if 0 not in nums or len(nums) == 1:
            return True

        current_index = 0
        length = len(nums) - 1
        while current_index < length:
            next_index = current_index + nums[current_index]
            if next_index >= length:
                return True
            non_zero_index = findBestJump(nums, current_index, next_index)
            if non_zero_index != -1:
                current_index = non_zero_index
                continue
            return False


sol = Solution()
start_time = time.time()
print(sol.canJump([5,9,3,2,1,0,2,3,3,1,0,0]))
# print(sol.canJump([random.randint(0, 100000) for _ in range(3000)]))
print("--- %s seconds ---" % (time.time() - start_time))

"""
RESULT

Runtime: 88 ms, faster than 89.80% of Python3 online submissions for Jump Game.
Memory Usage: 15.8 MB, less than 66.04% of Python3 online submissions for Jump Game.
"""