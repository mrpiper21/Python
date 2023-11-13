class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        List = {}
        for i in len(nums):
            x = target - nums[i]

            if x in List:
                return [i, List[x]]
            List[i] = i