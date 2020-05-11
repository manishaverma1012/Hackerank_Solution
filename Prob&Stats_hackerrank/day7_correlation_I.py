# Enter your code here. Read input from STDIN. Print output to STDOUT
import statistics
n=int(input())
p=list(map(float,input().split()))
q=list(map(float,input().split()))
x=statistics.mean(p)
y=statistics.mean(q)


z=0
for i in range(n):
    z+=(p[i]-x)*(q[i]-y)

M=0
N=0
for i in range(n):
    M+=(p[i]-x)**2


for i in range(n):
    N+=(q[i]-y)**2
 
a=(M/n)**0.5
b=(N/n)**0.5

cov=(1/n)*z


r=cov/(a*b)
print("%.3f"%r)