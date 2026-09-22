# a=7
# b=5
# print(a&b)
# print(~b)
# print(a^b)
# print(a|b)
# print(a<<4)
# print(b>>4)

# str1={'aman','priya',18}
# str2={'aman','priya',18}
# str3=str1
# print(str3)




# n=int(input("enter a number"))
# if (n%10==4)&(n%3==0):
#     print("number last digit is 4")
# else:
#     print("not correct")

# n=int(input("enter a number="))
# if n%10==4:
#     print("remainder is 4")
# else:
#     print("remainder is not 4")

# n=int(input("enter a number"))
# if n%7==0:
#     print("yes number is divisible by 7")
# else:
#     print("not divisible")
# n=int(input("enter a number"))
# if(n%7==0)&(n%10==5):
#     print("number last digit is 5")
# else:
#     print("not correct")

#Take an integer A as input. You have to tell whether A is divisible by both 5 and 11 or not.
# a=int(input("enter the number:"))
# if(a%5==0)&(a%11==0):
#     print("a is divisible by both")
# else:
#     print("a is not divisible by both")

# a=int(input("enter the number:"))
# b=int(input("enter the number:"))
# c=int(input("enter the number:"))
# if (a>=b) and (b>=c):
#     print("a")
# elif (b >= a)and (b >= c):
#     print("b")
# else:
#     print("c")

# RECTANGLE TRIANGLE PATTERN PRINTING
# for i in range(1,5):
#     for j in range(1,5):
#         print("* ",end=' ')
#     print()

# STRAIGHT PATTERN OF TRIANGLE
# for i in range(1,5):
#     for j in range(1,5):
#         if(j<=i):
#             print("* ",end=' ')
#         else:
#             print(" ",end=' ')
#     print()

# OPPOSITE TRIANGLE PRINTING NICHE WALA SIDE UPAR HO JATA HAI
# for i in range(1,5):
#     for j in range(1,5):
#         if(j<=5-i):
#             print("* ",end=' ')
#         else:
#             print(" ",end=' ')
#     print()

# RIGHT TO LEFT TRIANGLE PATTERN
# for i in range(1,5):
#     for j in range(1,5):
#         if(j>=5-i):
#             print("*",end=' ')
#         else:
#             print(" ",end=' ')
#     print()

# PYRAMID TYPE PATTERN PRINTING
# for i in range(1,5):
#     for j in range(1,5):
#         if(j>=5-i):
#             print("* ",end=' ')
#         else:
#             print(" ",end=' ')
#     print()

# DETERMINATION BETWEEN THE  ANGLE
# angle= int(input("enter the degree of angle:"))
# if  angle <=180:
#     print("obtuse angle")
# elif angle  ==90:
#     print("right angle")
# elif angle  <90:
#     print("acute angle")
# else:
#     print ("thankyou")

# a = int(input("enter the degree of angle="))
# b = int(input("enter the degree of angle="))
# c = int(input("enter the degree of angle="))
# if a+b+c != 180 or a == 0 or b == 0 or c == 0:
#     print("not valid triangle")
# elif a==90 or b==90 or c==90:
#     print("right triangle")    
# elif a>90 or b>90 or c>90:
#     print("obtuse triangle")
# else:
#     print("acute triangle")

# FOR OPPOSITE TRIANGLE PATTERN PRINTING
# row= int(input("enter max row:"))
# for i in range(row):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

# FOR STRAIGHT PATTERN PRINTING
# row= int(input("enter max row:"))
# for i in range(row):
#     for j in range(i-1):
#         print("*",end=" ")
#     print()

# ULTA SIDE SE STARTING POINT HAI ISS PATTERN KA
# n=5
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=' ')
#     for i in range(i+1):
#         print("*",end=' ')
#     print()

# voting system
# age = int(input("enter your age:"))
# if age>=18:
#     print("eligible to vote")
# else:
#     print("not eligible to vote")

# LEAP YEAR
# year = int(input("enter the year"))
# if year % 4 == 0:
#     print("yes it is a leap year")
# else:
#     print("not a leap year")

