n=int(input("Enter the size of the array : "))
l=[]
for i in range(n):
    x=int(input(f'Enter the value of l[{i+1}] : '))
    l.append(x)
for i in range(n):
    for j in range(i+1,n):
        if(l[i]>l[j]):
            l[i],l[j]=l[j],l[i]
print(f'Array sorted in ascending order = {l}')
