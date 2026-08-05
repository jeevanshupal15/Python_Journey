                                                                       # OOPs
# To map with real world scenarios, we can use the concept of Object-Oriented Programming (OOP) to model real-world entities and their interactions.
# OOP allows us to create classes that represent objects, encapsulate data, and define behaviors through methods. 
# This approach helps in organizing code, promoting reusability, and making it easier to maintain.
                                                         # Class & Object
# 1. class : class is a blueprint or template for creating objects. 
class Student:  # class
    name = "Jeevanshu pal"
    course = "bca"
s1 = Student()  # object
print(s1.name)  # accessing attribute of object
print(s1.name)  # accessing attribute of object
print(s1.course)

# init function :  special method in Python classes that is automatically called when an object of the class is created.    
class Student:
    collage_name = "IAMR"  # class attribute
    def __init__(self):  #default constructor
        pass
    def __init__(self , name, age): #parametrized constructor
        self.name = name #self.name = object attribute > class attribute , both have same value
        self.age = age
    def welcome(self): # method
        print("Welcome student ",self.name,self.age)
 # static method : dont use self parameter (work at class level)
    @staticmethod #decoretor
    def hello(): # method
        print("Welcome student in static method")    
s1 = Student("pavitra",17,) 
print(s1.name,s1.age,s1.collage_name)    
s2 = Student("abhinav",19)     
print(s2.name,s2.age,s2.collage_name)  
s1.welcome() 
s2.welcome() 
s1.hello() 

                                                                   # Abstraction
 # hiding the internal implementation details and showing only the necessary features to user.
class car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
    def start(self):
        self.clutch = True
        self.acc = True
    print("car is started")
car1 = car()
car1.start()
                                                                      #encapsulation 
# wrapping up of data and methods into a single unit called class. 
                                                                        # practice
# Q1 lets practice classs that takes name and marks of  3 subject as argument in constructor. then create a method to calculate average marks.
class Student:
    def __init__(self,name,mark):
        self.name = name
        self.mark = mark
    def get_avg(self):
        sum = 0
        for val in self.mark:
            sum += val
        print("hii",self.name,"your avg score is ",sum/3)
s1 = Student("hulk",[45,88,78])
s1.get_avg()
# Q2 create a account class with 2 attributes name and account no. create a method to debit and credit money from account. 
# also create a method to display balance.
class accounts:
    def __init__(self,bal,acc):
        self.balance = bal
        self.account = acc
    def debit(self, amount):
        self.balance -= amount
        print("your amount is debited",amount)
        print("your account balance is ",self.balance)
    def credit(self, amount):
        self.balance += amount
        print("your amount is credited",amount)
        print("your account balance is ",self.balance)
    def display_balance(self):
        return self.balance

acc1 = accounts(100000,123456)
acc1.debit(5000)
acc1.credit(10000)
acc1.display_balance()
acc1.debit(50000)



