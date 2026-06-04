id_card = input("do you have an id card? \n 'y' for yes and 'n' for no:").lower()
print (id_card) 
age = int(input("how old are you?: "))

if age >= 18 and id_card == "y":
    print("You are qualified for registration")
else:
    print("you are not qualified for rergistration")
