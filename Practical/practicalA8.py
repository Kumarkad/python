#Write a Python program that determines the location of a saddle point of matrix if one exists. An m x n matrix is said to have a saddle point if some entry a[i][j] is the smallest value in row i & the largest value in j.

from array import *

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m = 3
min = 0
max = 0
pos = [[0 for x in range(2)] for y in range(2)] 
print("The matrix is : ")
for r in matrix:
    print(r)
# find the saddle points in the given matrix */

for i in range(0,m):
	min = matrix[i][0]
	for j in range(0,m):
		if (min >= matrix[i][j]):
			min = matrix[i][j]
			pos[0][0] = i
			pos[0][1] = j
		j = pos[0][1];
		max = matrix[0][j];
	for k in range(0,m):
		if (max <= matrix[k][j]):
			max = matrix[i][j]
			pos[1][0] = k
			pos[1][1] = j

# saddle point is the minimum of a row and maximum of the column 
	if (min == max):
		if (pos[0][0] == pos[1][0] and pos[0][1] == pos[1][1]):
			print("Saddle point ( ", pos[0][0] , "," , pos[0][1] , " ) : " , max)