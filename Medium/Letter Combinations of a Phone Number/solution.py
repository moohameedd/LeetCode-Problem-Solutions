class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def find(x):
            if x=="1":
                return ""
            if x=="2":
                return "abc"
            if x=="3":
                return "def"
            if x=="4":
                return "ghi"
            if x=="5":
                return "jkl"
            if x=="6":
                return "mno"
            if x=="7":
                return "pqrs"
            if x=="8":
                return "tuv"
            if x=="9":
                return "wxyz"
        l=[]
        x=len(digits)
        if x==1:
            ch=find(digits[0])
            for c in ch:
                l.append(c)
        if x==2:
            ch1=find(digits[0])
            for i in range(len(ch1)):
                ch2=find(digits[1])
                for j in range(len(ch2)):
                    l.append(ch1[i]+ch2[j])
        if x==3:
            ch1=find(digits[0])
            for i in range(len(ch1)):
                ch2=find(digits[1])
                for j in range(len(ch2)):
                    ch3=find(digits[2])
                    for k in range(len(ch3)):
                        l.append(ch1[i]+ch2[j]+ch3[k])
                        
        if x==4:
            ch1=find(digits[0])
            for i in range(len(ch1)):
                ch2=find(digits[1])
                for j in range(len(ch2)):
                    ch3=find(digits[2])
                    for k in range(len(ch3)):
                        ch4=find(digits[3])
                        for x in range(len(ch4)):
                            l.append(ch1[i]+ch2[j]+ch3[k]+ch4[x])
                            
        return l
            