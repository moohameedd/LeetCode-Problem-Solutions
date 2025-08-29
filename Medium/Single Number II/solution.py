class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s=set(nums)
        for c in s:
            if nums.count(c)==1:
                return c