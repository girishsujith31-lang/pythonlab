list1=input("Enter colors in list1(separated withspace)").split()
list2=input("enter colors in list 2(separated with space):").split()
result=[]
for color in list1:
    if color not in list2:
        result.append(color)
        print(result)