# Gauss algorithm to find a linear combination of minimal length of two vectors
import numpy

def gauss(a,b):
    A=numpy.linalg.norm(a)**2
    B=numpy.linalg.norm(b)**2
    if(A<B):
        a,b = b,a
        A,B =B,A
    test=True
    while(test):
        if(A<B):
            a,b = b,a
            A,B =B,A
        n=numpy.dot(a,b)
        r=int(n/B)
        T=A-2*r*n+B*r**2

        if(T<B):
            test=True
            t=a-r*b
            a,b,A,B=b,t,B,T
 
        else:
            test=False
    return b

a=numpy.array([4,12,62])
b=numpy.array([5,21,30])
print(gauss(a,b))