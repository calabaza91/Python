#This is a class to be used for getting and storing employee information

class Employee:
    def __init__(self, name, idNum, dept, title):
        self.__name = str(name)
        self.__idNum = str(idNum)
        self.__dept = str(dept)
        self.__title = str(title)

    def set_Name(self, name):
        self.__name = str(name)
        
    def set_IdNum(self, idNum):
        self.__idNum = str(idNum)
        
    def set_Dept(self, dept):
        self.__dept = str(dept)

    def set_title(self, title):
        self.__title = str(title)

    def get_Name(self):
        return self.__name

    def get_IdNum(self):
        return self.__idNum

    def get_Dept(self):
        return self.__dept
    
    def get_Title(self):
        return self.__title

    def __str__(self):

        result ='\n---------------------' +\
                 '\nID Number: ' + self.get_IdNum() +\
                 '\nName: ' + self.get_Name() +\
                 '\nDepartment: ' + self.get_Dept() + \
                 '\nJob Title: ' + self.get_Title() + \
                 '\n---------------------'
                

        return result
                 
