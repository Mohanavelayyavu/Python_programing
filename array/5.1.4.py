def display(arr):
    print("The elements of the array are:", ' '.join(map(str, arr)))
def delete(arr, location):
    if 0 <= location < len(arr):
        removed = arr.pop(location)
        print(f"Deleted element {removed} from location {location}")
    else:
        print("Invalid location")
arr = []
n = int(input("Enter the number of elements: "))
print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))
display(arr)
location = int(input("Enter the location to insert: "))
element = int(input("Enter the element to insert: "))
if 0 <= location <= len(arr):
    arr.insert(location, element)
    print(f"Inserted {element} at location {location}")
else:
    print("Invalid location")
display_array(arr)
location = int(input("Enter the location to delete: "))
delete(arr, location)
display(arr)
