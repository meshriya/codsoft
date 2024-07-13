a=int(input(" "))
b=int(input(" "))
print("""1. Enter 1 for Addition
         2. Enter 2 for Subtraction
         3. Enter 3 for Multiplication
         4. Enter 4 for Division""")
c=int(input(" "))
d=0

if c==1:
    d=a+b
elif c==2:
    d=a-b
elif c==3:
    d=a*b
elif c==3:
    d=a/b
else:
    print("Invalid Input")
print (d)

