# Classes and Objects
# name=input("Enter Student Name: ")
# age=int(input("Enter Student's Age: "))
# std=int(input("Enter Student's Standard: "))
# class Student:
#     n1=name
#     a1=age
#     std1=std
# s1=Student()
# print("Name of the Student is ",s1.n1)
# print("Age of the Student is ",s1.a1)
# print("Student is studing in Std ",s1.std1)


# ======================================================================================================================================
# CLass and Object using Constructor using (__init__) method
# name=input("Enter Student Name: ")
# age=int(input("Enter Student's Age: "))
# std=int(input("Enter Student's Standard: "))
# class Student:
#      ////default contructors
#     def __init__(self):
#         print("adding new student in database......")
#     //// parameterized contructors
#     def __init__(self,name,age,std):
#         self.name=name
#         self.age=age
#         self.std=std    
# s1=Student(name,age,std)
# print("Name of the Student is ",s1.name)
# print("Age of the Student is ",s1.age)
# print("Student is studing in Std ",s1.std)

# ======================================================================================================================================
# Class and Object attribute
# class Student:
#     name="Kunal Chavan" #
#     age=25              #    All 3 attributes are class attributes
#     std=12              #
#     #  ////default contructors
#     def __init__(self):
#         print("adding new student in database......")
#     # //// parameterized contructors
#     def __init__(self,name,age,std):
#         self.name=name   #
#         self.age=age     #   All 3 attributes are Object attributes
#         self.std=std     #   NOte : Obj attributes > Class attributes
# s1=Student("Milind Chavan",24,15)
# print("Name of the Student is ",s1.name)
# print("Age of the Student is ",s1.age)
# print("Student is studing in Std ",s1.std)

# =======================================================================================================================================
#  Methods in Class and object
# name=input("Enter Student Name: ")
# age=int(input("Enter Student's Age: "))
# marks=int(input("Enter Student's Marks: "))
# class Student:
#     #  ////default contructors
#     def __init__(self):
#         print("adding new student in database......")
#     # //// parameterized contructors
#     def __init__(self,name,age,marks):
#         self.name=name
#         self.age=age
#         self.marks=marks
#     def greet(self):
#         print("Welcome to our esteemed College ",s1.name)
#     def get_age(self):
#         print("Age of the Student is ",s1.age)
#     def get_marks(self):
#         print("Marks of the student is ",s1.marks)
# s1=Student(name,age,marks)
# s1.greet()
# s1.get_age()
# s1.get_marks()

# ======================================================================================================================================
# Create Student class that takes name & marks of 3 subjects as arguments in contructor.
# then create a method to print the average
# class Student:
#     def __init__(self, name1, marks1, name2, marks2, name3, marks3):
#         self.subject1 = name1
#         self.marks1 = marks1
#         self.subject2 = name2
#         self.marks2 = marks2
#         self.subject3 = name3
#         self.marks3 = marks3
#     def avg(self):
#         total = self.marks1 + self.marks2 + self.marks3
#         average = total / 3
#         print(f"Average of {self.subject1}, {self.subject2}, {self.subject3} is: {average}")
# # Taking input
# s1_name = input("Enter Subject1 Name: ")
# s1_marks = int(input("Enter Marks of Subject1: "))
# s2_name = input("Enter Subject2 Name: ")
# s2_marks = int(input("Enter Marks of Subject2: "))
# s3_name = input("Enter Subject3 Name: ")
# s3_marks = int(input("Enter Marks of Subject3: "))
# # Creating object
# s5 = Student(s1_name, s1_marks, s2_name, s2_marks, s3_name, s3_marks)
# # Calling average method
# s5.avg()

# ======================================================================================================================================
# Static Method
# Methods that dont use self parameter(works only at class level)
# type "@staticmethod to use static method" also called decorator
# name=input("Enter Student Name: ")
# age=int(input("Enter Student's Age: "))
# std=int(input("Enter Student's Standard: "))
# class Student:
#     n1=name
#     a1=age
#     std1=std

#     @staticmethod
#     def college():
#         print("ABC College")

# s1=Student()
# s1.college()
# print("Name of the Student is ",s1.n1)
# print("Age of the Student is ",s1.a1)
# print("Student is studing in Std ",s1.std1)
# decorators allow us to wrap another function in order to extent the 
# behaviour of the wrapped function, without permanently modifying it

# ===========================================================================================================================================
# Abstraction means hiding the implementation details of a class and only 
# showing the essential features to the user.
# class car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False
#     def start(self):
#         self.clutch = True
#         self.acc = True
#         print("Car Started .....")
# car1=car()
# car1.start()

# =======================================================================================================================================
# Encapsulation means wrapping data and function into a single unit(object)
# it means class including all attributes(data) and methods or functions
# class Student:
#     def get_marks(self,Sub1,Sub2,Sub3):   //Methods
        # sum = Sub1 + Sub2 + Sub3  //
