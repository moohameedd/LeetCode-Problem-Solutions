class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        s=set(nums)
        l=[]
        for c in s:
            if nums.count(c)==1:
                l.append(c)
        return l
        