n=int(input('Enter the size of the array : '))
l=[]
for i in range(n):
    x=int(input(f'Enter number {i+1} : '))
    l.append(x)
maxi=l[0]
mini=l[0]
for i in range(1,n):
    if(l[i]>=maxi):
        maxi=l[i]
    if(l[i]<=mini):
        mini=l[i]
print(f'Maximum number : {maxi}')
print(f'Minimum number : {mini}')
