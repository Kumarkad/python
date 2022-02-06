# Shortest Unique prefix for every word

class Solution:
    def findPrefixes(self, arr, N):
        
        k=0
        i=1
        ans=[]
        while(k<N ):
            o=[]
            p=arr[k][:i]
            for l in arr:
                if(l.startswith(p)):
                    o.append(l)
            if(len(o)!=1):
                i=i+1
            else:
                ans.append(p)
                k=k+1
                i=1
        return ans

#  Driver Code Starts

import sys
sys.setrecursionlimit(10**6)
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=list(map(str,input().split()))
        
        ob = Solution()
        res = ob.findPrefixes(arr,N)
        for i in res:
            print(i,end=" ")
        print()
