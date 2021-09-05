#Capter 4 - Best Practices of Class Design
#4.1 Designing for inheritance and polymorphism - 50 xp

#4.2 Polymorphic methods
#To design classes effectively, you need to understand how inheritance and polymorphism work together.
#In this exercise, you have three classes - one parent and two children - each of which has a talk() method. 
#Analyze the following code:
from chapter_3 import Employee


class Parent:
    def talk(self):
        print("Parent talking!")     

class Child(Parent):
    def talk(self):
        print("Child talking!")          

class TalkativeChild(Parent):
    def talk(self):
        print("TalkativeChild talking!")
        Parent.talk(self)


p, c, tc = Parent(), Child(), TalkativeChild()

for obj in (p, c, tc):
    obj.talk()

## Correct answer
#Parent talking!
#Child talking!
#Talkative Child talking!
#Parent talking!

#4.3 Square and rectangle
#The classic example of a problem that violates the Liskov Substitution Principle is the Circle-Ellipse problem, 
# sometimes called the Square-Rectangle problem. By all means, it seems like you should be able to define a class 
# Rectangle, with attributes h and w (for height and width), and then define a class Square that 
# inherits from the Rectangle. After all, a square "is-a" rectangle!
# Unfortunately, this intuition doesn't apply to object-oriented design.

#4.3.1 Exercise
# Define a Rectangle class
class Rectangle:
    def __init__(self, h, w):
        self.h = h
        self.w = w
# Define a Square class
class Square(Rectangle):
    def __init__(self, w):
        Rectangle.__init__(self, w,w)
#4.3.2 Exercise - Option 3 
# The 4x4 Square object would no longer be a square if we assign 7 to h.

#4.3.3 Exercise
#The classic example of a problem that violates the Liskov Substitution Principle 
# is the Circle-Ellipse problem, sometimes called the Square-Rectangle problem.

# A Square inherited from a Rectangle will always have both the h and w attributes, 
# but we can't allow them to change independently of each other.
# Define methods set_h() and set_w() in Rectangle, each accepting one parameter and setting h and w.

class Rectangle:
    def __init__(self, w,h):
      self.w, self.h = w,h

# Define set_h to set h      
    def set_h(self, h):
      self.h = h
      
# Define set_w to set w          
    def set_w(self, w):
      self.w = w

# Define methods set_h() and set_w() in Square, each accepting one parameter, and 
# setting both h and w to that parameter in both methods.    
      
class Square(Rectangle):
    def __init__(self, w):
      self.w, self.h = w, w 

# Define set_h to set w and h
    def set_h(self, h):
      self.h = h
      self.w = h

# Define set_w to set w and h      
    def set_w(self, w):
      self.w = w
      self.h = w 
#4.3.4
#How does using these setter methods violate Liskov Substitution principle?

# Correct Answer - Option 2
# Each of the setter methods of Square change both h and w attributes, 
# while setter methods of Rectangle change only one attribute at a time, 
# so the Square objects cannot be substituted for Rectangle into programs 
# that rely on one attribute staying constant.

#4.4 Attribute naming conventions

#4.4.1 _name
#A helper method that checks validity of an attribute's value but isn't considered as part of class's
# public interface 

#4.4.2 __name
#A 'version' that stores current version of the class and shouldn't be passed to the child classes, 
# who will have their own versions. 

#4.4.3 __name__
# A method that is run whenever the object is printed.

#4.5 Using internal attributes
#In this exercise, you'll return to the BetterDate class of Chapter 2.
# Your date class is better because it will use the sensible convention of having exactly 
# 30 days in each month. You decide to add a method that checks the validity of the date, 
# but you don't want to make it a part of BetterDate's public interface.

# Add class attributes for max number of days and months
class BetterDate:
    _MAX_DAYS = 30
    _MAX_MONTHS = 12
    
    def __init__(self, year, month, day):
        self.year, self.month, self.day = year, month, day
        
    @classmethod
    def from_str(cls, datestr):
        year, month, day = map(int, datestr.split("-"))
        return cls(year, month, day)
    
    # Add _is_valid() checking day and month values
    def _is_valid(self):
        return self.month <= BetterDate._MAX_MONTHS and self.day <= BetterDate._MAX_DAYS
    
