# EXPERIMENT 01
# 1.A-B without using - oprator
# a = int(input("Enter the value of a: "))
# b = int(input("Enter the value of b: "))
# twos_complement_b = ~b + 1
# result = a + twos_complement_b
# print(f"The result of {a} - {b} is: {result}")

# 2.wap to perform all arithmetic operation without third variable
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# print(f"Addition: {num1 + num2}")
# print(f"Subtraction: {num1 - num2}")
# print(f"Multiplication: {num1 * num2}")
# if num2 != 0:
#     print(f"Division: {num1 / num2}")
# else:
#     print(f"Division by zero is not defined.")
# print(f"Floor Division: {num1 // num2}")
# print(f"Modulus: {num1 % num2}")
# print(f"Exponentiation: {num1 ** num2}")

# 3.SI
# principal=float(input("enter the amount:"))
# rate=float(input("enter the rate:"))
# time=int(input("enter the time period:"))
# si=(principal*rate*time)/100
# print("THE SI WILL BE=",si)

# 4.OPERATOR
# a=int(input("enter the first number:"))
# b=int(input("enter the second number:"))
# print(a&b)
# print(a|b)
# print(a^b)
# print(~a)
# print(a<<b)
# print(a>>b)

# 5.SWAPPING
# a=int(input("enter the number:"))
# b=int(input("enter the second number:"))
# a,b=b,a
# print(a,b)

# EXPERIMENT02
# 1.WAP TO INPUT THREE NUMBER AND FIND THE MAXIMUM BETWEEN THE THREE NUMBER
# a=int(input("enter the number:"))
# b=int(input("enter the number:"))
# c=int(input("enter the number:"))
# if (a>=b) and (b>=c):
#     print("a")
# elif (b >= a)and (b >= c):
#     print("b")
# else:
#     print("c")

# 2.WAP TO CHECK VOWELOR CONSONENT
# char=(input("enter the character:"))
# if char=="a"or"e"or"i"or"o"or"u":
#     print("vowel")
# else:
#     print("consonent")

# 3.LEAP YEAR
# year = int(input("enter the year"))
# if year % 4 == 0 or year % 100 ==0 or year % 400 == 0:
#     print("yes it is a leap year")
# else:
#     print("not a leap year")

# 4.divisible by 5 or 11
# a=int(input("enter the number:"))
# if(a%5==0)&(a%11==0):
#     print("a is divisible by both")
# else:
#     print("a is not divisible by both")

# 5.GRADEING
# marks=int(input("enter the marks:"))
# if marks>85:
#     print("A")
# elif marks>74 and marks<86:
#     print("B")
# elif marks>64 and marks<76:
#     print("C")
# elif marks<65:
#     print("D")
# else:
#     print("thank you")

# EXPERIMENT 03
# 1.WAP TO CHECK THE NUMBER IS  PRIME OR NOT
# num=int(input("enter the number:"))
# if num > 1:
#     for i in range(2, (num//2)+1):
#         if (num % i) == 0:
#             print(num, "is not a prime number")
#             break
#     else:
#         print(num, "is a prime number")
# else:
#     print(num, "is not a prime number")

# 2.TABLE OF A NUMBER
# num=int(input("enter a number:"))
# for i in range(1,11):
#     print(num,'x',i ,'=',num*i)

# 3.WRITE A PROGRAME TO CHECK THE NUMBER IS ARMSTRONG OR NOT
# num = int(input("Enter a number: "))
# sum = 0
# temp = num
# while temp > 0:
#    digit = temp % 10
#    sum += digit ** 3
#    temp //= 10
# if num == sum:
#    print("this is an Armstrong number",num)
# else:
#    print("this is not an Armstrong number",num)

# 4.WAP TO FIND REVERSE OF THE NUMBER
# a = input("enter the number:")
# reverse = a[ : : -1]
# if(a==reverse):
#     print('yes it is a pallindrome')
# else:
#     print('not pallindrome')

# 5.FIBONACCI SERIES
# num=int(input("enter a number:"))
# if(num==0 or num==1):
#     print("yes")
# else:
#     a=0
#     b=1
#     while(True):
#         c=a+b
#         a=b
#         b=c
#         if(c==num):
#             print("yes")
#             break
#         elif(c>num):
#             print("no")
#             break

