#N = int(input("Enter a number: "))
#if N <= 0:
 #   print("Please enter a positive integer.")
#else:
    # Print natural numbers from N to 1
 #   print("Natural numbers from", N, "to 1:")
  #  for i in range(N, 0, -1):
   #     print(i, end=" ")

#list = ['learnig','python','is','very','easy']
#list.reverse()
#print(list)

#num = int(input("enter a number:"))
#sum_even = 0
#for num in range(1, num + 1):
 #   if num % 2 == 0:
  #      sum_even += num
   #     print (sum_even)



#str = "learing python is very easy"
#reversed_str = str[::-1]
#print("Reversed order by character:",reversed_str)

'''num = int(input("enter a number:"))
sum_odd = 0
for num in range(6, num + 101):
    if num % 2 != 1:
       sum_odd += num
    print ("sum of odd is less than 5:",sum_odd)'''

'''string1 = ("binit")
string2 = ("kumar")
print(string1+string2)'''

row = int(input("enter max rows: "))
for i in range(row): 
    for j in range(i+1):
        print("* ", end="")
    print("")
