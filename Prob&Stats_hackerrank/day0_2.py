n = int(input())
d = list()
for i in range(2):
    k=list(map(int,input().split()))
    d.append(k)


c = list(zip(*d))
p = []
for i in range(len(c)):
    p.append(c[i][0] * c[i][1])

number=sum(p)/sum(d[1])   

print("{:.1f}".format(number))