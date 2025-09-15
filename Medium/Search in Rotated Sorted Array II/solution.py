class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        nums=sorted(nums)
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
        