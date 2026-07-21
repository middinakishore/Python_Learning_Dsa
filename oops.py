'''class Person:
    def __init__(self, name, gender, age):
        self.__name = name
        self.__gender = gender
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def set_gender(self, gender):
        self.__gender = gender

    def set_age(self, age):
        if age > 0:
            self.__age = age

    def get_name(self):
        return self.__name

    def get_gender(self):
        return self.__gender

    def get_age(self):
        return self.__age

    def display_info(self):
        print(f"Name: {self.__name}, Gender: {self.__gender}, Age: {self.__age}")


p1 = Person("Kishore", "Male", 20)
print("--- Initial Data ---")
p1.display_info()

p1.set_name("Kiran")
p1.set_age(26)

print("\n--- Updated Data ---")
print("Updated Name:", p1.get_name())
p1.display_info()
'''
from abc import ABC, abstractmethod

'''class BankAccount(ABC):
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    def get_balance(self):
        return self._balance

class SavingsAccount(BankAccount):
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            return True
        return False

account = SavingsAccount("Ravi", 5000)
account.deposit(1500)
account.withdraw(2000)
print(account.get_balance())'''


class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"{self.name} is eating."

    def sleep(self):
        return f"{self.name} is sleeping."


class Dog(Animal):
    def bark(self):
        return f"{self.name} is barking."


class Cat(Animal):
    def meow(self):
        return f"{self.name} is meowing."


dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.eat())
print(dog.bark())
print(cat.sleep())
print(cat.meow())

