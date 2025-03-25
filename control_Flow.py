# if 10 > 0:
#     print("Inside if")
# else:
#     print("Inside else")

#Electricity bill example
unit=float(input("Enter the unit (KWh) consumed : "))
rate=float(input("Enter the rate per unit (KWh) : "))
if unit > 100 :
    extra = unit - 100
    bill = ( 100 * rate ) + (extra * 1.5 * rate)
    print(f" The bill for {unit}  KWh  at {rate} INR is {bill} INR")
else:
    bill = unit * rate
    print(f" The bill for {unit}  KWh  at {rate} INR is {bill} INR")