# EXPERIMENT 04
# 1.
# row= int(5)
# for i in range(row):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

# 2.
# n = 4  
# num = 1
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(num,end=" ")
#         num +=1
#     print()

# 3.
# n = 5 
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end='')
#     print()

# 4.
# for i in range(1,5):
#      for j in range(1,5):
#          if(j>=5-i):
#              print("* ",end=' ')
#          else:
#              print(" ",end=' ')
#      print()

# 5.
# row= int(5)
# for i in range(row):
#     for j in range(5-i):
#         print("*",end=" ")
#     print()

# EXPERIMENT 05
# 1. INPUT A STRING FROM USER AND FIND ITS LENGTH
# a=(input("enter a string value="))
# print(len(a))

# 2.WAP TO FIND THE REVERSE OF GIVEN INPUT STRING
# input_string=input("enter a string value=")
# reversed_string=input_string[::-1]
# print(reversed_string)

# 3.STRING PALLINDROME CHECK
# a=input("enter a string=")
# print(a[::-1])

# 4.WAP TO PRINT EVEN LENGTH FROM GIVEN STRING
# a=("we are in GLA university")
# words=a.split()
# for word in words:
#     if len (word)%2==0:
#         print(word)

# 5.WAP TO COUNT VOWEL AND CONSONENT IN A STRING
# input_string =("my favorite hobby is to play cricket")
# vowel_count = 0
# consonant_count = 0
# vowels = "aeiouAEIOU"
# for char in input_string:
#     if char.isalpha():
#         if char in vowels:
#             vowel_count += 1
#         else:
#             consonant_count += 1
# print(f"Number of vowels: {vowel_count}")
# print(f"Number of consonants: {consonant_count}")

# EXPERIMENT 06
# 1.input a numeric list  from user and print only odd number from list
# input_string = input("Enter words separated by spaces: ")
# numbers = list(map(int, input_string.split()))
# for num in numbers:
#     if num % 2 != 0:
#         print(num)

# 2.compute all sum of all element of list
# input_string = input("Enter numbers separated by spaces: ")
# numbers = list(map(int, input_string.split()))
# total_sum = 0
# for num in numbers:
#     total_sum += num
# print("Sum of all elements:", total_sum)

# 3.print even number from list using list comprehension
# input_string = input("Enter numbers separated by spaces: ")
# numbers = list(map(int, input_string.split()))
# even_numbers = [num for num in numbers if num % 2 == 0]
# print("Even numbers:", even_numbers)

# 4. wap to remove duplicates from list
# input[2,4,6,2,3,4,8] ,, output[2,4,6,3,8]
# l1=[2,4,6,2,3,4,8]
# l2=[]
# for i in l1:
#     if i not in l2:
#         l2.append(i)
# print("list with removed duplicates",l2)

# 5.wap to add two diffrent list element?
# input[1,2,3,4]+[5,6,7,8],,output[6,8,10,12]
# list1=[1,2,3,4]
# list2=[5,6,7,8]
# result=[]
# for i in range(len(list1)):
#     result.append(list1[i]+list2[i])
# print(result)

# EXPERIMENT 07
# 1.CREATE A PROGRAM TO ADD A ITEM TO A TUPLE
# my_tuple = (1, 2, 3, 4, 5)
# new_item = 6
# new_tuple = my_tuple + (new_item,)
# print("Tuple after adding the new item will be:", new_tuple)

# 2.WAP TO REVERSE A TUPLE
# my_tuple = ("apple", "banana", "cherry", "kiwi")
# print(my_tuple[::-1])

# 3.WAP TO REPLACE THE LAST VALUE OF TUPLE IN LIST
# tuples_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# new_value = 100
# modified_list = [t[:-1] + (new_value,) for t in tuples_list]
# print(modified_list)

# 4.WAP to sum all elements in tuple 
# t = (1, 2, 3, 4, 5)
# total_sum = sum(t)
# print("Sum of all elements:", total_sum)

# 5.wap to print index of list
# lst = ['a', 'b', 'c', 'd', 'e']
# for index, element in enumerate(lst):
#     print(f"Index of {element}: {index}")

