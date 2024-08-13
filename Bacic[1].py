
# 1. Create a class called Person with attributes name and age. Create an object of the class and print 
# its attributes.


# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# Amin=person("Amin",25)
# print(Amin.age())
# print(Amin.name())

# 2. Add a method called greet to the Person class that prints a greeting message including the 
# person's name.
# class person:
#     def __init__(self,name):
#         self.name=name
#     def greet(self):
#         return F"({self.name},{"Hello How are you??"})"
# Amin=person("Amin")
# print(Amin.greet())

# 3. Create a class called Car with attributes make, model, and year. Include a method to print out 
# the car's details.

# class Car:
#     def __init__(self,make,model,year):
#         self.make=make
#         self.model=model
#         self.year=year

#     def out_of_car_detels(self):
#         return F"({"the car Deteals are"}  {self.make},{self.model},{self.year})"

# truck=Car("Tesla","BmW",2024)
# print(truck.out_of_car_detels())

# 4. Create a class Circle with a method to compute the area. Initialize the class with the radius?


# import math

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
    
#     def compute_area(self):
#         return math.pi * (self.radius ** 2)
# circle=Circle(5)
# print(circle.compute_area())       


# 5. Create a class Rectangle with methods to compute the area and perimeter. Initialize the class 
# with the length and width.# class Rectangle:
#     def __init__(self,width,length):
#         self.width=width
#         self.length=length

#     def area(self):
#         return (self.width*self.length)
#     def perimeter(self):
#         return 2*(self.width+self.length)
    
# rectangle=Rectangle(5,3)
# print("the area is ",rectangle.area())
# print("the perimeter  is ",rectangle.perimeter())


# Inheritance and Polymorphism Exercises

# 6. Create a base class Animal with a method speak. Create two derived classes Dog and Cat that 
# override the speak method.


# class animal:
#     def speak(self):
#         return F"({"Animals can speak like  human!"})"
    
# class Dog(animal):
#     def speak(self):
#         return F"({"Dogs Bark!"})"
# class Cat(animal):
#     def speak(self):
#         return F"({"cats mew"})"
# Animal=animal()
# dog=Dog()
# cat=Cat()
# print(Animal.speak())
 v# print(dog.speak())
# print(cat.speak())


# # 7. Create a base class Shape with a method area. Create derived classes Square and Triangle that 
# # implement the area method.

# from abc import ABC, abstractmethod


# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# class Square(Shape):
#     def __init__(self, side_length):
#         self.side_length = side_length

#     def area(self):
#         return self.side_length ** 2

# class Triangle(Shape):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height

#     def area(self):
#         return 0.5 * self.base * self.height
# if __name__ == "__main__":
#     square = Square(4)
#     triangle = Triangle(3, 5)

#     print(f"Area of the square: {square.area()}")
#     print(f"Area of the triangle: {triangle.area()}")








# 8. Create a class Employee with attributes name and salary. Create a derived class Manager with an 
# additional attribute department.

# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary

# class Manager(Employee):
#     def __init__(self,name,salary,department):
#         super().__init__(name,salary)
#         self.department=department
# emp=Employee("Ali",20000)
# Ahmad=Manager("Ahmad",30000,"IS")
# print(emp.name)
# print(emp.salary)
# print(Ahmad.department)

# 9. Create a base class Vehicle with a method drive. Create derived classes Bike and Truck that 
# override the drive method.

# class Vehicle:
#     def drive(self):
#         return f"({"Vechail made cars "})"
# class Bike(Vehicle):
#     def drive(self):
#         return f"({"Bike max speed is 200km/hour"})"
# class Truck(Vehicle):
#     def drive(self):
#         return f"({"Truck max speed is 20km/hour"})"


# my_bike=Bike()
# truck=Truck()
# print(my_bike.drive())
# print(truck.drive())


# 10. Create a base class Bird with a method fly. Create derived classes Eagle and Penguin. Override 
# the fly method in Penguin to indicate that penguins cannot fly.

# class Bird:
#     def fly(self):
#         return f"({"Birds cann fly"})"



# class Eagle(Bird):
#     def Fly(self):
#         return f"({"Eagle also can fly!!"})"

# class penguin(Bird):
#     def fly(self):
#         return f"({"that is so bad penguins can not fly!"})"

# b=Bird()
# e=Eagle()
# p=penguin()
# print(p.fly())


# Encapsulation and Abstraction Exercises

# 11. Create a class Account with private attributes balance. Provide public methods to deposit and 
# withdraw money

