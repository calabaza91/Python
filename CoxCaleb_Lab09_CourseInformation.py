#This program creates dictionaries for course information, lets the user search for a course
#and displays search result if course exists 

def main():

    #Create dictionary for room numbers
    roomNum = {'CS101': 3004,
               'CS102': 4501,
               'CS103': 6755,
               'NT110': 1244,
               'CM241': 1411}

    #Create dictionary for instructors
    instructor = {'CS101': 'Haynes',
               'CS102': 'Alvarado',
               'CS103': 'Rich',
               'NT110': 'Burke',
               'CM241': 'Lee'}

    #Create dictionary for class times
    time = {'CS101': '8:00 a.m.',
            'CS102': '9:00 a.m.',
            'CS103': '10:00 a.m.',
            'NT110': '11:00 a.m.',
            'CM241': '1:00 a.m.'}

    #Search for course
    search = input('Search for a course: ')

    #Check all dictionaries for course and display information if course exists
    if search in roomNum and instructor and time:
        print('Room #:',roomNum[search],'| Intructor:', instructor[search], "| Meeting Time:", time[search])
    else:
        print('Sorry,',search, 'was not found.')
        
main()
