class Solution:
    def sortVowels(self, s: str) -> str:
        voy=["A","E","I","O","U"]
        v=[]
        l=list(s)
        for c in l:
            if c.upper() in voy:
                v.append(c)
        v.sort()
        n=len(l)
        j=0
        for i in range(n):
            if l[i].upper() in voy:
                l[i]=v[j]
                j+=1
        return ''.join(l)
        