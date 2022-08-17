def xor(a, b):
    
    result = []
    
    for i in range(1, len(b)):
        
        if a[i] == b[i]:
            
            result.append('0')
            
        else:
            
            result.append('1')
            
    return ''.join(result)


def mod2div(divident, divisor):
    
    pick = len(divisor)
    
    tmp = divident[0 : pick]
    
    while pick < len(divident):
        
        if tmp[0] == '1':
            
            tmp = xor(divisor, tmp) + divident[pick]
            
        else:
            
            tmp = xor('0'*pick, tmp) + divident[pick]
            
        pick += 1
        
    if tmp[0] == '1':
        
        tmp = xor(divisor, tmp)
        
    else:
        
        tmp = xor('0'*pick, tmp)
        
    checkword = tmp
    
    return checkword


def encodeData(data, key):
    
    l_key = len(key)
    
    appended_data = data + '0'*(l_key-1)
    
    remainder = mod2div(appended_data, key)
    
    codeword = data + remainder
    
    return codeword

def decodeData(data,key):
    
    remainder =mod2div(data,key)
    
    if remainder =='0000':
        
        return True
        
    else:
        
        return False
        
    
data=input("Enter data in binary format : ")

key=input("Enter the Key : ")

ans = encodeData(data,key)

print("Encoded data to be sent to server in binary format :",ans)

checker=decodeData(ans,key)

if checker:
    
    print("Databit is successfully transmitted ")
    
else:
    
    print("Error !!!")
    
#Credit by : Kumarkad03_KD