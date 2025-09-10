class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarysearch(target: int, nums: List[int]) -> bool:
                left, right = 0, len(nums) - 1
                
                while left <= right:
                    mid = (left + right) // 2
                    if nums[mid] == target:
                        return True
                    elif nums[mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1
                return False
        for c in matrix:
            if binarysearch(target, sorted(c)):
                return True
        return False

        