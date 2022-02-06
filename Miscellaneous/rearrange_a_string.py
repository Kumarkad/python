# Rearrange A String

class Solution:
    def arrangeString(self, s):
        
        strings=""
        num=0
        print(s)
        for i in range(len(s)) :
            print(s[i])
            if s[i].isdigit():
                num=num+int(s[i])
            else:
                strings=strings+s[i]
        ans="".join(sorted(strings))
        strings=ans+str(num)
        return strings
                
#  Driver code

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.arrangeString(s)
        print(ans)