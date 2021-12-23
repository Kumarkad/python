'''Write a Python program to compute following computation on matrix: 
a)Addition of two matrices 
b) Subtraction of two matrices 
c) Multiplication of two matrices 
d) Transpose of a matrix
'''

def add(X,Y):
    for i in range(len(X)):
        
        for j in range(len(X[0])):
            result[i][j] = X[i][j] + Y[i][j]
   
    print('Addition of matrices : ') 
    for r in result:
        print(r)

def sub(X,Y):
    for i in range(len(X)):
        
        for j in range(len(X[0])):
            result[i][j] = X[i][j] - Y[i][j]
    
    print('Subtraction of matrices : ')
    for r in result:
        print(r)

def mul(X,Y):
    for i in range(len(X)):
        
        for j in range(len(X[0])):
            result[i][j] = X[i][j] * Y[i][j]
    print('Multiplication of matrices : ')
    for r in result:
        print(r)

def trans(X):
    for i in range(len(X)):
        
        for j in range(len(X[0])):
            result[j][i] = X[i][j]
    
    print('Matrix before transpose : ')
    for x in X:
        print(x)
    
    print('Transpose of matrices : ')
    for r in result:
        print(r)
    


X = [[1,2,3],
	[4 ,5,6],
	[7 ,8,9]]

Y = [[9,8,7],
	[6,5,4],
	[3,2,1]]


result = [[0,0,0],
		[0,0,0],
		[0,0,0]]

print('Matrix X : ')
for x in X:
    print(x)

print('Matrix Y : ')
for y in Y:
    print(y)

add(X,Y)

sub(X,Y)

mul(X,Y)

trans(X)