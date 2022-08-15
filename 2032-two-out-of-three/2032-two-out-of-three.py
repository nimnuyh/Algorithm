class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :rtype: List[int]
        """
        nums1 = set(nums1)
        nums2 = set(nums2)
        nums3 = set(nums3)
        
        ans = list((nums1 & nums2) | (nums2 & nums3) | (nums3 & nums1))
        return ans