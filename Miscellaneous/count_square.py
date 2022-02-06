def count_square(n):
    count=0;
    for i in range(2,n+1,2):
        k=n-i+1
        count +=(k*k)
        
    return count

n=int(input('Enter : '))
print(count_square(n))