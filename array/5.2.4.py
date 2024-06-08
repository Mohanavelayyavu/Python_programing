n=int(input("Enter how many values you want to read : "))
a=[]
for i in range(n):
    x=int(input(f'Enter the value of a[{i+1}] : '))
    a.append(x)
b=[]
for i in range(n):
    x=int(input(f'Enter the value of b[{i+1}] : '))
    b.append(x)
s=0
for i in range(n):
    if(a[i]==b[i]):
     s=s+1 
if(n<=0):
    print("Invalid input")
elif(s==n):
    print("Both arrays are equal")
else:
    print("Both arrays are not equal")
