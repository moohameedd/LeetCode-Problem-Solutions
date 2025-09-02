class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l=[]
        List=nums
        if target in List:
            l.append(List.index(target))
            l.append(len(List)-1-List[::-1].index(target))

            
        else:
            l.append(-1)
            l.append(-1)
        return l
