# Find the number of numbers that have even number of digits
def digits(num):
    count=0
    while(num>0):
        count+=1
        num=int(num/10)
        
    return count

def iseven(num):
    count=0
    even=digits(num)
    if even%2==0:
        count+=1
    return count

def findcount(arr):
    count=0
    for num in arr:
        even=iseven(num)
        if even==True:
            count+=1
            
    return count
ls=[738,8391,73,92010,7373,8]     
print(ls)
print(findcount(ls))          