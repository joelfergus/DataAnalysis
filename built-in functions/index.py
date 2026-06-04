name = "ella"
print(name) #this print out the value of name
print(len(name)) #this prints out the lenght of name
print(type(name)) # this prints the data type

names = ["elle", "emmanuella", "chidinma"]
names.append("bemi") #this adds only one item to the list
names.extend(["joan", "akpewve"]) #adss ,multiple items to the ist
print(names)

#ADDING ITEMS TO A LIST VIA USER INPUT
credentials = []
username = input("enter username: ")
password = input("enter password: ")
age = input("enter age: ")
location = input("what is your location?: " )
#credentials.append(username)
#credentials.append(password)
#credentials.append(age)
credentials.extend([username, password, age])

#inserting into a specific position on a list
credentials.insert(3, location) 

#removing an item from a list
credentials.remove(password)


print(credentials)
print(credentials[2])# gets the third value in the list




