#This program predicts and displays an approximate size
#of a population of organisms.

#Get starting number of organisms
population = int(input("Starting number of organisms: "))
#Get average daily increase
growth = float(input("Average daily increase: "))
#Divide by 100 to get percent in decimal form
growth /= 100
#Get number of days to multiply
days = int(input("Number of days to multiply:"))


#Displays headings of table and Day 1 with Initial Population
print("\nDay Approximate","\tPopulation")
print("----------------------------------")
print("1", '\t\t\t', population)

#Iterate daily population growth 
for days in range(2, days+1):

    #Multiply starting number by growth rate plus 1
    population = (population * (growth+1))

    #Display table without extra zeros with '%g'%(population)
    print(days, '\t\t\t', '%g'%(population))
