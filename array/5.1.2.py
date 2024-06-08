n=int(input('Enter the size of the array : '))
l=[]
for i in range(n):
    x=int(input())
    l.append(x)
m=int(input('Enter the number to find : '))
p=-1
for i in range(n):
    if(l[i]==m):
        p=i
if(p==-1):
    print(f'The number {m} is not found in the array')
if(p!=-1):
    print(f'The number {m} is found at the position {p+1}')
