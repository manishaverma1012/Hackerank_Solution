# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
n1=list(map(int,input().split()))
n2=int(input())
n3=int(input())

def norm(x):
    c=0.5+0.5*math.erf((x-n1[0])/(n1[1]*math.sqrt(2)))
    return c


a=(1-norm(n2))*100
print("%.2f"%a)
b=(1-norm(n3))*100
print("%.2f"%b)
d=norm(n3)*100
print("%.2f"%d)
