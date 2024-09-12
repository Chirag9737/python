


#  opps

#class
#object
#constructer
#attibutes
#methods
#static merhods
#absrtacthion
# encapsulathin
# polymorphism
# inharitance
# del key words  
class MyClass:
    def __init__(self, name,age):
        self.name = name
        self.age = age
      
      
        print(type(self))
      
      
      
      
      
    def Hello (self):
        print("hello",self.name)
        
    
      
    




# object (intance)
m = MyClass("chirag",17)
print(m.name,m.age)
m.Hello()







class car :
    color = "grey"
    brand = 'volvo'
    
car1 = car()
print(car1.brand)


# attributes

# class.attri & object.attri

# methods




class studet :
    def __init__(self, name, marks):
      self.name = name
      self.marks = marks
     
     
    # @staticmethod 
    def ave_marks(self):
        sum = 0
        for val in self.marks:
            sum += val
        print(f"hi {self.name} your avg score in : {sum/3}")
      

s1 = studet("chirag",[82,55,70])
# print(s1.name , s1.meth)
print(s1.ave_marks())



class account :
    def __init__(self, bal, acc):
        self.bal = bal
        self.account_no = acc
      
    def debit_ammount(self,debited_ammount):
        self.bal -= debited_ammount
        print (self.get_ammount())
        return debited_ammount
    
    def credit_ammount(self,credited_ammount):
        self.bal += credited_ammount
        print (self.get_ammount())
        return credited_ammount
       
 
    
    def get_ammount(self):
        
        return self.bal
    
    
    
acc1 = account(18000,32156498)
print(acc1.debit_ammount(359))
print(acc1.credit_ammount(19638))
    
    # inheritence
    
class Car:
    @staticmethod
    def start():
        print("car started .....")

    @staticmethod
    def stop():
        print("car stopped.....")
        
        
class toyotacar(Car):
    def __init__(self, brand):
        self.brand = brand
        

class fortuner (toyotacar):
    def __init__(self, fule_type):
        self.fule_type = fule_type
        
car1 = fortuner("Hibrid")
# crintar2 = toyotacar("prius")


print(car1)
car1.start()
      


class a:
    A = ("welcome to class a ")

class b:
   B = ("welcome to class b ")
    
class c(a,b):
    C = ("welcome to class c")

c1 = c()
print(c1.A)
print(c1.B)
print(c1.C)
print(c1)










