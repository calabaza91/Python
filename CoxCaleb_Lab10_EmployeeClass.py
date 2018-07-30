#This program creates a list of three employees using a class

import Cox_employee

def main():
    #Get list of Employees
    employees = make_list()

    #Display data in list

    print('Here is the list of employees:')
    display_list(employees)

def make_list():

    #Make empty list
    emp_list = []

    #Get Susan data
    name1 = 'Susan Meyers'
    idNum1 = '47899'
    dept1 = 'Accounting'
    title1 = 'Vice President'

    emp1 = Cox_employee.Employee(name1, idNum1, dept1, title1)

    emp_list.append(emp1)
    
    #Get Mark data
    name2 = 'Mark Jones'
    idNum2 = '39119'
    dept2 = 'IT'
    title2 = 'Programmer'

    emp2 = Cox_employee.Employee(name2, idNum2, dept2, title2)

    emp_list.append(emp2)

    #Get Joy data
    name3 = 'Joy Rogers'
    idNum3 = '81774'
    dept3 = 'Manufacturing'
    title3 = 'Engineer'

    emp3 = Cox_employee.Employee(name3, idNum3, dept3, title3)

    emp_list.append(emp3)

    return emp_list


def display_list(emp_list):
    for item in emp_list:
        print("\n-------------------")
        print("Name: ", item.get_Name())
        print("ID Number: ", item.get_IdNum())
        print("Department: ", item.get_Dept())
        print("Job Title: ", item.get_Title())
        print("-------------------")

main()
