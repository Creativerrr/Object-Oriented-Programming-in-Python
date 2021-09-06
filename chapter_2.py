#2 Inheritance and Polymorphism

#2.1 Class-level attributes
#Class attributes store data that is shared among all the class instances. 
# They are assigned values in the class body, and are referred to using the ClassName. 
# syntax rather than self. syntax when used in methods.

#2.1.1 Create a Player class
class Player:
    MAX_POSITION = 10
    
    def __init__(self):
      self.position = 0

# Print Player.MAX_POSITION  
print(Player.MAX_POSITION)   

# Create a player p and print its MAX_POSITITON
p = Player()
print(p.MAX_POSITION)

#2.1.2
class Player:
    MAX_POSITION = 10
    
    def __init__(self):
        self.position = 0

    # Add a move() method with steps parameter     
    def move(self, steps):
        if self.position + steps < Player.MAX_POSITION:
           self.position = self.position + steps 
        else:
           self.position = Player.MAX_POSITION
    
    # This method provides a rudimentary visualization in the console    
    def draw(self):
        drawing = "-" * self.position + "|" +"-"*(Player.MAX_POSITION - self.position)
        print(drawing)

p = Player(); p.draw()
p.move(4); p.draw()
p.move(5); p.draw()
p.move(3); p.draw()

#2.2 Alternative constructors
#Python allows you to define class methods as well, using the @classmethod decorator and a special
# first argument cls. The main use of class methods is defining methods that return an instance of the class,
# but aren't using the same code as __init__().
#2.2.1
class BetterDate:
    # Constructor
    def __init__(self, year, month, day):
      # Recall that Python allows multiple variable assignments in one line
      self.year, self.month, self.day = year, month, day
    
    # Define a class method from_str
    @classmethod
    def from_str(cls, datestr):
         # Split the string at "-" and  convert each part to integer
        parts = datestr.split("-")
        year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
        # Return the class instance
        return cls(year, month, day)
        
bd = BetterDate.from_str('2020-04-30')   
print(bd.year)
print(bd.month)
print(bd.day)

#2.2.2
#For compatibility, you also want to be able to convert a datetime object into a BetterDate object.
# # import datetime from datetime
from datetime import datetime

class BetterDate:
    def __init__(self, year, month, day):
      self.year, self.month, self.day = year, month, day
      
    @classmethod
    def from_str(cls, datestr):
        year, month, day = map(int, datestr.split("-"))
        return cls(year, month, day)
      
    # Define a class method from_datetime accepting a datetime object
    @classmethod
    def from_datetime(cls, dateobj):
      year, month, day = dateobj.year, dateobj.month, dateobj.day
      return cls(year, month, day) 


# You should be able to run the code below with no errors: 
today = datetime.today()     
bd = BetterDate.from_datetime(today)   
print(bd.year)
print(bd.month)
print(bd.day)

#2.3 Understanding inheritance
#Inheritance is a powerful tool of object-oriented languages that allows you to customize 
#functionality of existing classes without having to re-implement methods from scratch.

class Counter:
    def __init__(self, count):
       self.count = count

    def add_counts(self, n):
       self.count += n

class Indexer(Counter):
   pass

#True options 

#Inheritance represents in-a relationship
#If ind is an Indexer() object, than isinstance(ind, Counter) will return TRUE
#Running ind = indexer() will cause an error. 
#Class indexer is inherited from Counter.

#False

#If ind is an indexer() object, then running ind.add_counts(5) will cause an error.
#Inheritance can be used to add some of the parts of one class to another.
#Every in Counter object is an Indexer object. 

#2.4 Create a subclass

#2.4.1
class Employee:
  MIN_SALARY = 30000    

  def __init__(self, name, salary=MIN_SALARY):
      self.name = name
      if salary >= Employee.MIN_SALARY:
        self.salary = salary
      else:
        self.salary = Employee.MIN_SALARY
        
  def give_raise(self, amount):
      self.salary += amount
        
# Define a new class Manager inheriting from Employee
class Manager(Employee):
  pass

# Define a Manager object
mng = Manager("Debbie Lashko", 86500)

