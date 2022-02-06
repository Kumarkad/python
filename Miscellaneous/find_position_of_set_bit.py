import math

class Solution:
    def findPosition(self, N):
        
        if N==0:
            return -1
        if math.floor(math.log2(N))==math.ceil(math.log2(N)):
            return int(math.log2(N)+1)
        else:
            return -1

#  Driver Code Starts

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        
        ob = Solution()
        print(ob.findPosition(N))