# class Account:
#     def __init__(self,balance):
#         self.__balance=balance
#     def deposit (self,amounth):
#         self.__balance +=amounth
#         print("Deposit is successful. your new blance is",self.__balance)
#     def withdraw(self,amounth):
#         if amounth > self.__balance:
#             print("insufficient balance")
#         else:
#             self.__balance -=amounth
#             print("withdrawl is successful new balance is :",self.__balance)
#     def __show_balance(self):
#         print ("your currient balance is:",self.__balance)
# account=Account(20000)
# account.deposit(10000)
# account.withdraw(50000)
# account.withdraw(5000)
# account.__show_balance()
# # account.balance=999999
# # account.balance()


# 12. Create a class Book with private attributes title, author, and pages. Provide public methods to get 
# and set these attributes.

class Book:
    def __init__(self,title,author,pages):
        self.__title=title
        self.__author=author
        self.__pages=pages


    def get_title(self):
        print("title is ",self.__title)
    
    def get_author(self):
        print("author name is ",self.__author)
    
    def get_pages(self):
        print("pages of book is",self.__pages)

    
    def set_titile(self,title):
        self.__title=title
        
    def set_author(self,author):
        self.__author=author

    def set_pages(self,pages):
        self.__pages=pages

book=Book("pythons_book","salim",1000)
book.get_title()
book.get_author()
book.get_pages()


book.set_titile("new title is pythons_book")
book.set_author("new author is jan")
book.set_pages("new pages are 500")
print(book.get_title())
print(book.get_author())
print(book.get_pages())
    
# 13. Create a class Laptop with private attributes brand, model, and price. Provide a method to apply 
# a discount and a method to display laptop details.

 

# class Laptop:
#     def __init__(self, brand, model, price): 
#         self.__brand = brand    
#         self.__model = model    
#         self.__price = price
    
#     def apply_discount(self, discount_percentage):
        
#         if 0 < discount_percentage < 100:
#             discount_amount = (discount_percentage / 100) * self.__price
#             self.__price -= discount_amount
#             print(f"Discount applied: {discount_percentage}%. New price is ${self.__price:}")
#         else:
#             print("Discount percentage must be between 0 and 100.")
    
#     def display_details(self):
#         """Display the details of the laptop."""
#         print(f"Brand: {self.__brand}")
#         print(f"Model: {self.__model}")
#         print(f"Price: ${self.__price:}")


# laptop = Laptop("Dell", "XPS 13", 1200)  
# laptop.display_details()                
# laptop.apply_discount(10)              
# laptop.display_details()            




# 14. Create a class BankAccount with private attributes account_number and balance. Provide 
# methods to deposit, withdraw, and check the balance.


# class BankAccount:
#     def __init__(self,account_number,initial_balance):
#         self.__account_number=account_number
#         self.__initial_balance=initial_balance


#     def deposit(self,amount):
#         if amount>0:
#             amount+=self.__initial_balance
#             print(F"Deposit amount is{amount:} New balanceis{self.__initial_balance}")
#         else:
#             print("amount must be positive")

#     def withdraw(self,amount):
#         if amount>0:
#             if amount <= self.__initial_balance:
#                 self.__initial_balance -= amount
#                 print(F"withdraw is succesful {amount} :your current balance is {self.__initial_balance}")
#             else:
#                 print("your don't have insufficient:plese deposit your Account than try again ")
#     def checkbalance(self):
#         print(F"your current balance is {self.__initial_balance}")

# my_banck_account=BankAccount(1213,3500)
# my_banck_account.checkbalance()
# my_banck_account.deposit(500)
# my_banck_account.withdraw(1000)
# my_banck_account.withdraw(10000)


# 15. Create a class Student with private attributes name, grade, and age. Provide methods to get and 
# set these attributes and a method to display the student's details.



# class Student:
#     def __init__(self, name, grade, age):
#         self.__name = name    
#         self.__grade = grade  
#         self.__age = age      
    

#     def get_name(self):
#         return self.__name
    
#     def get_grade(self):
#         return self.__grade
    
#     def get_age(self):
#         return self.__age

#     def set_name(self, name):
#         self.__name = name
    
#     def set_grade(self, grade):
#         self.__grade = grade
    
#     def set_age(self, age):
#         if age > 0:
#             self.__age = age
#         else:
#             print("Age must be positive.")
    
    
#     def display_details(self):
#         print(f"Name: {self.__name}")
#         print(f"Grade: {self.__grade}")
#         print(f"Age: {self.__age}")

# student = Student("ali", "100", 15) 
# student.display_details()


