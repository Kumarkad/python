# to count the special characters omitted in the string


import re

def count_special(word):
    special_char = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    count=0
    for i in word:
        if special_char.search(i)==None :
            pass
        
        else:
            count +=1
            
    return count
    
word=input()
print(count_special(word))