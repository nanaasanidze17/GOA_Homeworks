#Task 1

def two_sum(num1, num2):
    print(num1 + num2)

two_sum(3, 7)


#Task 2

def sum(num1, num2, num3):
    print(num1 * num2 * num3)

sum(5, 2, 7)

#Task 3

def greet(first_name, last_name):
    return f"Hello, {first_name} {last_name}!"

first_name = "Nana"
last_name = "Asanidze"
greeting = greet(first_name, last_name)

print(greeting)



#Task 4

def sum_two(a, b):
    return a + b

num1 = 3
num2 = 2
result = sum_two(num1, num2)

print(result)


#Task 5

def sum(a, b, c):
    return a * b * c

num1 = 5
num2 = 6
num3 = 7
result = sum(num1, num2, num3)

print(result)


#Task 6

def food_(food_list):
    for food in food_list:
        print(food)


food = ["pizza", "fries", "vegetable", "soup"]
food_(food)


#Task 7

def num(num_list):
    for number in num_list:
        print(number)


number = [1, 5, 7, 3, 9]
num(number)