# student.set_name("Ahmad")   
# student.set_grade("90")        
# student.set_age(16)  
# student.display_details()            

# # Display updated student details
# student.display_details()


           
# advance class 


# 16. Create a class Library with attributes name and books (a list of Book objects). Provide methods 
# to add and remove books.



# class Book:
#     def __init__(self,book_name):
#         self.book_name=book_name

#     def __str__(self):
#         return f"Book_name is:{self.book_name}"

# class Library:
#     def __init__(self, name):
#         self.name = name            # Name of the library
#         self.books = []             # List of Book objects

#     def add_book(self, book):
#         """Add a book to the library."""
#         if isinstance(book, Book):
#             self.books.append(book)
#             print(f"Added book: {book}")
#         else:
#             print("Only objects of type Book can be added.")

#     def remove_book(self, book_name):
#         """Remove a book from the library by title."""
#         for book in self.books:
#             if book.book_name == book_name:
#                 self.books.remove(book)
#                 print(f"Removed book: {book}")
#                 return
#         print(f"No book found with title '{title}'.")

#     def display_books(self):
#         """Display all books in the library."""
#         if self.books:
#             print(f"Books in {self.name}:")
#             for book in self.books:
#                 print(book)
#         # else:
#         #     print(f"No books available in {self.name}.")

# # Example usage:
# library = Library("Afghan")  # Create a library

#  # Create some Book objects
# book1 = Book("python programing")
# book2=Book("java")

# # Add books to the library
# library.add_book(book1)
# library.add_book(book2)
# # Display all books
# library.display_books()

# library.remove_book("python programing")

# # # Display all books after removal 
# # library.display_books()

############################################################################################################################
 


# 17. Create a class School with attributes name and students (a list of Student objects). Provide 
# methods to add and remove students.

# class Student:
#     def __init__(self, name):
#         self.name = name


#     def __str__(self):
#         return f"Name: {self.name}"

# class School:  
#     def __init__(self, school_name):
#         self.school_name = school_name                # Name of the school
#         self.students = []              # List of Student objects

#     def add_student(self, student):
#         if isinstance(student, Student):
#             self.students.append(student)
#             print(f"Added student: {student}")

#     def remove_student(self, name):
       
#         for student in self.students:
#             if student.name == name:
#                 self.students.remove(student)
#                 print(f"Removed student: {student}")
#             

#     def display_students(self):
        
#         if self.students:
#             print(f"Students in {self.school_name}:")
#             for student in self.students:
#                 print(student)
#        


# school = School("Noor High school") 

# student1 = Student("Ali")
# student2 = Student("Ahmad")
# student3 = Student("salim")


# school.add_student(student1)
# school.add_student(student2)
# school.add_student(student3)

# school.display_students()

# school.remove_student("Ali")

# school.display_students()


# 18. Create a class Team with attributes name and members (a list of Person objects). Provide 
# methods to add and remove members.




# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"Name: {self.name}, Age: {self.age}"

# class Team:
#     def __init__(self, name):
#         self.name = name                # Name of the team
#         self.members = []              # List of Person objects

#     def add_member(self, person):
#         """Add a member to the team."""
#         if isinstance(person, Person):
#             self.members.append(person)
#             print(f"Added member: {person}")
#         else:
#             print("Only objects of type Person can be added.")

#     def remove_member(self, name):
#         """Remove a member from the team by name."""
#         for person in self.members:
#             if person.name == name:
#                 self.members.remove(person)
#                 print(f"Removed member: {person}")
#                 return
#         print(f"No member found with name '{name}'.")

#     def display_members(self):
#         """Display all members of the team."""
#         if self.members:
#             print(f"Members of {self.name}:")
#             for person in self.members:
#                 print(person)
#         else:
#             print(f"No members available in {self.name}.")

# # Example usage:
# team = Team("Developers")  # Create a team

# # Create some Person objects
# person1 = Person("Alice", 30)
# person2 = Person("Bob", 25)
# person3 = Person("Charlie", 35)

# # Add members to the team
# team.add_member(person1)
# team.add_member(person2)
# team.add_member(person3)

# # Display all members
# team.display_members()

# # Remove a member
# team.remove_member("Bob")

# # Display all members after removal
# team.display_members()







# 19. Create a class Company with attributes name and employees (a list of Employee objects). 
# Provide methods to add and remove employees.






# class Employee:
#     def __init__(self,name,age,salary):
#         self.name=name
#         self.age=age
#         self.salary=salary
#     def __str__(self):
#         return F"Name:{self.name},Age:{self.age},Salary:{self.salary}"
    