# EXPERIMENT 08
# 1.wap to iterate key value
# sample_dict = {'a': 1, 'b': 2, 'c': 3}
# for key, value in sample_dict.items():
#     print(f"Key: {key}, Value: {value}")

# 2.SUM OF ALL DICTIONARY ELEMENT
# d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# total_sum = sum(d.values())
# print("Sum of all values:", total_sum)

# 3.KEY VALUE SQUARING
# n = 5
# result_dict = {}
# for x in range(1, n + 1):
#     result_dict[x] = x * x
# print(result_dict)

# 4.SORTING THE DICTIONARY
# d = {2: 'apple', 1: 'mango', 3: 'orange'}
# sorted_dict = dict(sorted(d.items()))
# print(sorted_dict)

# 5.KEY VALUE OF DICTIONARY
# sample_dict = {'a': 1, 'b': 2, 'c': 3}
# for value in sample_dict.values():
#     print(value)

# EXPEIMENT 09 EXCEPTION
#  1.WAP HANDLE ZERO DIVISION ERROR EXCEPTION WHEN DIVIDING A NUMBER BY ZERO
# try:
#     a=10
#     b=0
#     a//b
# except:ZeroDivisionError
# result=("error:division by 0 is not allowed" )
# print(result)

# 2.WAP THAT PROMPTS THE USER TO INPUT TWO NUMBERS AND RAISE A TYPE ERROR EXCEPTION WHEN VALUE IS NOT INTEGERS
# try:
#     num1 = int(input("Enter the first number: "))
#     num2 = int(input("Enter the second number: "))
# except ValueError:
#     raise TypeError("both inputs must be numeric.")
# print(f"First number:(num1), Second number:(num2)=",num1+num2)

# 3.VALUE ERROR
# try:
#      num1 = int(input("Enter the first number: "))
# except ValueError:
#      result=("input must be integer")
# print(result)

# 4.SHOWCASE USE OF ELSE AND FINALLY
# try:
#     numerator = float(input("Enter the numerator: "))
#     denominator = float(input("Enter the denominator: "))
#     result = numerator / denominator
# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")
# else:
#     print(f"The result of the division is (result)")
# finally:
#     print("good")

# 5.CREATE A FUNCTION TO PRINT AREA OF CIRCLE
# import math
# def areaofcircle():
#      radius = float(input("Enter the radius of the circle: "))
#      area = math.pi*(radius ** 2)
#      print("The area of the circle is:",area)

# EXPERIMENT 10(FILE HANDLING)
# 1.WAP TO READ DATA FROM FILE
# file_path = 'example.txt'
# try:
#     with open(file_path, 'r') as file:
#         data = file.read()
#     print("File Contents:")
#     print(data)
# except FileNotFoundError:
#     print(f"Error: The file '{file_path}' was not found.")
# except IOError:
#     print(f"Error: An error occurred while reading the file '{file_path}'.")

# 2.WAP TO WRITE DATA INTO FILE
# file_path = 'output.txt'
# data = """
# Hello, this is a sample text.
# This file is generated by a Python script.
# """
# try:
#     with open(file_path, 'w') as file:
#         file.write(data)
#     print(f"Data successfully written to {file_path}")
# except IOError:
#     print(f"Error: An error occurred while writing to the file '{file_path}'.")

# 3.WAP TO SHOW CASE THE USEOF READ READLINE AND READLINES METHOD
# file_path = 'sample.txt'
# try:
#     with open(file_path, 'r') as file:
#         print("Using read() method:")
#         content = file.read()
#         print(content)
#     with open(file_path, 'r') as file:
#         print("\nUsing readline() method:")
#         first_line = file.readline()
#         second_line = file.readline()
#         print("First line:", first_line.strip())
#         print("Second line:", second_line.strip())
#     with open(file_path, 'r') as file:
#         print("\nUsing readlines() method:")
#         all_lines = file.readlines()
#         for index, line in enumerate(all_lines):
#             print(f"Line {index + 1}: {line.strip()}")
# except FileNotFoundError:
#     print(f"Error: The file '{file_path}' was not found.")
# except IOError:
    # print(f"Error: An error occurred while reading the file '{file_path}'.")
