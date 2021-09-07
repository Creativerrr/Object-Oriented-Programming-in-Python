#1 OOP termininology

#1.1 Classify the cards into the correct buckets. Are the statements true or false?

#True
#Attributes encode the state of an object and are represented by variables.
#Methods encode behavior of an object and are represented by functions.
#Encapsulation is a software design practice of the bundling the data and methods that operate on that data.

#False
#Object is an abstract template describing the general states and behaviors.
#Object and class are different terms describing  the same concept.
#A programming language can be either object-orented or procedural, but not both.
#.columns is an example of method of a DataFrame object. 

#1.2 Exploring object interface
#The best way to learn how to write object-oriented code is to study the design of existing classes.

#1.2.1 What class does the mystery object have?
#ANSWER  __main__.Employee

#1.2.2
# Print the mystery employee's name
print(mystery.name)

# Print the mystery employee's salary
print(mystery.salary)

#1.2.3 
# Print the mystery employee's name
print(mystery.name)

# Print the mystery employee's salary
print(mystery.salary)

# Give the mystery employee a raise of $2500
mystery.give_raise(2500)

# Print the salary again
print(mystery.salary)

#1.3 Understanding class definitions

def set_count(self, n):
    mc.set_count(5)
    mc.count = mc.count + 1
    mc=MyCounter()
    
#1.4 Create your first class

#1.4.1
# Create an empty class Employee
class Employee:
    pass

# Create an object emp of class Employee 
emp = Employee()

#1.4.2
# Include a set_name method
class Employee:
  
  def set_name(self, new_name):
    self.name = new_name
  
# Create an object emp of class Employee  
emp = Employee()

# Use set_name() on emp to set the name of emp to 'Korel Rossi'
emp.set_name("Korel Rossi")

# Print the name of emp
print(emp.name)

#1.4.3
class Employee:
  
  def set_name(self, new_name):
    self.name = new_name
  
  # Add set_salary() method
  def set_salary(self, new_salary):
    self.salary = new_salary
  
  
# Create an object emp of class Employee  
emp = Employee()

# Use set_name to set the name of emp to 'Korel Rossi'
emp.set_name('Korel Rossi')

# Set the salary of emp to 50000
emp.set_salary(50000)

#1.5 Using attributes in class definition

#1.5.1 
class Employee:
    def set_name(self, new_name):
        self.name = new_name

    def set_salary(self, new_salary):
        self.salary = new_salary 
  
emp = Employee()
emp.set_name('Korel Rossi')
emp.set_salary(50000)

# Print the salary attribute of emp
print(emp.salary)

# Increase salary of emp by 1500
emp.salary = emp.salary + 1500

# Print the salary attribute of emp again
print(emp.salary)

#1.5.2
lass Employee:
    def set_name(self, new_name):
        self.name = new_name

    def set_salary(self, new_salary):
        self.salary = new_salary 

    # Add a give_raise() method with raise amount as a parameter
    def give_raise(self, amount):
        self.salary = self.salary + amount

emp = Employee()
emp.set_name('Korel Rossi')
emp.set_salary(50000)

print(emp.salary)
emp.give_raise(1500)
print(emp.salary)

1.5.3
class Employee:
    def set_name(self, new_name):
        self.name = new_name

    def set_salary(self, new_salary):
        self.salary = new_salary 

    def give_raise(self, amount):
        self.salary = self.salary + amount

    # Add monthly_salary method that returns 1/12th of salary attribute
    def monthly_salary(self):
        return self.salary / 12
    
emp = Employee()
emp.set_name('Korel Rossi')
emp.set_salary(50000)

# Get monthly salary of emp and assign to mon_sal
mon_sal = emp.monthly_salary()

# Print mon_sal
print(mon_sal)

#1.6
#Correct use of __init__
#Python allows you to run custom code - for example, initializing attributes - any time an object is created: you just need to define a special method called __init__(). Use this exercise to check your understanding of __init__() mechanics!

#Which of the code blocks will NOT return an error when run?

#ANSWER Option 2 
class Counter: 
    def __init__(self, count, name):
        self.count = 5
        self.name = name
c = Counter(0, "My counter")
print(c.count)

#1.7 Add a class constructor

#1.7.1
class Employee:
    # Create __init__() method
    def __init__ (self, name, salary=0):
        # Create the name and salary attributes
        self.name = name
        self.salary = salary
    
    # From the previous lesson
    def give_raise(self, amount):
        self.salary += amount

    def monthly_salary(self):
        return self.salary/12
        
emp = Employee("Korel Rossi")
print(emp.name)
print(emp.salary)     

#1.7.2
class Employee:
    
    def __init__(self, name, salary=0):
        self.name = name
        # Modify code below to check if salary is positive
        if salary >= 0:
          self.salary = salary
        else:
          self.salary = 0
          print("Invalid salary!")
        
   
   # ...Other methods omitted for brevity ... 
      
emp = Employee("Korel Rossi", -1000)
print(emp.name)
print(emp.salary)

#1.7.3 
# Import datetime from datetime
from datetime import datetime

class Employee:
    
    def __init__(self, name, salary=0):
        self.name = name
        if salary > 0:
          self.salary = salary
        else:
          self.salary = 0
          print("Invalid salary!")
          
        # Add the hire_date attribute and set it to today's date
        self.hire_date = datetime.today()
        
   # ...Other methods omitted for brevity ...
      
emp = Employee("Korel Rossi")
print(emp.name)
print(emp.hire_date)

#1.8 Write a class from scratch

# Write the class Point as outlined in the instructions
import numpy as np

class Point:

    def __init__(self, x=0.0, y=0.0): 
        self.x = x
        self.y = y
    def distance_to_origin(self): 
        return np.sqrt(self.x**2 + self.y**2)
   
    def reflect(self, axis):
        if axis == "x":
            self.y = -self.y
        elif axis == "y":
            self.x = -self.x
        else:
            print("The argument axis only accepts values 'x' and 'y'!")

pt = Point(x=3.0)
pt.reflect("y")
print((pt.x, pt.y))
pt.y = 4.0
print(pt.distance_to_origin())