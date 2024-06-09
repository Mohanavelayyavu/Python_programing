import math
def is_perfect_square(num):
    """Checks if a number is a perfect square."""
    sqrt_num = int(math.sqrt(num))
    return sqrt_num * sqrt_num == num
def largest_not_perfect_square(arr):
    """Finds the largest number that is not a perfect square."""
    max_num = -1
    for num in arr:
        if not is_perfect_square(num) and num > max_num:
            max_num = num
    return max_num
if __name__ == "__main__":
    size = int(input("Enter array size: "))
    if size <= 0:
        print("Invalid input")
    else:
        elements = list(map(int, input("Enter array elements: ").split()))
        largest_num = largest_not_perfect_square(elements)
        if largest_num == -1:
            print("There is no number that is not a perfect square")
        else:
            print(f"The largest number that is not a perfect square: {largest_num}")
