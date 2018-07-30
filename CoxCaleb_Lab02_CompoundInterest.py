#This program calculates compound interest

print("Hello! Let's save some money!")

#Get principal amount
principal = float(input("\nWhat is the amount of principal originally deposited into the account? "))

#Get annual interest rate
interest_rate = int(input("\nWhat is the annual interest rate percentage paid by the account? "))

#Convert to percentage
interest_rate = interest_rate/100

#Get number of times per year that interest is compounded
times_compounded = int(input("\nHow many times a year is the interest compounded (i.e. monthly = 12,\nquarterly = 4)? "))

#Divide interest rate by times compounded
rate_by_compound = float(interest_rate)/float(times_compounded)
rate_by_compound += 1

#Get number of years account will be left to earn interest
years = int(input("\nHow long will the account be left open to earn interest? "))

#Multiply years that account will earn interest by times compounded
years_by_compound = float(times_compounded)*float(years)

#Calculate Compound Interest
exponential_rate_by_years = float(rate_by_compound)**float(years_by_compound)

compound_interest= float(exponential_rate_by_years)*float(principal)

#Print total
print("\nYour account balance after", int(years), "years: ", format(compound_interest, '.2f'))
print("\nWow! You're rich!")
