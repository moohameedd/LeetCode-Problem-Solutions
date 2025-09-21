class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
      
        l = [x for sub in matrix for x in sub]
        l.sort()
        return l[k-1]
