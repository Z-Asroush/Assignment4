x1= int(input("enter num 1:" ))
x2= int(input("enter num 2:"))

for i in range (1,10):
    a=x1*i
    

    for j in range (1,10):    
        b=x2*j
        
        if a==b:
            print("lcm = " , a)
            exit()