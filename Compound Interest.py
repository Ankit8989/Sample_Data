age= [25]
principal=1000
year=1
irate=8

result=principal*(pow((1+irate/100),year))

print("Enter value",result)



#For age>60 && age<60
#branchinf If statement

age=65
principal=1000
year=1


if(age>60):
    irate=8
else:
    irate=7

result=principal*(pow((1+irate/100),year))

print("Enter value",result)



#Same function but se command elif#
age=60
principal=1000
noofyear=1
if age>60:
    irate=8
elif age==60: #elif is else if
    irate=7.5
else:
    irate=7
    ma=principal*(1+irate/100)**noofyear

    print(ma)



#6,5,8,3,4