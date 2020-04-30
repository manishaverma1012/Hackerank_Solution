from collections import OrderedDict,defaultdict
d = OrderedDict()
m = defaultdict(list)
for i in range(int(input())):
    k = input().split()
    k[0] = ' '.join(k[0:len(k)-1])
    k[1] = int(k[len(k)-1])
    k = k[0:2]
    m[k[0]].append(k[1])
    d[k[0]] = i

for i in d:
    print(i,sum(m[i]))
