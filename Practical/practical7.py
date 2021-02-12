"""Write a Python Program for magic square. A magic square is an n * n matrix of the 
integers 1 to n2 such that the sum of each row, column, and diagonal is the same. The 
figure given below is an example of magic square for case n=5. In this example, the 
common sum is 65. """
def createSquare(n):
	mat=[[0 for i in range(n)]for j in range(n)]
	c=n
	r=n
	count=1
	rang=r*c
	i=0
	j=int(c/2)
	mat[i][j]=count
	
	while count<rang:
		count=count+1
		
		if (i-1)<0 and (j-1)<0:
			i=i+1
		elif (i-1)<0:
			i=c-1
			j=j-1
		elif(j-1)<0:
			j=c-1
			i=i-1
		elif (mat[i-1][j-1] !=0):
			i=i+1
		else:
			j=j-1
			i=i-1
		mat[i][j]=count
	print("Magic Squre for n =", n)
	print("Sum of each row or column",
		n * (n * n + 1) / 2, "\n")
	
	for i in range(n):
		print(mat[i])

n=int(input("Enter the no. for matrix : "))
createSquare(n)
