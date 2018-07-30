# Dempnstrates the ProductionWorker class

import employee

def main():
    print('===========================')
    print('Enter the employee\'s data.')
    name = input('Employee name: ')
    number = int(input('Employee number: '))
    shift = int(input('Shift 1 or 2: '))
    payrate = float(input('Rate of pay: $'))
    print('===========================\n')

    emp = employee.ProductionWorker(name, number, title, shift, payrate)

    print('Name: ', emp.get_name(), sep='')
    print('Employee #: ', emp.get_num(), sep='')
    print('Shift: ', emp.get_shift(), sep='')
    print('Pay Rate: $', format(emp.get_pay(), '.2f'), sep='')

main()