#         avg = sum/3               //attributes
#         print("Average of all 3 subject's is : ",avg)
# s1=Student()
# s1.get_marks(91,92,95)

# =======================================================================================================================================
# Create account class with 2 attributes - balance & account no.
# Create methods for debit, credit & printing the balance
# class Account:
#     def __init__(self,bal,acc,):
#         self.balance=bal
#         self.account_no=acc
#     def debit(self,deb_amount):
#         self.balance -= deb_amount
#         print("Rs.", deb_amount ," was debited")
#         print("Total balance =", self.get_balance())
#     def credit(self,cred_amount):
#         self.balance += cred_amount
#         print("Rs.", cred_amount , "was credited")
#         print("Total balance =", self.get_balance())
#     def get_balance(self):
#         return self.balance  
# acc1=Account(10000,"IOB222332")
# acc1.debit(2000)
# acc1.credit(5000)

# =========================================================================================================================================
# (del) keyword : used to delete object properties or objects itself.
#  del.name or del s1
# class Student:
#     def __init__(self, name):
#         self.name = name 
# s1=Student("Milind Chavan")
# print(s1.name)

# ========================================================================================================================================
# Private(like) attributes & methods
# Private attributes & methods are meant to be used only within the class and are not
# accessible from outside the class
# class Account:
#     def __init__(self, acc_no,acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass
#     def reset_pass(self):
#         return self.__acc_pass
# acc1= Account("IOB12334",23234)
# print("Account NO is: ",acc1.acc_no)
# print("Account Password is :",acc1.reset_pass())
# print("Account password is : ",acc1.__acc_pass)
#                            OR
# class Person:
#     __name = "anonymous"
#     def __hello(self):
#         print("Hello person")
#     def welcome(self):
#         self.__hello()
# p1 = Person()
# p1.welcome()

# ======================================================================================================================================

# Inheritance 
#  When one class( child / derived ) derives the properties & methods of another class (parent / base).
# Example:
# class car:
#     @staticmethod
#     def start():
#         print("Car Started....")

#     @staticmethod
#     def stop():
#         print("Car Stopped....")

# class Toyota(car):
#     def __init__(self,name,color):
#         self.name=name
#         self.color=color
# car1 = Toyota("Fortuner","black")
# car2 = Toyota("Prius","red")
# car1.start()
# car2.stop()
# print(car1.color)
# print(car2.color)
# =======================================================================================================================================
# _______________________________________________Single Inheritance_______________________________________________________________________
# class car:
#     @staticmethod
#     def start():
#         print("Car Started....")

#     @staticmethod
#     def stop():
#         print("Car Stopped....")

# class Toyota(car):
#     def __init__(self,name,color):
#         self.name=name
#         self.color=color
# car1 = Toyota("Fortuner","black")
# car2 = Toyota("Prius","red")
# car1.start()
# car2.stop()
# print(car1.color)
# print(car2.color)

# ==========================================================================================================================================
# ______________________________________________Multilevel Inheritance___________________________________________________________________

# class Car:
#     @staticmethod
#     def start():
#         print("Car Started....")

#     @staticmethod
#     def stop():
#         print("Car Stopped....")

# class ToyotaCar(Car):
#     def __init__(self,brand):
#         self.brand = brand

# class Fortuner(ToyotaCar):
#     def __init__(self, type,color):
#         self.type = type
#         self.color= color

# class Prius(ToyotaCar):
#     def __init__(self, type,color):
#         self.type = type
#         self.color=color

# car1 = Fortuner("Diesel","Blue")
# car1.start()
# print(car1.color)
# car2 = Prius("Electric","Red")
# car2.stop()
# print(car2.color)

# ============================================================================================================================================
# ______________________________________________Multiple Inheritance___________________________________________________________________
#  In Multiple Inheritance their will be more than one base / parent class
# class A:
#     varA="Welcome to class A"
# class B:
#     varB="Welcome to class B"

# class C(A,B):
#     varC="Welcome to class C"

# c1=C()
# print(c1.varC)
# print(c1.varB)
# print(c1.varA)

# ============================================================================================================================================
# _______________________________________Super Method__________________________________________________________________________________________
# super() method is used to access methods of the parent class.
# class Car:
#     def __init__(self, type):
#         self.type = type

#     @staticmethod
#     def start():
#         print("Car Started....")

#     @staticmethod
#     def stop():
#         print("Car Stopped....")

# class ToyotaCar(Car):
#     def __init__(self,name,type):
#         super().__init__(type)
#         self.name = name
#         super().start()

