'''
Write a Python program to store first year percentage of students in 
array.
Write function for sorting array of floating point numbers in ascending 
order using quick sort and display top five scores
'''
def partition(arr, low, high):

    i = (low-1)   

    pivot = arr[high]   
 
    for j in range(low, high):

        if arr[j] <= pivot:

            i = i+1

            arr[i], arr[j] = arr[j], arr[i]
 
    arr[i+1], arr[high] = arr[high], arr[i+1]

    return (i+1)

def quick_sort(marks ,low ,high):
    
    if len(marks)==1:
        return marks
        
    if low < high :
        pi = partition(marks,low,high)
        
        quick_sort(marks, low, pi-1)
        quick_sort(marks, pi+1, high)
    
def top_five_marks(marks):
        print(" Marks of top five scores are : ")
        marks.reverse()
        print(marks[:6])
            
marks=[100,30,60,70,54,23,19,20,35,5]
'''
n = int(input("Enter number of students whose marks are to be displayed : "))
print("Enter marks for",n,"students : ")
for i in range(0, n):
    ele = int(input())
    marks.append(ele)  # adding the element
'''
print("The marks of",'n',"students are : ")
print(marks)

n=len(marks)

quick_sort(marks,0,n-1)

print(" Marks of students after performing quick sort : ")
for i in marks:
        print(i)
        
top_five_marks(marks)