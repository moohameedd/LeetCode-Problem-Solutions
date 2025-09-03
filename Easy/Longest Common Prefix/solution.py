class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs, key=len)
        s=""
        n=len(strs)
        j=0
        ok=True
        while j<len(strs[0]) and ok:
            for i in range(1,n):
                if strs[0][j]!=strs[i][j]:
                    ok=False
                    break
            if ok:
                s+=strs[0][j]
                j+=1
        return s
