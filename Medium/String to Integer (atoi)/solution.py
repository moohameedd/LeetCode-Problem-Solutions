class Solution:
    def myAtoi(self, s: str) -> int:
        while len(s)>0 and s[0]==" ":
            s=s[1:]
        signe=""
        if len(s)>0 and ( s[0]=="+" or s[0]=="-"):
            signe=s[0]
            s=s[1:]
            
        ch=""
        for i in range(len(s)):
            if s[i] in "0123456789":
                ch+=s[i]
            else:
                break
        if ch=="" :
            return 0
        elif int(signe+ch)>(2**31)-1:
            return (2**31)-1
        elif int(signe+ch)<-((2**31)-1):
            return -(2**31)
            
        else:
            return int(signe+ch)
                