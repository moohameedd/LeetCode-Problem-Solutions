import math 
from typing import List

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums) - 1:
            g = math.gcd(nums[i], nums[i+1])
            if g > 1:
                nums[i] = math.lcm(nums[i], nums[i+1])
                nums.pop(i+1)
                if i > 0:
                    i -= 1
            else:
                i += 1
        return nums
