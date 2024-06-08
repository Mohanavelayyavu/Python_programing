n=int(input("Enter the size of the array : "))
l=[]
for i in range(n):
    x=int(input())
    l.append(x)
for i in range(n):
    for j in range(i+1,n):
        if(l[i]==l[j]):
            l[i]='p'
            l[j]='p'
print('The unique elements found in the array are : ')
for i in range(n):
    if(l[i]!='p'):
        print(l[i],end=' ')
