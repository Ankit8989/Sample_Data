class Calc1:
    def __init__(self):
        self.price=1000

    def discount1(self):
        val1=self.price*.1
        return val1

class Calc2(Calc1):
    def __init__(self):
        super(). __init__()
    def discount2(self):
        val2=super().discount1()  #Accessign parent class
        val3=val2*.5
        return val3

    def discount3(self):
        val4=self.price*.2      #Accessing parent attribute
        return val4

c1=Calc1()
c1.price=100
c2=Calc2()
c2.price=500
d1=c1.discount1()
d2=c2.discount2()
d3=c2.discount3()

print("Discount1",d1)
print("Discount2",d2)
print("Discount3",d3)