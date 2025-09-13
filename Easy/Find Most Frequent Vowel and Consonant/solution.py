class Solution:
    def maxFreqSum(self, s: str) -> int:
        l = list(s)
        t = set(l)
        mv = 0  
        mc = 0  
        voy = ["a", "e", "i", "o", "u"]  

        for c in t:
            freq = l.count(c)
            if c in voy:
                if freq > mv:
                    mv = freq
            else:
                if freq > mc:
                    mc = freq

        return mv + mc
