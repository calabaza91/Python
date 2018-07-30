#This program creates a Golf.txt file of golfers' names and scores
#then reads the records from the file

def main():

    outfile = open('golf.txt', 'w')

    print('Welcome to the Annual Springfolk Golf Club Tournament!',
          "\nPlease enter the contestants' name and score.\n")
    playerNum = 0
    
    more = 'y'

    #Loop to create list of golfers and scores
    while more == 'y':
        playerNum += 1
        golfer = input('Enter Name: ')

        score = int(input('Enter Score: '))
        
        outfile.write('-------------------------------------\n')
        outfile.write('PLAYER NUMBER ' + str(playerNum) + '\n')
        outfile.write('-------------------------------------\n')
        outfile.write('Name: ' + golfer + '\n')
        outfile.write('Score: ' + str(score) + '\n\n')

        
        more = input("Any more? (y/n) ")

    print('Data has been saved to file.')

    outfile.close()

    #Open File for Reading

    infile = open('golf.txt', 'r')

    print('Reading file. The Library is officially open.')

    for line in infile:

        line = line.rstrip('\n')

        print(line)
    
    infile.close()
    
main()
