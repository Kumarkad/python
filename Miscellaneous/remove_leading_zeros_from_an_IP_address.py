# Given an IP address, remove leading zeros from the IP address. Note that our IP address here can be a little different. It can have numbers greater than 255. Also, it does not necessarily have 4 numbers. The count can be lesser/more.

class Solution:
    def newIPAdd(self, S):
        t=0
        temp=""
        j=1
        n=len(s)
        for i in S:
            if i=="0" and t==0:
                continue
            elif i=="." and (t>0 or t==0):
                if t==0:
                    temp+="0"
                    temp+=i
                else:
                    temp+=i
                    t=0
            else:
                temp+=i
                t+=1
                j+=1
        if i=="0" and t==0:
            temp+="0"
        return temp

#  Driver Code Starts

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.newIPAdd(s)
        print(ans)
