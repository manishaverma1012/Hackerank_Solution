# Enter your code here. Read input from STDIN. Print output to STDOU
import math
a=list(map(int,input().split()))
n=int(input())
defective=a[0]/a[1]
non_defective=1-(defective)
c=math.pow(non_defective,(n-1))*defective
print("%.3f"%c)