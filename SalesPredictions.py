#Sales Predictions

sales = float(input('Enter total amount of annual sales: '))

profit = sales * 0.23

print('The expected profit for $', format(sales, ',.2f'),
      ' sales is $', format(profit, ',.2f'),'.', sep='')


