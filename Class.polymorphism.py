#polymorphism

def add(a,b):

    print(a+b)


add(10,20)
add('ten','count')

#############################


class Duck:
    def fly(self):
        print("Duck flying")

class Airplane:
    def fly(self):
        print("Airplane flyig")

class Whale:
    def swim(self):
        print("Whale Swimming")

def lift_off(entity):
    entity.fly()

duck=Duck()
airplane=Airplane()
whale=Whale()

lift_off(duck)       #Prints Duck flying
lift_off(airplane)    #prints Airplane flyting
#lift_off(whale)       # Throws the error 'Whale' object has no attributes 'fly'

