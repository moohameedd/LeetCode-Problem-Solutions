class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        i=0
        ch=""
        m=0
        length=len(s)
        while i<length :
            if s[i] not in ch:
                ch+=s[i]
                i=i+1
            else:
                if m<len(ch):
                    m=len(ch)
                ch=ch[ch.index(s[i])+1:]
        if len(ch)>m:
            return len(ch)
        return m
        