#Professor McGonagall teaches transfiguration at Hogwarts. She has given Harry the task of changing himself into a cat. She explains that the trick is to analyze your own DNA and change it into the DNA of a cat. The transfigure spell can be used to pick any one character from the DNA string, remove it and insert it in the beginning.  Help Harry calculates minimum number of times he needs to use the spell to change himself into a cat.

class Solution:
    def transfigure(self, A, B): 
        
        if len(A) != len(B):
            return -1
        da={}
        db={}
        for i in A:
            if i not in da:
                da[i]=0
            else:
                da[i]+=1
        for i in B:
            if i not in db:
                db[i]=0
            else:
                db[i]+=1
        if da == db:
            count = 0
            i = len(A) -1
            j=i
            
            while (i>=0):
                if A[i]!=B[j]:
                    count+=1
                else:
                    j-=1
                i-=1
                
            return count
        else:
            return -1

#  Driver Code

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        line = input().strip().split()
        A = line[0]
        B = line[1]
        obj = Solution();
        print(obj.transfigure(A,B))
