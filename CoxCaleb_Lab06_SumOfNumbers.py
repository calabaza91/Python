#Creates file of numbers and then finds the sum of all the numbers

import random

def main():
    
    #Open file
    outfile = open('numbers.txt', 'w')

    #Sets random number for series of nadom numbers
    randNum = random.randint(1,10)

    print('Numbers to be added:')
    for num in range(1, randNum + 1):
    #Get numbers and change numbers to string
        outfile.write(str(num) + '\n')

        print(num)
    #Close file
    outfile.close()

    print('Data saved to file. \n')

    #Open File for reading
    infile = open('numbers.txt', 'r')

    
    print('Reading file. The numbers are:')
    
    total = 0

    #Iterates through each line in file
    for line in infile:
        #Convert string number to integer number
        numInt = int(line)
        
        #Displays numbers in 
        print(str(numInt))
        total += numInt

        
    print("The total is: ", total)

    print('Done reading. The library is closed.')

main()    
    
        