# str = "hello"
# print (str)
# print(str[4])
# print(str[-1])
# print(str[0:3])
# print(str[1:4])

# str=input("enter string")
# str=str.split()
# print(str)

# str=input("enter string:")
# str=(len(str))
# print(str)

# str = input("enter string:")
# str1 = str.split()
# for i in str1:
#     print(i,len(i))

# print even lenght word
# str = input("enter string:")
# str1 = str.split()
# for i in str1:
#     if len(i)%2==0:
#         print(i)

# str = "hello"
# print(str.upper())
# print(str.lower())
# print(str.isalpha())
# print(str.isalnum())
# print(str.capitalize())
# print(str.isdigit())

# condition1="True"
# condition2= "False"
# if condition1!=condition2:
#     print(True)
# else:
#     print(False)

# DAY CHECK
# day = int(input("enter the number:"))
# if day == 1:
#     print('Monday')
# elif day ==2:
#     print('Tuesday')
# elif day ==3:
#     print('Wednesday')
# elif day ==4:
#     print('Thursday')
# elif day ==5:
#     print('Friday')
# elif day ==6:
#     print('Saturday')
# else:
#     print('Sunday')

# AVERAGE
# a = int(input("enter first number="))
# b = int(input("enter second number="))
# c = int(input("enter third number="))
# d = int(input("enter fourth number="))
# e = int(input("enter fifth number="))
# avg = (a+b+c+d+e)/5
# print("average of 5 number is:",avg)

# l1=[10,20,30,40,50]
# print(l1[-2])
# print(l1[-5:-1])
# print(l1[-4])

# l1=[10,20,30,40,50]
# l1[1:3]=[22,55]
# print(l1)

# l=[]
# n=int(input("enter your value="))
# for i in range(0,n):
#     l.append(input())
# for i in l:
#     print(l,end=" ")

# FIND SUM OF ELEMENT IN LIST
# number=[1,2,3,4]
# total_sum=sum(number)
# print("f the sum of the list:", {total_sum})

# a=[1,2,3,4]
# prod=1
# for i in range(len(a)):
#     prod=prod*a[i]
# print(prod)

# a=[55,800,45,63]
# b=max(a)
# print(b)

# a=[1,2,3,4]
# b=a.index(1)
# print(b)

# thistuple=("apple","banana","cherry","orange","melon","mango")
# print(thistuple[4:])
# print(thistuple[:4])
# print(thistuple[1:4])

# x=("apple","banana","orange")
# y=list(x)
# y[1]="kiwi"
# x=tuple(y)
# print(x)

# unpacking
# fruits = ("apple","banana","cherry")
# (red,yellow,green)=fruits
# print(yellow)
# print(red)

# dict={}
# print(dict)
# print("total lenght:",len(dict))

# dict={10:"aman",20:"rishav"}
# print(dict)
# dict.update({30,"neha"})
# print(dict)

# list1=[1,2,3,4]
# list2=[3,4,5,2]
# result=[]
# for i in range(len(list1)):
#     result.append(list1[i]+list2[i])
# print(result)
    
# l1=[1,2,3,3,2,4,5,6]
# l2=[]
# for i in l1:
#     if i not in l2:
#         l2.append(i)
# print("list with removed duplicates",l2)


# input_string = input("Enter a string: ")
# words = input_string.split()
# word_frequencies = {}
# for word in words:
#     if word in word_frequencies:
#         word_frequencies[word] += 1
#     else:
#         word_frequencies[word] = 1
# for word, frequency in word_frequencies.items():
#     print(f"Word: {word}, Frequency: {frequency}")


# Wap for leap year where code ask which number should be checked for leap year
# while True:
#     year_input = input("Enter a year to check (or type 'exit' to quit): ").strip()

#     if year_input.lower() == 'exit':
#         print("Exiting the program. FIR!")
#         break
#     if not year_input.isdigit():
#         print("Please enter a  year!")
#         continue
#     year = int(year_input)
#     if (year % 4 == 0 ):
#         print(f"{year} is a Leap Year")
#     else:
#         print(f"{year} is NOT a Leap Year")

#     print()  
