def merge(nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
       class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l = nums1[:m] + nums2[:n]
        l.sort()
        for i in range(m + n):
            nums1[i] = l[i]
        return nums1
        
    
    
    
print(merge([1,2,3,0,0,0],3,[2,5,6],3))