# Print mng's name
print(mng.name)

#2.4.2
class Employee:
  MIN_SALARY = 30000    

  def __init__(self, name, salary=MIN_SALARY):
      self.name = name
      if salary >= Employee.MIN_SALARY:
        self.salary = salary
      else:
        self.salary = Employee.MIN_SALARY
        
  def give_raise(self, amount):
    self.salary += amount

        
# MODIFY Manager class and add a display method
class Manager(Employee):
  def display(self):
    print("Manager ", self.name)


mng = Manager("Debbie Lashko", 86500)
print(mng.name)

# Call mng.display()
mng.display()

#2.5 Method inheritance
# Inheritance is powerful because it allows us to reuse and customize code without rewriting existing code.
# By calling methods of the parent class within the child class, we reuse all the code in those methods, 
# making our code concise and manageable.

#2.5.1
class Employee:
    def __init__(self, name, salary=30000):
        self.name = name
        self.salary = salary

    def give_raise(self, amount):
        self.salary += amount

        
class Manager(Employee):
  # Add a constructor 
    def __init__(self, name, salary=50000, project=None):

        # Call the parent's constructor   
        Employee.__init__(self, name, salary)

        # Assign project attribute
        self.project = project  

  
    def display(self):
        print("Manager ", self.name)
 
 # 2.5.2
 class Employee:
    def __init__(self, name, salary=30000):
        self.name = name
        self.salary = salary

    def give_raise(self, amount):
        self.salary += amount

        
class Manager(Employee):
    def display(self):
        print("Manager ", self.name)

    def __init__(self, name, salary=50000, project=None):
        Employee.__init__(self, name, salary)
        self.project = project

    # Add a give_raise method
    def give_raise(self, amount, bonus=1.05):
        new_amount = amount * bonus
        Employee.give_raise(self, new_amount)
    
    
mngr = Manager("Ashta Dunbar", 78500)
mngr.give_raise(1000)
print(mngr.salary)
mngr.give_raise(2000, bonus=1.03)
print(mngr.salary)

#2.6 Inheritance of class attributes

#2.6.1
class Racer(Player):
    MAX_SPEED = 5
    
p = Player()
r = Racer()

print("p.MAX_SPEED = ", p.MAX_SPEED)
print("r.MAX_SPEED = ", r.MAX_SPEED)

print("p.MAX_POSITION = ", p.MAX_POSITION)
print("r.MAX_POSITION = ", r.MAX_POSITION)

#2.6.2 Question
#Which of the following statements about inheritance of class attributes is correct?

#Answer
#Class attributes CAN be inherited, and the value of class attributes CAN be overwritten in the child class

#2.7 Customizing a DataFrame
# In this exercise, you will implement a small LoggedDF class that inherits from a regular pandas DataFrame 
# but has a created_at attribute storing the timestamp. You will then augment the standard to_csv() method
# to always include a column storing the creation date.

#2.7.1
# Import pandas as pd
import pandas as pd

# Define LoggedDF inherited from pd.DataFrame and add the constructor
class LoggedDF(pd.DataFrame):
  
  def __init__(self, *args, **kwargs):
    pd.DataFrame.__init__(self, *args, **kwargs)
    self.created_at = datetime.today()
    
    
ldf = LoggedDF({"col1": [1,2], "col2": [3,4]})
print(ldf.values)
print(ldf.created_at)

#2.7.2
# Import pandas as pd
import pandas as pd

# Define LoggedDF inherited from pd.DataFrame and add the constructor
class LoggedDF(pd.DataFrame):
  
  def __init__(self, *args, **kwargs):
    pd.DataFrame.__init__(self, *args, **kwargs)
    self.created_at = datetime.today()
    
  def to_csv(self, *args, **kwargs):
    # Copy self to a temporary DataFrame
    temp = self.copy()
    
    # Create a new column filled with self.created_at
    temp["created_at"] = self.created_at
    
    # Call pd.DataFrame.to_csv on temp, passing in *args and **kwargs
    pd.DataFrame.to_csv(temp, *args, **kwargs)