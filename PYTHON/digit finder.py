num = input("enter a number:")
if num[0]!='-'and len(num) == 3:
    print("3digit")
elif num[0]!='-' and len (num) == 4:
    print("3 digit")
else:
    print("not a 3 digit")