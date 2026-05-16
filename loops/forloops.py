# # # name = "ella"
# # # for char in name:
# # #     print(char) # this prints out each character in the string name

# # sales = [200, 300, 400]
# # total = 0
# # for price in sales:
# #     print(price) # this prints out each item in the list sales
# #     total += price #this adds each price to the total and updates the total with the new value
# # print("Total sales:", total)

# # from conditionals import index


# column = ["age", "income", "score"]
# for index,col in enumerate(column):
#     print("this column is at index: " + str(index) + " with a value of: " + col) # this prints out the index and the value of each item in the list column



# #zip function
# names = ["ella", "emmanuella", "chidinma"]
# ages = [20, 21, 22]
# for name, age in zip(names, ages):
#     print(name + " is " + str(age) + " years old") # this prints out the name and age of each person in the lists names and ages   




students = [
        ["ella", 19, 4.0],
        ["emmanuella", 20, 3.8],
        ["chidinma", 21, 4.2]
    ]
for student in students:
       # print(student) # this prints out each sublist in the list students
        for detail in student:
            print(detail, end=" ") # this prints out each item in the sublist student
        print() # this adds a new line after each sublist is printed
        print(f"the name of the student is {student[0]} and their age is {student[1]} with a CGPA of {student[2]}") # this prints out the name, age and gpa of each student in the list students



for i in range(10):
      if i == 5:
            print("this is the middle of the loop")
      print(i) # this prints out the value of i in each iteration of the loop

for i in range(1, 30):
      if i % 2 == 0:
            print(f"{i} is an even number")
      else:
            print(f"{i} is an odd number")