a=int(input("Enter the no of class held:"))
b=int(input("Enter the no of class attended:"))
c=b/a*100
if c>75:
    percentange=c/100
    print("your attend percentage:",percentange)
    print("you are allow to exam hall")
else:
    print("you are not allow to exam hall")
