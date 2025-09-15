class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        s=list(map(str,text.split()))
        nb=len(s)
        for c in s:
            for k in brokenLetters:
                if k in c:
                    nb=nb-1
                    break
        return nb
            