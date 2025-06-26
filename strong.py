num = int(input("enter a num :"))
for i in range (1, num+1):
        temp = 0
        for j in str(i):
            temp = temp + fact(int(j))
        if temp == i:
         print(i, end=", ")
         def fact(a):
            fact = 1
            for i in range(1,a+1):
               fact = fact*1
               return fact
            
 
