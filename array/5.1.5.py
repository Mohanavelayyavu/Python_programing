from math import sqrt
n=int(input('Enter the size of the array : '))
l=[]
for i in range(n):
    x=float(input())
    l.append(x)
mean=0
for i in range(n):
    mean=mean+l[i]
mean=mean/n
s=0
for i in range(n):
    b=l[i] - mean
    c=b*b
    s=s+c
variance = s/n
deviation = sqrt(variance)
print('Mean = ',mean)
print('variance = ',variance)
print('deviation = ',deviation)
