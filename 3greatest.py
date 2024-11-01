a=int(input("Enter number1\n:"))
b=int(input("Enter number2\n:"))
c=int(input("Enter number3\n:"))
if a==b==c:
    print("All are equal")
elif a==b:
    if c>a:
        print(f"{c} is greatest")
        print(f"{a} and {b} are equal")
    else:
        print(f"{c} is smallest")
        print(f"{a} and {b} are equal")
elif b==c:
    if a>b:
        print(f"{a} is greatest")
        print(f"{b} and {c} are equal")
    else:
        print(f"{a} is smallest")
        print(f"{b} and {c} are equal")
elif c==a:
    if b>c:
        print(f"{b} is greatest")
        print(f"{c} and {a} are equal")
    else:
        print(f"{b} is smallest")
        print(f"{c} and {a} are equal")
else:
    if a>b and a>c:
      print(a,"is the greatest")
    elif b>a and b>c:
      print(b,"is the greatest")
    elif c>a and c>b:
      print(c,"is the greatest")
    else:
        print('Enter a proper input')
