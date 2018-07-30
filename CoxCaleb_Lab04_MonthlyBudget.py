#This program tells the user if they are over, under or have made their budget

#Get budget
budget = float(input("Enter your monthly budget: "))

#Set total variable
total = 0.00

#Set control variable
keep_going = 'y'

#Get series of expenses
while keep_going == 'y':

    #Get expense
    number = float(input('Enter an expense: '))
    #Add expense to total
    total += number

    #Check for control variable
    keep_going = input("Are there any more expenses this month? (y/n) ")

#Check if total of expenses is over budget
if total > budget:
    print("Your total expenses of $", format(total, '.2f'), \
          " is over your budget of $", format(budget,'.2f'),".\n"\
          "You spent too much!!", sep='')
    
#Check if total of expenses is under budget
elif total < budget:
    print("Your total expenses of $", format(total, '.2f'), \
          " is under your budget of $", format(budget,'.2f'),".\n"
          "You put those coupons to use!", sep='')
    
#Check if total of expenses is exactly the amount of budget
else:
    print("Your total expenses of $", format(total, '.2f'), \
          " is equal to your budget of $", format(budget,'.2f'),".\n"\
          "You zeroed out.", sep='')
