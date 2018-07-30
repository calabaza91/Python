#This program translates a sentence into Pig Latin


def main():
    
    print("Let's have some Pig Latin fun!")
    
    #Get sentence from user and convert to string
    sentence = str(input("Type your sentence here: "))

    #Strip period off the end for better translation for last word
    noPeriod = sentence.rstrip('.')

    #Upper case string for legibility
    upper = noPeriod.upper()

    #Split sentence into words
    words = upper.split()

    #Iterate through list of words
    for index in words:

        #Get each word minus the first letter in that word
        slicedWord = index[1:]
        
        #Get first letter in each word
        firstLetter = index[0]
        
        #Display new sentence in Pig Latin
        print(slicedWord + firstLetter + 'AY', end=' ')

main()
