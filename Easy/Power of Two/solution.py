class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False
        else:
            s=1
            while s*2<=n:
                s=s*2
            if s==n :
                return True
            else:
                return False
            