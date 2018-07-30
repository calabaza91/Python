#Make an Employee base class

class Employee:
    
    #Initialize data attributes with name and number values
    def __init__(self, name, number, title):
        self.__name = str(name)
        self.__number = str(number)
        self.__title = str(title)

    #Mutator methods
    def set_name(self, name):
        self.__name = str(name)

    def set_num(self, number):
        self.__number = str(number)

    def set_title(self, title):
        self.__title = str(title)
        
    #Accessor methods
    def get_name(self):
        return self.__name
    
    def get_num(self):
        return self.__number
    
    def get_title(self):
        return self.__title

    def __str__(self):
        result ='\n---------------------' +\
                 '\nID Number: ' + self.get_num() +\
                 '\nName: ' + self.get_name() +\
                 '\nJob Title: ' + self.get_title()               

        return result

    
#Make a Produciton Worker subclass
    
class ProductionWorker(Employee):

  #  title = "Production Worker"
    #The __init__ method accepts arguments fot the worker's shift and pay rate
    def __init__(self, name, number, shift, payrate):
        #Call base class's __init__ method and pass required arguments
        Employee.__init__(self, name, number,'Production Worker')

        #Initialize the __shift  and __pay_rate attributes
        self.__shift = str(shift)
        self.__payrate = str(payrate)

    #Mutator methods for shift and pay rate
    def set_shift(self, shift):
        self.__shift = str(shift)

    def set_pay(self, payrate):
        self.__payrate = str(payrate)

    #Accessor methods for shift and pay rate
    def get_shift(self):
        #Reassign 1 to Day and 2 to Night 
        if self.__shift == '1':
            return 'Day'
        elif self.__shift == '2':
            return 'Night'

    def get_pay(self):
        return self.__payrate

    def modify_emp(self):
        self.set_shift(input('Enter new shift (1 or 2): '))
        self.set_pay(input('Enter new hourly pay rate: '))

    def __str__(self):

        return Employee.__str__(self) + \
               '\nShift: '+ self.get_shift() + \
               '\nPay Rate: $'+ self.get_pay() + \
               '\n---------------------'

        
        

class ShiftSupervisor(Employee):

#    title = "Shift Supervisor"
    def __init__(self, name, number, salary, bonus):

        Employee.__init__(self, name, number, 'Shift Supervisor')
        self.__salary = str(salary)
        self.__bonus = str(bonus)

    def set_salary(self, salary):
        self.__salary = str(salary)

    def set_bonus(self, bonus):
        self.__bonus = str(bonus)

    def get_salary(self):
        return self.__salary
    def get_bonus(self):
        return self.__bonus

    def modify_emp(self):
        self.set_salary(input('Enter new salary: '))
        self.set_bonus(input('Enter new bonus: '))
        
    def __str__(self):

        return Employee.__str__(self) + \
               '\nSalary: $'+ self.get_salary() + \
               '\nBonus: $'+ self.get_bonus() + \
               '\n---------------------'
