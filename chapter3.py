#Exeptions
#Example 1
class BalanceExeptions(Exception): pass
class Customer:
    def __init__(self, name, balance):
        if balance < 0:
            raise BalanceError("Balance has to be non-negative")
        else:
            self.name, self.balance = name, balance


try:
    cust = Customer("Larry Torres", -100)
except:
    cust = Customer("Larry Torres", 0)

#Catching Exeptions
# MODIFY the function to catch exceptions
def invert_at_index(x, ind):
  try:
    return 1/x[ind]
  except ZeroDivisionError:
    print("Cannot divide by zero!")
  except IndexError:
    print("Index out of range!")
 
a = [5,6,0,7]

# Works okay
print(invert_at_index(a, 1))

# Potential ZeroDivisionError
print(invert_at_index(a, 2))

# Potential IndexError
print(invert_at_index(a, 5))

#Custom exceptions
class SalaryError(ValueError):pass
class BonusErroe(SalaryError):pass

class Employee:
    MIN_SALARY = 30000
    MAX_BONUS = 5000

    def __init__(self, name, salary = 30000):
        self.name = name
        if salary < Employee.MIN_SALARY:
            raise SalaryError("Salary is too low!")
        self.salary = salary
    
    # Rewrite using exceptions
    def give_bonus(self, amount):
        if amount > Employee.MAX_BONUS:
            print("Bonus amount is too high!")
        elif self.salary + amount < Employee.MIN_SALARY:
            print("The salary after bonus is too low!")
        else:
            self.salary += amount
#Handling exception hierarchies

emp = Employee("Katze Rik", salary=50000)
try:
  emp.give_bonus(7000)
except SalaryError:
  print("SalaryError caught!")

try:
  emp.give_bonus(7000)
except BonusError:
  print("BonusError caught!")

try:
  emp.give_bonus(-100000)
except SalaryError:
  print("SalaryError caught again!")

try:
  emp.give_bonus(-100000)
except BonusError:
  print("BonusError caught again!")  

#example code exceptions 
#Select the statement which is TRUE about the order of except blocks:
#It's better to list the except blocks in the increasing order of specificity, i.e. 
# children before parents, otherwise the child exception will be called in the parent except block.
#code1
emp = Employee("Katze Rik",\
                    50000)
try:
  emp.give_bonus(7000)
except SalaryError:
  print("SalaryError caught")
except BonusError:
  print("BonusError caught")

#code2
emp = Employee("Katze Rik",\
                    50000)
try:
  emp.give_bonus(7000)
except BonusError:
  print("BonusError caught")
except SalaryError:
  print("SalaryError caught")
