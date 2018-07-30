import employee
import pickle

#Global Filename constant
FILE = 'file.dat'

#Global constants for menu
SEARCH = 1
ADD = 2
CHANGE = 3
DELETE = 4
PRINT = 5
QUIT = 6


def main():
    #Load file
    emps = load_emps()

    choice = 0
   
    #Iterate through Menu
    while choice != QUIT:
        try:
            #Get User choice
            choice = display_menu()
            #Process choice
            if choice == PRINT:
                print_emps(emps)
            elif choice == SEARCH:
                #Call Search function
                search_emps(emps)
            elif choice == ADD:
                #Call Add function
                add_emp(emps)
            elif choice == CHANGE:
                #Call Change function
                change_emp(emps)
            elif choice == DELETE:
                #Call Delete function
                del_emp(emps)
        #Catch invalid inputs
        except Exception as err:
            print(err, "\n Try Again.")
    
  
    #Save to file
    save_emps(emps)



#Load Function
def load_emps():
    #Exception handler to catch IOErrors
    try:
        #Open file for reading, if any
        infile =  open(FILE, 'rb')
        #Pickle in to load file
        emp_dict = pickle.load(infile)
        #Close file
        infile.close()
    #Catch IOErrors
    except IOError:
    #If file/dictionary doesn't exist, create a new one
        emp_dict = {}
    #If file does exist, return pickled file or empty dictionary
    return emp_dict


#Menu Function
def display_menu():
    #Print menu
    print("\n=====================\n"
          "         MENU          \n"
          "=====================\n"
          "1) Search Employees\n"
          "2) Add Employee\n"
          "3) Change Employee\n"
          "4) Delete Employee\n"
          "5) Print List\n"
          "6) Quit\n"
          "=====================\n")
    
    #Get choice
    choice = int(input('Please choose an option: '))

    #Validate choice
    while choice < SEARCH or choice > QUIT:
        choice = int(input('Please choose a valid option: '))
        
    #Return user choice
    return choice



#Print list of all employees
def print_emps(emps):

    if len(emps) == 0:
        print('There is nothing here.')
    else:
        for key in emps:
            print(emps[key], '\n')


#Search employee dictionary
def search_emps(emps):
    print('Search for an employee.')
    print(emps)

    
    #Get ID to look up
    num = input('Enter an employee ID Number: ')
    
    #Look it up in dictionary
    print(emps.get(num, 'Sorry, employee not found.'))





#Add employees
def add_emp(emps):
    
    print('Add an employee.')
    num = input('Num: ')
    
    if num not in emps:
        name = input('Name: ')
    
    
        print('Choose a title:',\
              '\n1) Production Worker',\
              '\n2) Shift Supervisor')
        title = int(input('Select 1 or 2: '))

        if title == 1:
            shift = int(input('Shift 1 or 2: '))
            payrate = input('Pay: ')

            emps[num] = employee.ProductionWorker(name, num, shift, payrate)

            
        elif title == 2:
            salary = input('Salary: ')
            bonus = input('Bonus: ')

            emps[num] = employee.ShiftSupervisor(name, num, salary, bonus)

        print('Employee successfully added to file.')
    else:
        print('Employee already exists')


#Delete employee
def del_emp(emps):

    print('Delete employee entry.')

    num = input('Enter employee ID Number: ')

    if num in emps:
        del emps[num]
        print('Employee entry deleted.')
    else:
        print('Employee was not found.')


#Change employee info
def change_emp(emps):

    num = input('Enter employee ID Number: ')

    if num in emps:

        emps[num] = modify_emp(emps[num])
        print('Employee information updated.')

    else:
        print('Employee not found.')


#Modify employee based on title
def modify_emp(emp):

    print(emp, '\n')

    emp.modify_emp()

    return emp


#Save Function
def save_emps(my_emps):
    #Open file for writting
    outfile = open(FILE, 'wb')
    #Pickle dictionary and save it
    pickle.dump(my_emps, outfile)
    #Close file
    outfile.close()
#-------------------------

main()
