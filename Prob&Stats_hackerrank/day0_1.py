import statistics
from scipy import stats
n= int(input())
p=list(map(int,input().split()))
print("%.1f"%statistics.mean(p))
print("%.1f"%statistics.median(p))  
print(int(stats.mode(p)[0]))