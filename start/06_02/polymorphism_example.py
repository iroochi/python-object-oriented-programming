"""
Python Polymorphism example
"""
class ClassA:
    def my_method1(self):
        print("my_method1() from Class A")

class ClassB(ClassA):
    def my_method1(self):
        print("my_method1() from Class B")

objA = ClassA()
objB = ClassB()
objA.my_method1()
objB.my_method1()