# class Company:
#     def __init__(self,company_name):
#         self.company_name=company_name
#         self.employees=[]
#     def add_employee(self,employee):
#         if isinstance(employee,Employee):
#             self.employees.append(employee)
#             print(f"Added Employe is : {employee}")
#         else:
#             print("only object Employee can add")
#     def remove_employee(self,name):
#         for employee in self.employees:
#             if employee.name==name: 
#                 self.employees.remove(employee)
#                 print(f"Removed employee is : {employee}")


#     def disply_details(self):
#         if self.employees:
#             print(f"Employees of :{self.company_name}")
#             for employee in self.employees:
#                 print(employee)




# Google=Company("Google")
# employee1=Employee("salim",22,999999)
# employee2=Employee("masom",66,55555)
# employee3=Employee("shahar",55,123445)

# Google.add_employee(employee1)
# Google.add_employee(employee2)
# Google.add_employee(employee3)

# Google.remove_employee("salim")

# Google.disply_details()





# 20. Create a class Zoo with attributes name and animals (a list of Animal objects). Provide methods 
# to add and remove animals


# class Animal:
#     def __init__(self, name, species, age):
#         self.name = name
#         self.species = species
#         self.age = age

#     def __str__(self):
#         return f"Name: {self.name}, Species: {self.species}, Age: {self.age}"

# class Zoo:
#     def __init__(self, name):
#         self.name = name                # Name of the zoo
#         self.animals = []              # List of Animal objects

#     def add_animal(self, animal):
#         """Add an animal to the zoo."""
#         if isinstance(animal, Animal):
#             self.animals.append(animal)
#             print(f"Added animal: {animal}")
#         else:
#             print("Only objects of type Animal can be added.")

#     def remove_animal(self, name):
#         """Remove an animal from the zoo by name."""
#         for animal in self.animals:
#             if animal.name == name:
#                 self.animals.remove(animal)
#                 print(f"Removed animal: {animal}")
#                 return
#         print(f"No animal found with name '{name}'.")

#     def display_animals(self):
#         """Display all animals in the zoo."""
#         if self.animals:
#             print(f"Animals in {self.name}:")
#             for animal in self.animals:
#                 print(animal)
#         else:
#             print(f"No animals available in {self.name}.")

# # Example usage:
# zoo = Zoo("Wildlife Safari")  # Create a zoo

# # Create some Animal objects
# animal1 = Animal("Lion", "Panthera leo", 5)
# animal2 = Animal("Elephant", "Loxodonta africana", 10)
# animal3 = Animal("Giraffe", "Giraffa camelopardalis", 7)

# # Add animals to the zoo
# zoo.add_animal(animal1)
# zoo.add_animal(animal2)
# zoo.add_animal(animal3)

# # Display all animals
# zoo.display_animals()

# # Remove an animal
# zoo.remove_animal("Elephant")

# # Display all animals after removal
# zoo.display_animals()




# 21. Create a class FileManager with methods to read from and write to a file.


# class FileManager:
#     def __init__(self, filename):
#         self.filename = filename

#     def write_to_file(self, content):
#         """Writes the specified content to the file."""
#         try:
#             with open(self.filename, 'w') as file:
#                 file.write(content)
#             print(f"Content written to {self.filename} successfully.")
#         except IOError as e:
#             print(f"An error occurred while writing to the file: {e}")

#     def read_from_file(self):
#         """Reads and returns the content of the file."""
#         try:
#             with open(self.filename, 'r') as file:
#                 content = file.read()
#             return content
#         except FileNotFoundError:
#             print(f"The file {self.filename} does not exist.")
#             return None
#         except IOError as e:
#             print(f"An error occurred while reading the file: {e}")
    
# # Example usage:
# if __name__ == "__main__":
#     file_manager = FileManager('example.txt')

#     # Writing to the file
#     file_manager.write_to_file('Hello, world!')

#     # Reading from the file
#     content = file_manager.read_from_file()
#     if content:
#         print("File content:")  
#         print(content)

# 22. Create a class Log with methods to write error messages to a log file.


# import os
# from datetime import datetime

# class Log:
#     def __init__(self, log_filename='error.log'):
#         self.log_filename = log_filename

#     def write_error(self, message):
#         """Writes an error message to the log file with a timestamp."""
#         timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#         log_entry = f"{timestamp} - ERROR - {message}\n"
        
#         try:
#             with open(self.log_filename, 'a') as log_file:
#                 log_file.write(log_entry)
#             print(f"Error logged to {self.log_filename}.")
#         except IOError as e:
#             print(f"An error occurred while writing to the log file: {e}")

