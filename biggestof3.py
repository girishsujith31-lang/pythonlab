a= int(input("Enter first number:"))
b= int(input("Enter second number:"))
c= int(input("Enter third number:"))

if a>=b and a>=c:
    print("biggest number is:",a)
elif b>=a and b>=c:
    print("biggest number is:",b)
else:
    print("biggest number is: ",c)

