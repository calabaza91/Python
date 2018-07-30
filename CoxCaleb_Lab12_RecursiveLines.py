#This program makes a triangle
def main():
    print('Let\'s make a triangle!')
    
    #Get integer for base of triangle
    n = int(input('Enter a number: '))
    
    #Pass integer 'n' argument into triangle function  
    triangle(n)

#Triangle function has base parameter and
#a constant starting position parameter of 1
def triangle(base, start = 1):
    
    #Prints last tier
    if base == start:
        print(start * '*')
        
    else:
        #Prints top to second to last tier
        print(start * '*')
        
        #Recursion of triangle function
        #Passes base again and accumulates the start position
        triangle(base, start+1)

main()
