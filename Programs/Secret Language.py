def Encode():
    import string
    import random

    msg = input("Hn Ballu?:") 
    a_msg = msg.split()  

    r1 = ''.join(random.choices(string.ascii_letters + string.digits, k=3))  
    r2 = ''.join(random.choices(string.ascii_letters + string.digits, k=3))  
    for i in range(len(a_msg)):
        items = list(a_msg[i])  
        if len(items) > 3:
            items[0], items[-1] = items[-1], items[0]  
            items.insert(0, r1)  
            items.append(r2) 
            a_msg[i] = ''.join(items) 
        elif len(items) < 3:
            a_msg[i] = ''.join(items[::-1])  

    
    print(a_msg)

"""Encode()       

def Decode(encoded_msg):
    for i in range(len(encoded_msg)):
        items=list(encoded_msg[i])
        if len(items)>3: 
            del items[0:3]
            del items[-3:]
            items[0], items[-1] = items[-1], items[0] 
            encoded_msg[i]=''.join(items)
        elif len(items)<3:
           encoded_msg[i]=''.join(items[::-1])
    print(encoded_msg)
    
encoded_msg=['nh', 't3ElotehxtU', 't3EojaaxtU']    
Decode(encoded_msg)""" 
    

        

    

