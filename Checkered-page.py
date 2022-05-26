def CheckeredPage():
    n=int(input('n:'))
    m=int(input('m:'))
    for j in range (m):
        if j % 2 != 0:
            for i in range (n) :
                if i % 2 != 0:
                    print ('*',end='' )
                if i % 2 == 0:
                    print('#',end=''  )
        else:
            for i in range (n) :
                if i % 2 != 0:
                    print ('#',end='' )
                if i % 2 == 0:
                    print('*',end='' )
        print("\n")        
CheckeredPage()


