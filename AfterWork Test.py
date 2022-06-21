percentOff1 = 0.10
percentOff2 = 0.15
percentOff3 = 0.20
print('Please enter your Work hours, and do Note That this is an estimate.')
workHours = int(input())


while workHours > 1:
  print ('Before, We Start, please input your Pay per hour')
  payHours = float(input())
  yourPay = workHours * payHours
  print('Please press The Co-ordinated button Start from 1-3, starting from %10-%20 Respectifully.')
  print('1 = %10')
  print('2 = %15')
  print('3 = %20')
  break






if input() == '2':
    print ('Please keep in Mind that this is not the TRUE amount they will take off, They will Take either a bit more or a bit less.')
    taxDeduct2 = yourPay * percentOff2
    netCheck2 = yourPay - taxDeduct2
    netCheck2 = str(netCheck2)
    print('')
    print ('Your Total pay will be ' + netCheck2 + ' For this paycheck')


if input() == '1':
    print ('Please keep in Mind that this is not the TRUE amount they will take off, They will Take either a bit more or a bit less.')
    taxDeduct1 = yourPay * percentOff1
    netCheck1 = yourPay - taxDeduct1
    netCheck1 = str(netCheck1)
    print('')
    print ('Your Total pay will be ' + netCheck1 + ' For this paycheck.')



if input() == '3':
    print ('Please keep in Mind that this is not the TRUE amount they will take off, They will Take either a bit more or a bit less.')
    taxDeduct3 = yourPay * percentOff3
    netCheck3 = yourPay - taxDeduct3
    netCheck3 = str(netCheck3)
    print('')
    print ('Your Total pay will be ' + netCheck3 + ' For this paycheck')

