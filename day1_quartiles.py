import statistics 
n=int(input())
p=sorted(list(map(int,input().split())))
q1=statistics.median(p[:n//2])
q2=statistics.median(p)
q3=statistics.median(p[(n+1)//2:])
print(int(q1))
print(int(q2))
print(int(q3))