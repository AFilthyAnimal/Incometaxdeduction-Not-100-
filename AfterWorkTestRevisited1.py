percentOff1 = 0.10
percentOff2 = 0.15
percentOff3 = 0.20

print ('Hello, To Start please input your hours to the closest whole number.')
print
workHours = int(input())

print ('Next, Please stat your pay per hour.')

payHours = float(input())

yourPay = workHours * payHours
print ('If you have Statutory hours, Please input them here.')

statHours = int(input())

while statHours > 1:
        statPay =  payHours * 1.5
        totStat = statHours * statPay
        break
while statHours < 1:
        print ("I understand, sometimes Work ain't it")
        break

statHours = str(statHours)
print ('Alright, Now Choose the Closest Variable that the Income tax is decucted from 1-3')

print ('Option 1. 0.10')
print ('Option 2. 0.15')
print ('Option 3. 0.20')

if int(input()) == 1:
        print ('please keep in mind this is not totally Accurate, and does not include RRSP, or anything additonal.')
        totalDeduct1 = yourPay * percentOff1
        netCheck1 = yourPay - totalDeduct1
        netCheck1 = str(netCheck1)
        print('')
        print ('Your Estimated Net Pay will be ' + netCheck1 + ' With a Statutory pay of ' + statHours )



