class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0:
            return False
        else:
            s=1
            while s*4<=n:
                s=s*4
            return s==n
                
        