#This program creates simple math quizez until the user chooses to stop

#imports math and random 
import math
import random


#Main Function
def main():

    #control variable
    keep_going = 'y'

    #Loop quiz for as long as user wants
    while keep_going == 'y':
    
        #Shows result function containing all other functions
        showResult()
        #Lets user choose to continue or not
        keep_going=input("Would you like more practice? (y/n) ")

#Display Qusetion function
def displayQuestion():
    
    #get random number 1
    num1 = random.randint(1,1000)
    #get random number 2
    num2 = random.randint(1,1000)
    #display question
    print("\t ", num1, "\n\t+", num2)

    #Returns num1 and num2 to be used elsewhere
    return num1, num2

#Get Answer Function
def getAnswer():
    #Get answer from user
    answer = int(input("\nEnter the sum: "))
    #Returns answer to be used elsewhere
    return answer

#Show Result function
def showResult():
    #Get num1 and num2 values by calling Display Question function
    num1, num2 = displayQuestion()

    #Add two values together
    result = num1 + num2

    #Get user answer by calling Get Answer function
    answer = getAnswer()
    
    #Check answer to see if it equals sum of values
    if answer == result:
        #If correct, let them know!
        print('Correct! Great job!')
    else:
        #Else, let them know. :/
        print('Wrong answer. Try again!')

        #Let user try until they get answer correct
        while answer != result:
            answer = getAnswer()
            #Displays message if answer is incorrect
            if answer != result:
                print("Nope, still wrong. Try again!")
        #Displays message if answer is correct               
        print("Good job!\n")
        
#Call main function
main()
