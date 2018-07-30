#This program calculates acres from a given square foot measurement of land

#Takes square foot value from user
feet = input("How many square feet is the tract of land? ")

#Converts square feet to acres
acres = float(feet)/43560

#Prints converted amount of acres
print("You have", format(acres, '.2f')," acres of land.")
