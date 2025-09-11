def swap_first_last(s):
    if len(s) <= 1:
        return s
    return s[-1] + s[1:-1] + s[0]
original_string = input("enter the original string")
swapped_string = swap_first_last(original_string)
print(f"Original string: {original_string}")
print(f"Swapped string: {swapped_string}")