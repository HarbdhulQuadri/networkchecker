#DEFINING THE PROVIDERS  
mtn = [703,706,803,806,810,813,814,816,903,906]
glo =[705,805,807,811,815,905]
airtel=[701,708,802,808,812,902,907,901]
etisalat = [809,817,818,908,909]

#Accepting Input
number = input('ínput your number')

#selecting the first 3 digit to determine the network provider
provider = int(number[1:4])

#checking the  provider
if provider in mtn:
    print("MTN  number")
elif provider in glo:
    print("GLO number")
elif provider in airtel:
    print("Airtel number")
elif provider in etisalat:
    print("(9mobile )")
else:
    print('number not found')
            