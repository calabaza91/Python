#Sum of Digits

print('Let\'s add some digits!')
#Get digits
strNum = input('Enter a series of digits with nothing separating them: ')

#Check if string is digits
checkNum = strNum.isdigit()

#If data inputted does not contain only digits, make user reenter data
#until data is only digits
while checkNum is False:
    print('Please only enter digits.')
    strNum = input('Enter a series of digits with nothing separating them: ')
    checkNum = strNum.isdigit()


#Accumulator
total = 0
#Iterate through number in string form
for char in strNum:
    #Change each index into an integer
    num = int(char)
    #Add to total
    total += num

#Display total
print("The total sum of your digits, ",strNum,", is ",total,'.', sep='')
