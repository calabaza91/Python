#This program asks the user to enter a series of 20 numbers
#and stores in a list

#Constant for size of list
NUM_BERS = 20

def main():
    
    print('Let\'s make a number list!')
    try:
        #Makes list with 20 indexes 
        nums = [0] * NUM_BERS
        
        #Accumulator
        total = 0
        
        #User enters number for each index in list
        for index in range(NUM_BERS):
            print('Enter a Number: ')
            nums[index] = int(input())

            #Adds value to accumulator
            total += nums[index]

        #Calculates average
        average = total/NUM_BERS
        
    #Exception handler for any errors
    except Exception as err:
        print(err)
        
    #Displays list, min, max, total and average if no errors occur
    else:
        print('\nYour list is this: ')
        print(nums)
        print('---------------------------------')
        print('The lowest number is: ', min(nums))
        print('The highest number is:', max(nums))
        print('The total sum of the list is: ', total)
        print('The average of the list is: ', average)
main()
