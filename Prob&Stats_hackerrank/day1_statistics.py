import statistics
n=int(input())
p=list(map(int,input().split()))
u=statistics.mean(p)
m=[]
for i in range(len(p)):
    q=p[i]-u
    x=q**2
    m.append(x)

y=sum(m)/n
sqrt = y ** 0.5
print('%.1f'%sqrt)
