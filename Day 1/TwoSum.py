class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        min_num = min(nums)
        lower_nums = [x for x in nums if x <= target] if min_num >= 0 else nums
        result = []
        for i in range(len(lower_nums)):
            for j in range(i + 1, len(lower_nums)):
                if lower_nums[i] + lower_nums[j] == target:
                    result.append(nums.index(lower_nums[i]))
                    if nums.index(lower_nums[i]) == nums.index(lower_nums[j]):
                        indices = [i for i, x in enumerate(nums) if x == lower_nums[j]]
                        result.append(indices[1])
                    else:
                        result.append(nums.index(lower_nums[j]))
                    break   
        return result