#     def configure_log_file(self, new_filename):
#         """Changes the log file to a new filename."""
#         self.log_filename = new_filename
#         print(f"Log file changed to {self.log_filename}.")

# # Example usage:
# if __name__ == "__main__":
#     logger = Log()

#     # Write an error message to the default log file
#     logger.write_error("This is a test error message.")

#     # Change the log file and write another error message
#     logger.configure_log_file('new_error.log')
#     logger.write_error("This is another test error message.")



# 23. Create a class Config that reads configuration settings from a file and provides methods to access 
# these settings.

# import json

# class Config:
#     def __init__(self, config_filename):
#         self.config_filename = config_filename
#         self.config_data = self._load_config()

#     def _load_config(self):
#         """Loads the configuration settings from the file."""
#         try:
#             with open(self.config_filename, 'r') as file:
#                 return json.load(file)
#         except FileNotFoundError:
#             print(f"Configuration file {self.config_filename} not found.")
#             return {}
#         except json.JSONDecodeError:
#             print(f"Error decoding JSON from the configuration file {self.config_filename}.")
#             return {}
#         except IOError as e:
#             print(f"An error occurred while reading the configuration file: {e}")
#             return {}

#     def get(self, key, default=None):
#         """Gets the value of a configuration setting."""
#         return self.config_data.get(key, default)

#     def set(self, key, value):
#         """Sets a configuration setting and saves it to the file."""
#         self.config_data[key] = value
#         self._save_config()

#     def _save_config(self):
#         """Saves the configuration settings to the file."""
#         try:
#             with open(self.config_filename, 'w') as file:
#                 json.dump(self.config_data, file, indent=4)
#         except IOError as e:
#             print(f"An error occurred while writing to the configuration file: {e}")

# # Example usage:
# if __name__ == "__main__":
#     config = Config('config.json')

#     # Set a configuration setting
#     config.set('database_host', 'localhost')
#     config.set('database_port', 5432)

#     # Get configuration settings
#     db_host = config.get('database_host', 'default_host')
#     db_port = config.get('database_port', 3306)

#     print(f"Database Host: {db_host}")
#     print(f"Database Port: {db_port}")

# 24. Create a class Database that connects to a database and provides methods to execute queries. 
# Handle exceptions if the connection fails


# import sqlite3

# class Database:
#     def __init__(self, db_filename):
#         self.db_filename = db_filename
#         self.connection = None 
#         self.cursor = None
#         self._connect()

#     def _connect(self):
#         """Establishes a connection to the SQLite database."""
#         try:
#             self.connection = sqlite3.connect(self.db_filename)
#             self.cursor = self.connection.cursor()
#             print(f"Connected to database {self.db_filename}.")
#         except sqlite3.Error as e:
#             print(f"An error occurred while connecting to the database: {e}")

#     def execute_query(self, query, params=None):
#         """Executes a single query and commits the changes if applicable."""
#         if params is None:
#             params = ()
#         try:
#             self.cursor.execute(query, params)
#             self.connection.commit()
#             print("Query executed successfully.")
#         except sqlite3.Error as e:
#             print(f"An error occurred while executing the query: {e}")

#     def fetch_results(self, query, params=None):
#         """Executes a query and fetches the results."""
#         if params is None:
#             params = ()
#         try:
#             self.cursor.execute(query, params)
#             results = self.cursor.fetchall()
#             return results
#         except sqlite3.Error as e:
#             print(f"An error occurred while fetching the results: {e}")
#             return []

#     def close(self):
#         """Closes the connection to the database."""
#         try:
#             if self.connection:
#                 self.connection.close()
#                 print("Database connection closed.")
#         except sqlite3.Error as e:
  #             print(f"An error occurred while closing the connection: {e}")

# # Example usage:
# if __name__ == "__main__":
#     db = Database('example.db')

#     # Create a table
#     db.execute_query('''
#         CREATE TABLE IF NOT EXISTS users (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             username TEXT NOT NULL,
#             email TEXT NOT NULL
#         )
#     ''') 

#     # Insert a new record
#     db.execute_query('INSERT INTO users (username, email) VALUES (?, ?)', ('john_doe', 'john@example.com'))

#     # Fetch records
#     results = db.fetch_results('SELECT * FROM users')
#     for row in results:
#         print(row)

#     # Close the connection
#     db


# 25. Create a class Report that generates a report from data in a file. Provide methods to handle 
# exceptions if the file does not exist or cannot be read.



# class Report:
#     def __init__(self, filename):
#         self.filename = filename
#         self.data = None
#         self._load_data()

