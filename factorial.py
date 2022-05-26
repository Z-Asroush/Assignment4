import math
x= int(input('enter number:'))
n=1
while x>n:
    if math.factorial(n)== x:
        print('yes')
        exit()
    else :

        n=n+1
print('no')        

