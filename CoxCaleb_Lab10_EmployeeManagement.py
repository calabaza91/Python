import Cox_employee
import pickle

#Global constants for menu
SEARCH = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 6
PRINT = 5

#Global constant for file
FILENAME = 'file.dat'

def main():

    #Load Employees
    my_emps = load_emps()
    #Guard
    choice = 0
    #Iterate through Menu
    while choice != QUIT:
        try:
            #Get User choice
            choice = display_menu()
            #Process choice
            if choice == PRINT:
                print_emp(my_emps)
            elif choice == SEARCH:
                #Call Search function
                search(my_emps)
            elif choice == ADD:
                #Call Add function
                add_emp(my_emps)
            elif choice == CHANGE:
                #Call Change function
                change_emp(my_emps)
            elif choice == DELETE:
                #Call Delete function
                delete_emp(my_emps)
        #Catch invalid inputs
        except Exception as err:
            print(err, "\n Try Again.")
        
            
    #Save employee dictionary to file
    save_emps(my_emps)
    
#Load Function
def load_emps():
    #Read pickle file (if there is any)
    try:
        infile = open(FILENAME, 'rb')

        emp_dict = pickle.load(infile)

        infile.close()
    #If file does not exist, create empty dictionary
    except IOError:
        emp_dict = {}
    #Return either pickled file or empty dictionary
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



def print_emp(my_emps):
    print("\n-------------------")
    for emp in my_emps:
        print("Employee ID #", my_emps[emp].get_IdNum(), sep='')
        print("-------------------")
        print("Name:", my_emps[emp].get_Name())
        print("Department:", my_emps[emp].get_Dept())
        print("Job Title:", my_emps[emp].get_Title())
        print("\n-------------------")



#Search Function
def search(my_emps):
    print('Search for an employee.')
    print(my_emps)
    
    #Get ID to look up
    idNum = str(input('Enter an employee ID Number: '))
    
    #Look it up in dictionary
    print(my_emps.get(idNum, 'Sorry, employee not found.'))



#Add Function
def add_emp(my_emps):
    print('Add an employee.')
    
    #Get Employee info
    idNum = str(input('Enter employee id: '))
    name = str(input('Enter employee name: '))
    dept = str(input('Enter employee department: '))
    title = str(input('Enter employee job title: '))
    
    #Create Employee obj named entry
    entry = Cox_employee.Employee(name, idNum, dept, title)

    #If ID doesn't exist, add to dictionary as
    #key with entry obj as the associated value

    if idNum not in my_emps:
        my_emps[idNum] = entry
        print('The entry has been added to the file.')
    else:
        print('That employee already exists in the file.')

    return entry


    
#Change Function
def change_emp(my_emps):
    print("Change employee data.")

    #Get ID to look up
    idNum = str(input('Enter employee ID Number: '))

    #If ID is in dictionary, get new info and update employee info
    if idNum in my_emps:
        #Get new ID:
        name = str(input('Enter new employee Name: '))

        #Get new Dept:
        dept = str(input('Enter new Department: '))

        #Get new job title
        title = str(input('Enter new Job Title: '))

        #Create employee obj named entry
        entry = Cox_employee.Employee(name, idNum, dept, title)

        #Update employee data
        my_emps[idNum] = entry

        print('Information Updated.')
    #If ID is not in dictionary, ID does not exist  
    else:
        print('That name was not found.')


        
#Delete Function
def delete_emp(my_emps):
    print('Delete employee entry.')

    #Get ID
    idNum = str(input('Enter employee ID Number: '))

    #If ID in dictionary, delete it
    if idNum in my_emps:
        del my_emps[idNum]
        print('Employee entry deleted.')
    else:
        print('Employee was not found.')



#Save Function
def save_emps(my_emps):

    #Open file to be written on
    outfile = open(FILENAME, 'wb')
    #Pickle dictionary and save it
    pickle.dump(my_emps, outfile)
    #Close file
    outfile.close()


main()
    
