n=int(input("Enter the size of the array : "))
l=[]
for i in range(n):
    x=int(input(f'Enter the value of l[{i+1}] : '))
    l.append(x)
s=0
for i in range(n):
    s=s+l[i]
print(f'The sum of array elements = {s}')
