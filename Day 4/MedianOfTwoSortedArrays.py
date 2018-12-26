class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        result = nums1 + nums2
        result.sort()
        
        if len(result) % 2 != 0:
            return result[len(result) // 2]
        else:
            return (result[len(result) // 2] + result[(len(result) - 1) // 2]) / 2.0
