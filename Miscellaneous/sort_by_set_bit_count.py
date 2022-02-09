# Given an array of integers, sort the array (in descending order) according to count of set bits in binary representation of array elements.

class Solution:
    def sortBySetBitCount(self, arr, n):
        
        def solve(ele):
            count = 0
            while ele: 
                count += 1
                ele = (ele & ele-1) 
            return count 
        arr.sort(key=solve, reverse=True)
 
#  Driver Code Starts

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        ob.sortBySetBitCount(arr, n)
        print(*arr)

        T -= 1


if __name__ == "__main__":
    main()
