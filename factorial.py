def fact(a):
    fact = 1
    for i in range(1,a+1):
        fact = fact * i
        return fact

num = int(input("enter a number: "))
for i in range(1, num+1):
    if i < num:
        print(i,"/",fact(i), sep="",end=" + ")
    else:
         print(i, "/",fact(i),sep="")
