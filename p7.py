from datetime import date
class Person:
 def __init__(self, name, age):
  self.name = name
  self.age = age
 # a class method to create a Person object by birth year.
 @classmethod
 def fromBirthYear(Person, name, year):
  return Person(name, int(date.today().year) - year)
 # a static method to check if a Person is adult or not.
person1 = Person('mayank', 21)
person2 = Person.fromBirthYear('mayank', 1996)
print(person1.age)
print(person2.age) 