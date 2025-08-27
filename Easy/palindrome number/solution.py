class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        i=0
        j=len(x)-1
        while j>=i:
            if x[i]!=x[j]:
                return False
            else:
                i=i+1
                j=j-1
        return True
    
    
