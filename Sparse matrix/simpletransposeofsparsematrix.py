# SimpleTranpose of sparse matrix

# function for display transpose of sparse matrix
def displaytranspose(result):
	print(" Transpose of sparse matrix : ")
	for row in result:
		for element in row:
			print(element,end=" ")
		print()

# function for transpose the sparse matrix
def transpose(sparse):
	#print(sparse)

	result=[]
	temp=[]
	temp.append(sparse[0][1])
	temp.append(sparse[0][0])
	temp.append(sparse[0][2])
	result.append(temp)
	for i in range(sparse[0][1]):
		for j in range(1,len(sparse)):
			temp1=[]
			if i== sparse[j][1]:
	
				temp1.append(sparse[j][1])
				temp1.append(sparse[j][0])
				temp1.append(sparse[j][2])
				result.append(temp1)
	#print(result)
	displaytranspose(result)
	
	return result			

# function for display sparse matrix
def displaysparse(sparse):
	print(" display sparse matrix : ")
	for row in sparse:
		for element in row:
			print(element,end=" ")
		print()
	
	transpose(sparse)

# fuction for display the simple matrix
def display(mat):
	print(" display matrix : ")
	for row in mat:
		for element in row:
			print(element,end=" ")
		print()

# function for convert the matrix into sparse matrix
def sparse(mat,count):
			sparse=[]
			row=len(mat)
			col=len(mat[0])	
			#print('values : ',row,col,count)
			t=[]
			t.append(row)
			t.append(col)
			t.append(count)
			sparse.append(t)

			for i in range(row):
				for j in range(col):
					if mat[i][j] !=0:
						temp=[]
						temp.append(i)
						temp.append(j)
						temp.append(mat[i][j])
						sparse.append(temp)		
			displaysparse(sparse)

# function to count the total no. of non-zero value
def total(mat):
	row=len(mat)
	col=len(mat[0])
	count=0
	for i in range(row):
		for j in range(col):
			if mat[i][j] !=0:
				count=count+1
	sparse(mat,count)
	
			
mat=[[0,3,0,0],
[2,5,0,1],
[8,0,0,0],
[0,6,0,4]]

display(mat)
total(mat)