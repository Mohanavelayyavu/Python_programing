def count_subsets(a):
    n = len(a)
    return 2 ** n
n = int(input("Enter array size: "))
if n <= 0:
    print("Invalid input")
else:
    print(f"Enter {n} elements:")
    a=list(map(int, input().split()))
    subsets_count = count_subsets(a)
    print(subsets_count)
