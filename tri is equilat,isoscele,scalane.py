a=int(input("Enter the value:"))
b=int(input("Enter the value:"))
c=int(input("Enter the length:"))
if a==b and a==c:
    print("it is Equilateral")
elif a==b or b==c or c==a:
    print("it is isosceles")
else:
    print("it is scalene")
    
