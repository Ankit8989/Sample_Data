
#Scenerio 1
try:
    a=1
    b=0
    print(a/b)
    print(a)

except:
    print("you divided by 0")

#Scenario 2

try:
    a=1
    b=0
    print(a)
    print(a/b)
    #print('10'+10)
except TypeError:
    print("You added values of incompatible types")
except ZeroDivisionError:
    print("You divided by 0")


#Scenario 3

try:
    print('10'+10)
    print(a/b)
    print(a)
except(TypeError, ZeroDivisionError):
    print("Invalid Input")


#Scenario 4

try:

    print(1/0)
except ZeroDivisionError:
   print("You divided by 0")
finally:
    print("This will print no matter what.")

#Scenario 5

try:
    f=open('log.txt','W')
    #print('10'+10
    print(1/0)
    print('test')
except Exception as e:
        f.write('Error: %s'%(e))
finally:
       f.close()

############################################

#Scenario 6

import pandas as pd
data1=pd.read_csv("Book1.csv")
n=len(data1)
lstQnt=[]
for i in range(0,n):
    try:
        f=open('log.txt','a')
        saleamt=int(data1.loc[i,"SaleAmount"])
        prc=int(data1.loc[i,"Price"])
        qnt=saleamt/prc
        lstQnt.append(qnt)
    except Exception as e:
        f.write('Error : %s - %s'% (data1.loc[i,"Stock"],e))
        lstQnt.append(e)
    finally:
        f.close()

data1['Qnt']=lstQnt
data1.to_csv("Book1.csv",index=False)