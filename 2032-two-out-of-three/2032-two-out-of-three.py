class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :rtype: List[int]
        """
        num = nums1 + nums2 + nums3
        num_list = [nums1, nums2, nums3]
        num_set = set(num)
        a = []
        for i in num_set :
            c = 0
            for j in num_list :
                if j.count(i) > 0 :
                    c += 1
            if c > 1 :
                a.append(i)
        return a