bd1 = BetterDate(2020, 4, 30)
print(bd1._is_valid())

bd2 = BetterDate(2020, 6, 45)
print(bd2._is_valid())

# 4.6 Properties
#Example
# Use "protected" attribute with leading _ to store data 
class Employer:
    def __init__(self, name, new_salary):
        self._salary = new_salary
#Use @property on a method whose name is exactly the name of the restricted attribute;
# return the internal attribute
    @property
    def salary(self):
        return self._salary
# Use @attr.setter on a method attr() that will be on obj.attr = value
    @salary.setter
    def salary(self, new_salary):
        if new_salary < 0:
            raise ValueError("Invalid Salary")
        self._salary = new_salary
emp = Employer("Bold Batdorj", 5000000)
emp.salary

emp.salary = 100000
emp.salary

emp.salary = -1000000

#4.7 What do properties do?
#Which of the following statements is NOT TRUE about properties?
#This statement is indeed not true! Properties control only one specific attribute
#  that they're attached to. There are ways to prevent creating new attributes,
#  but doing so would go against the "we're all adults here" principle.

# 4.8 Create and set properties 
#In this exercise, you'll create a balance property for a Customer class 
# - a better, more controlled version of the balance attribute that you worked with before.
class Customer:
    def __init__(self, name, new_bal):
        self.name = name
        if new_bal < 0:
           raise ValueError("Invalid balance!")
        self._balance = new_bal  

    # Add a decorated balance() method returning _balance        
    @property
    def balance(self):
        return self._balance

    # Add a setter balance() method
    @balance.setter
    def balance(self, new_bal):
        # Validate the parameter value
        if new_bal < 0:
           raise ValueError("Invalid balance!")
        self._balance = new_bal
        print("Setter method called")

# Create a Customer        
cust = Customer("Belinda Lutz", 2000)

# Assign 3000 to the balance property
cust.balance = 3000

# Print the balance property
print(cust.balance)

#4.9 Read-only properties
#The LoggedDF class from Chapter 2 was an extension of the pandas 
# DataFrame class that had an additional created_at attribute that stored the timestamp
# when the DataFrame was created, so that the user could see how out-of-date the data is.

#4.9.1 
import pandas as pd
from datetime import datetime

# LoggedDF class definition from Chapter 2
class LoggedDF(pd.DataFrame):
    def __init__(self, *args, **kwargs):
        pd.DataFrame.__init__(self, *args, **kwargs)
        self.created_at = datetime.today()

    def to_csv(self, *args, **kwargs):
        temp = self.copy()
        temp["created_at"] = self.created_at
        pd.DataFrame.to_csv(temp, *args, **kwargs)   

# Instantiate a LoggedDF called ldf
ldf = LoggedDF({"col1": [1,2], "col2":[3,4]}) 

# Assign a new value to ldf's created_at attribute and print
ldf.created_at = '2035-07-13'
print(ldf.created_at)

#4.9.2 
import pandas as pd
from datetime import datetime

# MODIFY the class to use _created_at instead of created_at
class LoggedDF(pd.DataFrame):
    def __init__(self, *args, **kwargs):
        pd.DataFrame.__init__(self, *args, **kwargs)
        self._created_at = datetime.today()
    
    def to_csv(self, *args, **kwargs):
        temp = self.copy()
        temp["created_at"] = self._created_at
        pd.DataFrame.to_csv(temp, *args, **kwargs)   
    
    # Add a read-only property: _created_at
    @property  
    def created_at(self):
        return self._created_at

# Instantiate a LoggedDF called ldf
ldf = LoggedDF({"col1": [1,2], "col2":[3,4]}) 

#4.9.3 What happens when you assign '2035-07-13' to ldf.created_at?

# ANSWER: #AttributeError: can't set attribute
#An AttributeError is thrown since ldf.created_at is read-only.
