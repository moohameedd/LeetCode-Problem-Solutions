class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        l=list(s)
        if l==sorted(l) or l==sorted(l,reverse=True):
            return True
        else:
            return False