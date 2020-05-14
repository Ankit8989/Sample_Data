def addlist(lst1,lst2):
    n=len(lst1)
    lst3=[]
    for i in range(0,n):
        s=lst1[i]+lst2[i]
        lst3.append(s)
    return lst3

mylist1=[60,70,50,80]
mylist2=[50,60,70,80]
print(addlist(mylist1,mylist2))