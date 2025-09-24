class Solution:
    def trailingZeroes(self, n: int) -> int:
            s=math.factorial(n)
            count=0
            
            while s%10==0:
                count+=1
                s=s//10
            return count