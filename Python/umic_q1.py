from numpy import * 
import numpy as np
import sympy as sp

with open("myFirstFile.txt",'r+') as data:
    data.truncate(0)
    d= int(input())
    def prime(x):    
        for i in range(2,x):
            if x%i == 0:
                return False
                break
            else: 
                continue
    a=[]
    if d>1:
        for i in np.arange(10**(d-1), 10**(d)):
            if prime(i) != False:
                a.append(i)
    elif d==1:
        for i in np.arange(2, 10**(d)):
            if prime(i)!=False:
                a.append(i)
    for j in range(len(a)-1):
        if a[j+1]-a[j]==2 :
            data.write("{0} {1} \n".format(a[j],a[j+1])) 
        print(data.read())
print("\n")

