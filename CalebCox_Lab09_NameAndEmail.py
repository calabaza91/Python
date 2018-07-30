#Import pickle
import pickle


#Menu global variables
SEARCH = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5


def main():


    end_of_file = False

    try:
        #Open file for reading
        in_file = open('file.dat','rb')
        contacts = pickle.load(in_file)
        display_data(contacts)
    except EOFError:
        end_of_file = True
        #Close file to be opened for writing
        in_file.close()
    
    #Guard
    choice = 0

    #Use menu choices
    while choice != QUIT:
        try:
            #Call choice from menu
            choice = display_menu()

            #Tell User what they chose
            print("You have selected ", choice,'.\n',sep='')
            
            if choice == SEARCH:
            #Search contacts
                #print('Search for a contact.')
                search(contacts)
            elif choice == ADD:
                #Add
                add_contact(contacts)
 #               
            elif choice == CHANGE:
                #Change 
                change_contact(contacts)
                
            elif choice == DELETE:
                #Delete
                delete_contact(contacts)

                
            elif choice == QUIT:
                #Close and save file
                out_file =  open('file.dat', 'wb')
                pickle.dump(contacts,out_file)
                out_file.close()

                print('Goodbye.')
                
                
        #Catch exceptions
        except Exception as Err:
            print(Err, '\n Try again.')


            

#Display menu function
def display_menu():
    #Print menu
    print("\n----------------------\n"
          "        MENU          \n"
          "----------------------\n"
          "1) Search Contacts\n"
          "2) Add Contact\n"
          "3) Change Email\n"
          "4) Delete Contact\n"
          "5) Quit\n"
          "----------------------\n")
    choice = int(input('Please choose an option: '))
    return choice

    

#Search function
def search(contacts):
    print(contacts)
    name = str(input('Please enter a name: '))
    print(contacts.get(name, 'Sorry, that name was not found.'))

    
    
#Add function
def add_contact(contacts):
    print('Add a contact.')
    
    more =  'y'
    #Add multiple contacts
    while more == 'y':
        
        name = str(input('Please enter a name: '))
        email = str(input('Please enter an email: '))
        if name not in contacts:
            contacts[name] = email
            more = str(input('Add another? (y/n)'))
        else:
            print('That contact already exists.')
            more = str(input('Want to try adding another? (y/n)'))

            
        
#Change function
def change_contact(contacts):
    print('Change a contact\'s info.')
    name = str(input('Please enter a name: '))
    if name in contacts:
        email = str(input('Enter an email: '))
        #Change email
        contacts[name] = email
    else:
        print("Sorry that name was not found.")


        
#Delete function
def delete_contact(contacts):
    print('Delete a contact.')
    name = str(input('Please enter a name: '))
    if name in contacts:
        #Delete contact
        del contacts[name]
    else:
        print("Sorry that name was not found.")


       

    
#Pickle In function
def display_data(person):

    print('    Name//Email   ')
    print('------------------')
    #Display Names and Emails
    for key in person:
        print(key, "//", person[key], sep='')
    print('------------------')

  
main()


