#HRD1916190
#Answer1
#Section a

import  statistics
product=('prod1','prod2','prod3','prod4')
price=[200,500,100,400]
cost=[160,440,90,300]
profit=[]

for i in range(0,len(price)):

    diff=price[i]-cost[i]

    profit.append(diff)



print(profit)
    d1 = zip(product,profit)  # Zip converting into one
    d2 = dict(d1)  # Converting into dictinory
    print(d2)

#Section b
#Total profit of all products

n=len(profit)
total=0
for i in range (0,n):

    total=total+profit[i]

print("Total profit of all products:",total)

#Mean of the price
x=statistics.mean(price)
print(x)

m=len(price)

sum=0


for i in range(0,m):
    sum=sum+price[i]

mean=sum/m

print("Mean",mean)


#max of the price

m=len(price)

Max=max(price)

print("Max of the price",Max)


#Answer 3

#Section a

def Salesman(avg_sales,):




    if (avg_sales>=600):

        print("Above Avg")

    elif(avg_sales<=400):

        print("Below Avg")

sales=500
days=("day1","day2")
output=Salesman(sales,days)

print(output)
print("Days2",)


#Section  b

try:
    a=5
    b=6
    print(a)
    print(a/b)

except TypeError:
    print("Incompatible types")



#Section d

code=100
sub='Python'

print("Subject info:",code,sub)
print(sub.upper())


#Section e

Dept=("Marketing","Finance","operations","HR")
no_of_staff=[100,50,80,60]

combine=zip(Dept,no_of_staff)
dict1=dict(combine)

print(dict1)



l=len(dict1)
for i in range(0,l):
    if(i==1):

print(dict1)


units = [600, 400]
days = ("day1", "day2")
n=len(units)
def salesman(u,d):
    for i in range(0,n):
        if(units[i]>500):
            print("Above Avg")

        else:

            print("Below Avg")

combine=zip(days,units)
dict1=dict(combine)

print(dict1[1])




aa=salesman(days,units)

print(aa)





