age1=[30,65,60,45,80]
principal1=[1000,4000,3000,4000,2000]
noofyear=1
irate=8

totalAmt=0
approved=[]
i=0

while(totalAmt<10000):
    ma3=principal1[i]*(1+irate/100)**noofyear
    totalAmt=totalAmt+ma3
    approved.append("Yes")
    i=i+1

print(approved)



age3=[45,62,66,55,70]
principal1=1200
noofyear=1
lst2=[]

totalAmt=0
approved=[]


i=0

while(totalAmt<3000):

    if age3[i]>=60:

        irate=8
    else:

        irate=7

    ma3=principal1* (1+irate/100)**noofyear
    totalAmt=totalAmt+ma3
    i=i+1
    approved.append("Yes")


print(approved)





