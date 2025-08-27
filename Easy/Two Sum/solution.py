class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range (len(nums)-1):
            s = nums[i]
            for j in range (len(nums)):
                if i==j:
                    continue
                else:
                    if s+nums[j]==target:
                        return [i,j]
        
