#Capter 4 - Best Practices of Class Design
#4.1 Designing for inheritance and polymorphism - 50 xp

#4.2 Polymorphic methods
#To design classes effectively, you need to understand how inheritance and polymorphism work together.
#In this exercise, you have three classes - one parent and two children - each of which has a talk() method. 
#Analyze the following code:
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
Parent talking!
Child talking!
Talkative Child talking!
Parent talking!

#4.3 Square and rectangle
#The classic example of a problem that violates the Liskov Substitution Principle is the Circle-Ellipse problem, 
# sometimes called the Square-Rectangle problem. By all means, it seems like you should be able to define a class 
# Rectangle, with attributes h and w (for height and width), and then define a class Square that 
# inherits from the Rectangle. After all, a square "is-a" rectangle!
# Unfortunately, this intuition doesn't apply to object-oriented design.

#4.3.1 Exercise
# Define a Rectangle class
class Rectangle:
    def __init__(self, h, w)
        self.h = h
        self.w = w
# Define a Square class
class Square(Rectangle):
    def __init__(self, w):
        Rectangle.__init__(self, w,w)
#4.3.2 Exercise
