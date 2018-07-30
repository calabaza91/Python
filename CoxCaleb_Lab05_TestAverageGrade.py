#This program calculates an average of 5 tests and displays the letter grade

#Main function
def main():

    print("Let's calculate your average score!\n")
    #Get test scores and pass them through Determine Grade function
    test1 = int(input("Enter test score: "))
    determine_grade(test1)

    test2 = int(input("Enter test score: "))
    determine_grade(test2)

    test3 = int(input("Enter test score: "))
    determine_grade(test3)

    test4 = int(input("Enter test score: "))
    determine_grade(test4)

    test5 = int(input("Enter test score: "))
    determine_grade(test5)

    #Pass test scores through Calc Average function
    calc_average(test1,test2,test3,test4,test5)

#Calc Average function
def calc_average(test1,test2,test3,test4,test5):
    #Add all scores and divide by 5
    average = (test1 + test2 + test3 + test4 + test5)/5
    #Display average
    print("Your average is: ", average,".", sep='')
    #Pass average through Determine Grade function
    determine_grade(average)

#Determine Grade function
def determine_grade(grade):

    #Check scores and display letter grade and message
    if grade < 60:
        print("This recieves an F. Don't forget to study!!\n")
    elif 60 <= grade <= 69:
        print("This recieves a D. You can do better! Go see a tutor.\n")
    elif 70 <= grade <= 79:
        print("This recieves a C. Don't settle for mediocrity!\n")
    elif 80 <= grade <= 89:
        print("This recieves a B. Good job! Study a little more!\n")
    elif 90 <= grade <= 100:
        print("This recieves an A. Excellent! You're a star, baby!\n")

#Call Main
main()
