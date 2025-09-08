class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        s=nums1+nums2
        s.sort()
        length=len(s)
        if length%2==1:
            return float(s[length//2])
        else:
            return(s[(length//2)]+s[(length//2)-1])/2