lst = ["Binit","Adarsh","Rohan","Rahul"]
lststu = list(enumerate(lst))
for rollno,name in lststu:
    print("\nRoll No:",rollno+1)
    print("Student Name:",name)