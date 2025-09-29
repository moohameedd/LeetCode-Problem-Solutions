class Solution:
    def addDigits(self, num: int) -> int:
        s=str(num)
        while len(s)>1:
            n=0
            for c in s:
                n+=int(c)
            s=str(n)
        return int(s)