# car1=ToyotaCar("Fortuner","Petrol")
# print(car1.name)
# print(car1.type)
# =========================================================================================================================================
# ____________________________________class methods()__ (it is also called class decorator)__________________________________________________________________________________
# In Python, the classmethod() function is used to define a method that is bound to the class and not the instance of the class. 
# This means that it can be called on the class itself rather than on instances of the class.
# Class methods are useful when you need to work with the class itself rather than any particular instance of it.
# class Person:
#         name="anonymous"
#         # def changeName(obj,name):
#         #         obj.__class__.name = "Rahul"

#         @classmethod
#         def changeName(cls, name):
#                 cls.name = name
# P1= Person()
# P1.changeName("rahul")
# print(P1.name)
# print(Person.name)
# =========================================================================================================================================
# ____________________________________Property decorator____________________________________________________________________________________   
# We use @property decorator on any method in class to used the method as a property
# The @property decorator lets you call a method like an attribute.
# It’s used when you want to get (or later set) a value using dot notation, 
# but with the power of a method behind it (e.g., calculation, logic, etc.). 
# Basic Example Without @property:
# Suppose you’re building a system for real estate, and each house has a base price and a tax. 
# You want to calculate the final price including tax, but you don’t want users to have to call a method like get_final_price().

# ___________________(Without @property:)_________________________
# class House:
#     def __init__(self, base_price, tax_rate):
#         self.base_price = base_price
#         self.tax_rate = tax_rate

#     def final_price(self):
#         return self.base_price + (self.base_price * self.tax_rate)

# h = House(100000, 0.1)
# print(h.final_price())  # method call

# _______________________(With @property:)__________________________
# class House:
#     def __init__(self, base_price, tax_rate):
#         self.base_price = base_price
#         self.tax_rate = tax_rate

#     @property
#     def final_price(self):
#         return self.base_price + (self.base_price * self.tax_rate)

# h = House(100000, 0.1)
# print(h.final_price)  # looks like an attribute!


# Why use it?
# You hide complex logic behind a simple interface.
# You can change method implementation later without changing how users use the class.3=]

# ===================================================================================================================================================
#____________________________________________Python @property decorator____________________________________________________________________-
# @property decorator is a built-in decorator in Python which is helpful in defining the properties effortlessly 
# without manually calling the inbuilt function property(). Which is used to return the property attributes of a class 
# from the stated getter, setter and deleter as parameters. Now, lets see some examples to illustrate the use of 
# @property decorator in Python: Example 1: 
# Python program to illustrate the use of
# @property decorator
# Defining class
# class Portal:
#     # Defining __init__ method
#     def __init__(self):
#         self.__name =''
#     # Using @property decorator
#     @property
#     # Getter method
#     def name(self):
#         return self.__name
#     # Setter method
#     @name.setter
#     def name(self, val):
#         self.__name = va
#     # Deleter method
#     @name.deleter
#     def name(self):
#        del self.__name
# # Creating object
# p = Portal()
# # Setting name
# p.name = 'GeeksforGeeks'
# # Prints name
# print (p.name)
# # Deletes name
# del p.name
# # As name is deleted above this 
# # will throw an error
# print (p.name)
# Here, the @property decorator is used to define the property name in the class Portal, 
# that has three methods(getter, setter, and deleter) with similar names i.e, name(), 
# but they have different number of parameters. Where, the method name(self) labeled with @property is a getter method, 
# name(self, val) is a setter method as it is used to set the value of the attribute __name and so its labeled with @name.setter. 
# Lastly, the method labeled with @name.deleter is a deleter method which can delete the assigned value by the setter method. 
# However, deleter is invoked with the help of a keyword del.

# =========================================================================================================================================
# _______________________________________________Polymorphism________________________________________________________________________________
# Operator Overloading: When the same operator is allowed to have different meaning according to the content.
# print(1 + 2) #3
# print("Milind" + "Chavan") # MilindChavan #concatenate
# print([1,2,3] + [4,5,6]) #Merge = [1,2,3,4,5,6]
# 
# 
# _____________________Operator Overloading on Complex no.____________________
# class addComplex:
#         def __init__(self, real , img):
#                 self.real=real
#                 self.img=img
        
#         def shownum(self):
#                 print(self.real,"i +",self.img," j")
        
#         def __add__(self,num2):
#                 newReal=self.real + num2.real
#                 newImg=self.img + num2.img
#                 return addComplex(newReal,newImg)

# num1=addComplex(1,3)
# num1.shownum()

# num2=addComplex(5,7)
# num2.shownum()

# num3=num1 + num2
# num3.shownum()
# ==========================================================================================================================================
# define a circle class to create a circle with radius r using the constructor
# define an Area() method of the class which calculate the area of circle.
# define a perimeter() method of the clss which calculate the perimeter of circle:
class Circle:
        def __init__(self, r):
                self.r = r
        
        def Area(self):
                return (22/7) * self.r ** 2
        
        def perimeter(self):
                return 2 * (22/7) * self.r
        
cal=Circle(7)
print(cal.Area())
print(cal.perimeter())