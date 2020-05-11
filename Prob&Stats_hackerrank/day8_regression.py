# Enter your code here. Read input from STDIN. Print output to STDOUT
import statistics
x=[]
y=[]
for i in range(5):
    p=list(map(int,input().split()))
    x.append(p[0])
    y.append(p[1])

X=statistics.mean(x)
Y=statistics.mean(y)

m=sum(x)
n=sum(y)
z=0
for i in range(len(x)):
    z+=x[i]**2
    

t=0    
for i in range(len(x)):
    t+=x[i]*y[i]


b=((5*t)-(m*n))/((5*z)-(m**2))
a=Y-b*X
result=a+b*80
print("%.3f"%result)

