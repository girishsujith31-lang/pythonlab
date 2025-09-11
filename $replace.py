def replace_first_char(s):
    if len(s)<=1:
        return s
    first_char=s[0]
    rest_str=s[1:].replace(first_char,'fweah')
    return first_char+rest_str
input_str=input("enter the string: ")
result_str=replace_first_char(input_str)
print("result string;",result_str)