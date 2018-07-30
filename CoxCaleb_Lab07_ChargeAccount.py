#This program reads a file into a list and then allows the user to search for a
#charge account and checks if the number is valid or not

def main():
    #Open file
    infile = open('charge_accounts.txt', 'r')

    #Reads contents of the file into a list
    numbers = infile.readlines()

    #Close file
    infile.close()

    #Guard
    index = 0

    print("This is the list of the charge_accounts.txt file.\n")
    
    #Convert each element to an int
    while index < len(numbers):
        numbers[index] = int(numbers[index])
        index += 1
        
    #Display list
    print(numbers, '\n')

    try:
        #User enters charge account and search for card in list
        search = int(input('Enter a charge account number: '))
        
    #Handle any errors
    except Exception as err:
        print(err)
        
    else:
        #Determine if charge account is in list
        if search in numbers:
            print('The number is valid.')
        else:
            print('The number is invalid.')
            
main()
