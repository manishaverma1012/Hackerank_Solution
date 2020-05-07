# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import factorial, exp
mean=float(input())
x=int(input())

def poiss(l, k):
    P= ((l ** k) * exp(-l))/factorial(k)
    return P


c=poiss(mean,x)
print("%.3f" %c)



