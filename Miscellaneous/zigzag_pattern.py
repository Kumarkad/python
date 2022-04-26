def convert(s,numRows):
    if numRows==1:
        return s
    rowa={row:" " for row in range(1,numRows+1)}
    row=1
    flag=True
    
    for i in s:
        rowa[row]+=i
        if (row==1) or ((row<numRows) and flag):
            row+=1
            flag=True
            
        else:
            row-=1
            flag=False
            
    word=""
    for row in range(1,numRows+1):
        word+=rowa[row]
        
    return word.replace(" ","")
    
s=input("Enter the string : ")
numRows=int(input("Enter the number of rows : "))
print(convert(s,numRows))