class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ok=False
        n=0
        for i in range(len(s)-1,-1,-1):
            if "A"<=s[i].upper()<="Z":
                ok=True
                n+=1
            if ok and (s[i]==" " or i==0):
                return n
        if " " not in s:
            return len(s)
        else:
            return 1
        