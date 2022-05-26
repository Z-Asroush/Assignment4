def multiplication():
    n=int(input('n:'))
    m=int(input('m:'))
    for j in range (1,m+1):
        for i in range (1,n+1):
            x=j*i
            print(x,"_",end="")
        print("\n")

multiplication()