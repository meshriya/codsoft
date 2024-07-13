import random 
len=int(input("Enter the length of password "))
__password=""
a=(len//2) -2
b=2
for i in range(a):
    
    t=random.randint(97,122)
    _password=_password+chr(t)
    t=random.randint(48,57)
    _password=_password+chr(t)
    
for i in range(b):
    t=random.randint(65,90)
    _password=_password+chr(t)
    
    t=random.randint(35,38)
    _password=_password+chr(t)
    
    
print(__password)
