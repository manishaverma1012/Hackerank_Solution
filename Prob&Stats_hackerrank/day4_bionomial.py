from scipy.stats import binom
b=1.09
g=1
s=2.09
p=(b/s)

result=binom.rvs(size=3,n=6,p=(b/s))
print("%.3f"%result)

