def compare(s1, s2):
    if s1 == s2:
        return f"{s1} is equal to {s2}"
    elif str1 > str2:
        return f"{s1} is greater than {s2}"
    else:
        return f"{s1} is less than {s2}"
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
result = compare_strings(s1, s2)
print(result)