#     def _load_data(self):
#         """Loads data from the specified file."""
#         try:
#             with open(self.filename, 'r') as file:
#                 self.data = file.read()
#             print(f"Data loaded successfully from {self.filename}.")
#         except FileNotFoundError:
#             print(f"File {self.filename} does not exist.")
#             self.data = ""
#         except IOError as e:
#             print(f"An error occurred while reading the file: {e}")
#             self.data = ""

#     def generate_report(self):
#         """Generates a report based on the loaded data."""
#         if self.data:
#             # Example report generation: count lines and words
#             num_lines = self.data.count('\n') + 1
#             num_words = len(self.data.split())
#             report = f"Report for file: {self.filename}\n"
#             report += f"Total lines: {num_lines}\n"
#             report += f"Total words: {num_words}\n"
#             return report
#         else:
#             return "No data available to generate the report."

#     def display_report(self):
#         """Prints the generated report."""
#         report = self.generate_report()
#         print(report)

# # Example usage:
# if __name__ == "__main__":
#     report = Report('data.txt')
#     report.display_report()



# Real-world Application Exercises
# 26. Create a class Ticket for a movie theater with attributes movie_name, seat_number, and price. 
# Provide methods to display ticket details and apply discounts.

# class Ticket:
#     def __init__(self,move_name,seat_number,price):
#         self.move_name=move_name
#         self.seat_number=seat_number
#         self.price=price
    
#     def display_ticket_details(self):
#         return (f"Move:{self.move_name}\n"
#         f" Seat:{self.seat_number}\n"
#         f" Price:{self.price}" )
                
    
#     def apply_discount(self,discount_percentage):
#         if 0< discount_percentage<100:
#             discount_amout= (self.price*discount_percentage)/100
#             self.price-=discount_amout
#         else:
#             print("discount must be betwen 0 and 100")
# ticket=Ticket("Tytinic",77,1200)
# print(ticket.display_ticket_details())
# # after apply discount
# ticket.apply_discount(50)
# print(ticket.display_ticket_details())
   
                




# 27. Create a class ShoppingCart with methods to add, remove, and display items. Each item should 
# be an object of a class Item with attributes name and price.

# class Item:
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price

# class ShoppingCart(self.card_no,item):
#     self.card_no=card_no
#     self.items=[]


#     def add_item(self,item):
#         self.items.append(item)
#         return f"Added Item : {item}"

#     def remove_item(self,item_name):
#         for item in self.items:
#             if item.name ==name:
#                 return f" Removed Itemm : {item}"

#     def display_items(self):
#         if self.items:
#             return f" Item in Shoping Card : {item}"
    
# sh_card=ShoppingCart(7)
# item1=Item("Clock",3300)
# item2=Item("Coat",300)
# item3=Item("Shoes",500)
# sh_card.add_item(item1)
# sh_card.add_item(item2)
# sh_card.add_item(item3)
          
            





    

# class Item:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#     def __str__(self):
#         return f"{self.name}: ${self.price:.2f}"

# class ShoppingCart:
#     def __init__(self):
#         self.items = []

#     def add_item(self, item):
#         self.items.append(item)

#     def remove_item(self, item_name):
#         self.items = [item for item in self.items if item.name != item_name]

#     def display_items(self):
#         return [str(item) for item in self.items]

# # Example usage:
# cart = ShoppingCart()
# cart.add_item(Item("Apple", 0.99))
# cart.add_item(Item("Bread", 2.49))
# print(cart.display_items())
# cart.remove_item("Apple")
# print(cart.display_items())



























# 28. Create a class Restaurant with attributes name and menu (a list of Item objects). Provide 
# methods to add and remove items from the menu.





# class Menu:
#     def __init__(self,food_name,price):
#         self.food_name=food_name
#         self.price=price

#     def __str__(self):
#         return f" Food_name:{self.food_name} Price:{self.price}"

# class Restaurant:
#     def __init__(self,name):
#         self.name=name
#         self.items=[]
#     def add_item(self,item):
#         if isinstance(item,Menu):
#             self.items.append(item)
#             print(f"Added item:{item}")
#         else:
#             print("only item object can add")
#     def remove_item(self,name):
#         for item in self.items:
#             if item.food_name==name:
#                 self.items.remove(item)
#                 print(f"Rmoved item:{item}")
#             else:
#                 print("itme not foud")

#     def disply_item(self):
#         if self.items:
#             print("Items in Menu")
#             for item in self.items:
#                 print(item)


