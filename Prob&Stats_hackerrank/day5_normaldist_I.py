# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
n1=list(map(int,input().split()))
n2=float(input())
n3=list(map(int,input().split()))

def norm(x):
    c=0.5+0.5*math.erf((x-n1[0])/(n1[1]*math.sqrt(2)))
    return c


a=norm(n2)
print("%.3f"%a)
b=norm(n3[1])
d=norm(n3[0])
z=b-d
print("%.3f"%z)
