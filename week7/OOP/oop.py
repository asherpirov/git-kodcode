class Dog:
    """Represents a dog."""
    def __init__(self, name):
        """Initializes a dog with a name."""
        self.name = name
    def bark(self):
        """Returns a barking sound string."""
        return self.name + " says woof"

d = Dog("Rex")
print(d.bark())


#q2

class Rectangle:
    """Represents a rectangle."""
    def __init__(self, width, height):
        """Initializes width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Calculates the rectangle area."""
        return self.width * self.height

r = Rectangle(3,4).area()
print(r)

#q3

class Counter:
    """Represents a simple counter."""
    def __init__(self, counter = 0):
        """Initializes counter with a start value."""
        self.count = counter

    def increment(self):
        """Increments the counter by 1."""
        self.count += 1

    def value(self):
        """Returns the current counter value."""
        return self.count

c = Counter()
c.increment()
c.increment()
print(c.value())

#q4

class Point:
    """Represents a point in 2D space."""
    def __init__(self, x, y):
        """Initializes x and y coordinates."""
        self.x = x
        self.y = y

    def __str__(self):
        """Returns a string of the point."""
        return f"({self.x}, {self.y})"

#q5

class BankAccount:
    """Represents a basic bank account."""
    def __init__(self, balance = 0):
        """Initializes account with a default balance of 0."""
        self.balance = balance

    def deposit(self, amount):
        """Deposits money into the account."""
        self.balance += amount
    def withdraw(self, amount):
        """Withdraws money if sufficient funds exist."""
        if amount <= self.balance:
            self.balance -= amount

my_account = BankAccount()
my_account.deposit(100)
my_account.withdraw(50)
print(my_account.balance)

#q6
class Temperature:
    """Represents temperature in Celsius."""
    def __init__(self,celsius):
        """Initializes Celsius value."""
        self.celsius = celsius

    def to_fahrenheit(self):
        """Converts Celsius to Fahrenheit."""
        return (self.celsius *1.8) + 32

print(Temperature(100).to_fahrenheit())

#q7

class Student:
    """Represents a student with a shared school."""
    school = "Kodcode"

    def __init__(self, name):
        """Initializes student with a name."""
        self.name = name

student1 = Student("Asher")
student2 = Student("Yossi")
student1.name = "avi"
print(student1.name)
print(student2.name)

#q8
class Player:
    """Represents a player and tracks total instances."""
    counter = 0
    def __init__(self, name):
        """Initializes a player and increments total count."""
        self.name = name
        Player.counter += 1

player1 = Player("asher")
player2 = Player("yossi")
print(Player.counter)

#q9
class Money:
    """Represents a monetary amount."""
    def __init__(self, amount):
        """Initializes amount."""
        self.amount = amount

    def is_more_than(self, other):
        """Compares if this amount is larger than another."""
        return self.amount > other.amount
#q10
class Playlist:
    """Represents a music playlist."""
    def __init__(self):
        """Initializes an empty playlist."""
        self.songs = []

    def add(self, title):
        """Adds a song to the playlist."""
        self.songs.append(title)

    def remove(self, title):
        """Removes a song if it exists in the playlist."""
        if title in self.songs:
            self.songs.remove(title)

    def count(self):
        """Returns the number of songs."""
        return len(self.songs)

    def __str__(self):
        """Returns a string of all songs."""
        return f"Playlist songs: {', '.join(self.songs)}"









