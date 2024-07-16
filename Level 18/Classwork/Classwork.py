#Task 1
def greet(name):
    print("Hello", name)

greet("Nana")

#Task 2
def sum(num1, num2, num3):
   print(num1 + num2 + num3)

num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
num3=int(input("Enter third number:"))

sum(num1, num2, num3)

#Task 3

def print_numbers(start, end):
    for i in range(start, end):
        print(i)

print_numbers(1,6)
    

#Task 4

def info( Name ,  surname , study ):
    print(Name, surname, study)

Name = input("My Name Is:")
surname = input("My Surname Is:")
study  = input("I Study In:")

#Task 5

def sum(num1, num2, num3):
   return int(num1) * int(num2) * int(num3)

num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
num3=int(input("Enter third number:"))

x = sum(num1, num2, num3)

print(x)


#Task 7

def list_print(list1):
    for i in list1:
        print(i)

list_print=[1, 2, 3, 4, 5]
