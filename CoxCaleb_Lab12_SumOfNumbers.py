#Sum of numbers program

def main():
    print('Let\'s do some summation!')
    #Get integer
    n = int(input('Enter a number: '))
    #Pass integer 'n' as argument for sum_of_num function
    sum_of_num(n)

#Summation function
    #n == integer given
    #acc == accumulator set to 1
def sum_of_num(n, acc = 1):

    #Product of Accumulator multiplied by 'n' integer divided by itself
    digit = int(acc*(n)/n)

    #Total sum of numbers formula
    total = int(n*(n+1)/2)

    #If Accumulator passes 'n' integer, print total
    if n < acc:
        print('--------')
        print('Total: ',total)

    #Print each digit leading up to and including 'n' integer
    else:
        print(digit)
        #Resursion for summation function
        sum_of_num(n, acc+1)
    
main()
