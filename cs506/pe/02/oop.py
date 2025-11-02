# Part 1: User class
class User:
    """
    Represents a basic user profile with several attributes.

    Explanation:
    ------------
    - Attributes: first_name, last_name, age, email, location.
    - describe_user(): prints user summary.
    - greet_user(): prints personalized greeting.

    Example:
    --------
    >>> user = User("Clark", "Ngo", 30, "clark@example.com", "Seattle")
    >>> user.describe_user()
    Name: Clark Ngo, Age: 30, Email: clark@example.com, Location: Seattle
    >>> user.greet_user()
    Hello Clark Ngo! Welcome back.
    """

    def __init__(self, first_name, last_name, age, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location

    def describe_user(self):
        print(f"Name: {self.first_name} {self.last_name}, Age: {self.age}, "
              f"Email: {self.email}, Location: {self.location}")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}! Welcome back.")


# Create two users and call methods
user1 = User("Clark", "Ngo", 30, "clark@example.com", "Seattle")
user2 = User("Mia", "Lopez", 25, "mia@example.com", "Manila")

user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()


# Part 2: Multilevel Inheritance Example
class Animal:
    """Base class representing an animal."""
    def speak(self):
        print("Animal speaks in its own way.")


class Mammal(Animal):
    """Intermediate class representing mammals."""
    def speak(self):
        print("Mammal makes a sound.")


class Dog(Mammal):
    """Derived class representing dogs."""
    def speak(self):
        print("Dog barks: Woof Woof!")


# Demonstrate multilevel inheritance
dog = Dog()
dog.speak()  # Expected output: Dog barks: Woof Woof!
