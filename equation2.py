import math

def equation2(a,b,c):
    delta=b*b-(4*a*c)
    x1=(-b+math.sqrt(delta))/2*a
    x2=(-b-math.sqrt(delta))/2*a
    print("x1=", x1 ,"x2=",x2)

equation2(1,1,0)
