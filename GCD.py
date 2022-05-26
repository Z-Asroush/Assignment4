x1= int(input("enter num 1:" ))
x2= int(input("enter num 2:"))

if x2>x1:
    bigger=x2 
    smaller=x1
else:
    bigger=x1 
    smaller=x2
while True:
    remaining= bigger%smaller

    if remaining==0:
        print("gcd =" , smaller)
        exit()
    else:
        bigger=smaller 
        smaller=remaining
        



