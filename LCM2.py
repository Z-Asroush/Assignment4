from ast import Import
import math

x1= int(input("enter num 1:" ))
x2= int(input("enter num 2:"))

LCM=(x1*x2)/math.gcd(x1,x2)
print("LCM = ", LCM)