# kabul=Restaurant("kabul")
# menu1=Menu("Rice",180)
# menu2=Menu("soup",80)
# kabul.add_item(menu1)
# kabul.add_item(menu2)
# kabul.disply_item()
# kabul.remove_item("Rice")
# kabul.disply_item()




# 29. Create a class Flight with attributes flight_number, destination, and passengers (a list of Person
# objects). Provide methods to add and remove passengers.


# class passengers:
#     def __init__(self,name,set_number):
#         self.name=name
#         self.set_number=set_number

#     def __str__(self):
#         return f" Name:{self.name} Set_number:{self.set_number}"
    
# class Flights:
#     def __init__(self,flight_number,destination):
#         self.flight_number=flight_number
#         self.destination=destination
#         self.persons=[]
    
#     def add_passenger(self,person):
#         if isinstance(person,passengers):
#             self.persons.append(person)
#             print(f"Add passenger:{person}")
#         else:
#             print("only passengers object can add")


#     def remove_passenger(self,name):
#         for person in self.persons:
#             if person.name==name:
#                 self.persons.remove(person)
#                 print(f"Removed passenger:{person}")
#         # else:
#         #     print("person not found")
#     def disply_flight_details(self):
#         if self.persons:
#             print("passengers in Flight")
#             for person in self.persons:
#                 print(person)

# flight=Flights(7,"Australi")
# person1=passengers("Hakimi",77)
# person2=passengers("Ali",66)
# flight.add_passenger(person1)
# flight.add_passenger(person2)
# flight.disply_flight_details()
# flight.remove_passenger("Ali")
# flight.disply_flight_details()

# 30. Create a class Hotel with attributes name and rooms (a list of Room objects). Each Room
# should have attributes room_number and is_occupied. Provide methods to book and checkout rooms.




# class Room:
#     def __init__(self,room_number):
#         self.room_number=room_number
#         self.is_occupied=False


#     def __str__(self):
#         status= "occupied" if self.is_occupied else   "Avialabel"
#         return f"Room:{self.room_number}{status}"




# class Hotel:
#     def __init__(self,name):
#         self.name=name
#         self.rooms=[]



        
#     def add_room(self,room):
#         self.rooms.append(room)

#     def book_room(self,room_number):
#         for room in self.rooms:
#             if room.room_number==room_number:
#                 if not room.is_occupied:
#                     room.is_occupied=True
#                     return f" Room:{room_number} has been occupied"
#                 else:
#                     return f" Room :{room_number} is already occupeid"

#     def check_out_room(self,room_number):
#         for room in self.rooms:
#             if room.room_number==room_number:
#                 if not room.is_occupied:
#                     room.is_occupied=False 
#                     return f"   Room : {room_number}"


#                     return f"Room:   {room_number} has been checkout"
#                 else:
#                         return f"Room:  {room_number} is not occupied"
#                 return f"Room:  {room_number} does not exsist"

#     def disply_rooms(self):
#         return {str(room)for room in self.rooms}





# # Example usage:
# hotel = Hotel("kabul")
# hotel.add_room(Room(101))
# hotel.add_room(Room(102))
# print(hotel.disply_rooms())
# print(hotel.book_room(101))
# print(hotel.check_out_room(101))
# print(hotel.disply_rooms())



# GUI Application Exercises
# 36. Create a class CounterApp that uses tkinter to create a simple counter GUI with increment and 





# import tkinter as tk

# class CounterApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Counter App")
        
#         self.counter = 0

#         self.label = tk.Label(root, text="Counter: 0", font=("Arial", 24))
#         self.label.pack(pady=20)

#         self.increment_button = tk.Button(root, text="Increment", command=self.increment)
#         self.increment_button.pack(side=tk.LEFT, padx=10)

#         self.decrement_button = tk.Button(root, text="Decrement", command=self.decrement)
#         self.decrement_button.pack(side=tk.RIGHT, padx=10)

#     def update_label(self):
#         self.label.config(text=f"Counter: {self.counter}")

#     def increment(self):
#         self.counter += 1
#         self.update_label()

#     def decrement(self):
#         self.counter -= 1
#         self.update_label()

# # Example usage
# root = tk.Tk()
# app = CounterApp(root)
# root.mainloop()

# 37. Create a class ToDoApp that uses tkinter to create a to-do list GUI where users can add and 
# remove tasks.


# import tkinter as tk

# class ToDoApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("To-Do List App")

#         self.tasks = []

#         self.task_entry = tk.Entry(root, width=50)
#         self.task_entry.pack(pady=10)

#         self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
#         self.add_button.pack(pady=5)

