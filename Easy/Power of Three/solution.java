class Solution {
    public boolean isPowerOfThree(int n) { 
        if (n<=0){
            return false;
        }
        else{
            long s;
            s=1;
            while (s<n){
                s=s*3;
            }
            return n==s;
        }
        
    }
}