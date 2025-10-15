a=int(input("Enter the aptitude mark:"))
b=int(input("Enter the GD mark:"))
c=int(input("Enter the technical mark:"))
d=int(input("Enter the HR mark:"))
tot=a+b+c+d
if a>=85 and tot>380 and tot<=400:
    print("you are eligible for job")
    print("your salary = 30000")
elif b>=90 and tot>380 and tot<=390:
    print("you are eligible for job")
    print("your salary = 28000")
elif c>=80 and tot>370 and tot<=380:
    print("you are eligible for job")
    print ("your salary =25000")
elif d>90 and tot>350 and tot<=370:
    print("you are eligible for job")
    print("your salary = 20000")
else:
    print("you are not eligible for job")
        
