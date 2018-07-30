#This program takes a client’s age and classifies it as an infant, child, teenager or adult

#Get age from client
age = int(input('How old are you? '))

#Determine age classification
    #If age is at least 1, then client is an infant
if age <= 1:
    print('You are an intelligent infant.')
    #If age greater than 1 but less than 13, then client is a child
elif 1 < age < 13:
    print('You are a child. Enjoy it while it lasts!')
    #If age is at least 13 but less than 20, then client is a teenager
elif 13 <= age < 20:
    print('You are a teenager. Make good choices!')
    #If age at least 20, then client is an adult
elif 20 <= age:
    print('You are an adult. Don\'t take things too seriously.')