#         self.task_listbox = tk.Listbox(root, width=50, height=10)
#         self.task_listbox.pack(pady=10)

#         self.remove_button = tk.Button(root, text="Remove Selected Task", command=self.remove_task)
#         self.remove_button.pack(pady=5)

#     def add_task(self):
#         task = self.task_entry.get()
#         if task:
#             self.tasks.append(task)
#             self.update_task_listbox()
#             self.task_entry.delete(0, tk.END)

#     def remove_task(self):
#         selected_index = self.task_listbox.curselection()
#         if selected_index:
#             self.tasks.pop(selected_index[0])
#             self.update_task_listbox()

#     def update_task_listbox(self):
#         self.task_listbox.delete(0, tk.END)
#         for task in self.tasks:
#             self.task_listbox.insert(tk.END, task)

# # Example usage
# root = tk.Tk()
# app = ToDoApp(root)
# root.mainloop()




# 38. Create a class CalculatorApp that uses tkinter to create a simple calculator GUI.


# import tkinter as tk

# class CalculatorApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Calculator")

#         self.result_var = tk.StringVar()

#         self.entry = tk.Entry(root, textvariable=self.result_var, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
#         self.entry.grid(row=0, column=0, columnspan=4, pady=10, padx=10)

#         buttons = [
#             ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
#             ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
#             ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
#             ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
#         ]

#         for (text, row, col) in buttons:
#             if text == '=':
#                 button = tk.Button(root, text=text, command=self.calculate)
#             else:
#                 button = tk.Button(root, text=text, command=lambda t=text: self.on_button_click(t))
#             button.grid(row=row, column=col, sticky='nsew', ipadx=10, ipady=10)

#         for i in range(5):
#             root.grid_rowconfigure(i, weight=1)
#         for i in range(4):
#             root.grid_columnconfigure(i, weight=1)

#     def on_button_click(self, button_text):
#         current_text = self.result_var.get()
#         self.result_var.set(current_text + button_text)

#     def calculate(self):
#         try:
#             expression = self.result_var.get()
#             result = eval(expression)
#             self.result_var.set(result)
#         except Exception as e:
#             self.result_var.set("Error")

# # Example usage
# root = tk.Tk()
# app = CalculatorApp(root)
# root.mainloop()







# 39. Create a class LoginApp that uses tkinter to create a login form GUI.

# import tkinter as tk

# class LoginApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Login Form")

#         tk.Label(root, text="Username").grid(row=0, column=0, padx=10, pady=10)
#         tk.Label(root, text="Password").grid(row=1, column=0, padx=10, pady=10)

#         self.username_entry = tk.Entry(root)
#         self.username_entry.grid(row=0, column=1, padx=10, pady=10)

#         self.password_entry = tk.Entry(root, show="*")
#         self.password_entry.grid(row=1, column=1, padx=10, pady=10)

#         self.login_button = tk.Button(root, text="Login", command=self.login)
#         self.login_button.grid(row=2, column=1, pady=20)

#         self.message_label = tk.Label(root, text="")
#         self.message_label.grid(row=3, column=0, columnspan=2, pady=10)

#     def login(self):
#         username = self.username_entry.get()
#         password = self.password_entry.get()
#         if username == "admin" and password == "password":
#             self.message_label.config(text="Login successful", fg="green")
#         else:
#             self.message_label.config(text="Invalid credentials", fg="red")

# # Example usage
# root = tk.Tk()
# app = LoginApp(root)
# root.mainloop()

# 40. Create a class WeatherApp that uses tkinter to create a weather information GUI.


# import tkinter as tk
# import random

# class WeatherApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Weather App")

#         self.city_entry = tk.Entry(root, width=50)
#         self.city_entry.pack(pady=10)

#         self.get_weather_button = tk.Button(root,fg=("black") ,text="Weather Condition", command=self.get_weather)
#         self.get_weather_button.pack(pady=5)

#         self.weather_label = tk.Label(root, text="",bg="black",fg="Red" ,font=("Arial", 16))
#         self.weather_label.pack(pady=20)

#     def get_weather(self):
#         city = self.city_entry.get()
#         if city:
#             # Simulating weather data
#             temperature = random.randint(-10, 35)
#             conditions = random.choice(["Sunny", "Cloudy", "Rainy", "Snowy"])
#             weather_info = f"The weather in {city} is {temperature}°C with {conditions} conditions."
#             self.weather_label.config(text=weather_info)
#         else:
#             self.weather_label.config(text="Please enter a city name.")

# # Example usage
# root = tk.Tk()
# app = WeatherApp(root)
# root.mainloop()
























