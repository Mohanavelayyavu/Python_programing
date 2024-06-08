n=int(input("Enter array size: "))
a=[]
for i in range(n):
    x=int(input())
    a.append(x)
s=0
for i in range(n):
    for j in range(i+1,n):
        if(a[i]==a[j]):
            print(f'The repetitive element : {a[i]}')
            s=1 
            break
if(n<=0):
    print('Invalid input')
elif(s==0):
    print('Array elements are not repeted')
