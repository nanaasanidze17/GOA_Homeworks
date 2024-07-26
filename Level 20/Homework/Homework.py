# Task 2

num1= 5
num2= 8

print(num1 + num2)

#Task 3

num1= "3"
num2= "6"

print(num1 + num2)

# concatenation is combining two or more strings into one.

#Task 4

num1= 9
num2= 4

print(num1/num2)

#Task 5
# ==
print(12 == 12) #True

# >
print(15 > 2) #True

# <
print(21 < 4) #False

# !=
print(23 != 23) #Fasle

# >=
print(4 >= 4) #True

# <=
print(10 <= 13) #True

#Task 6

print(6 + 4 <= 5 * 2)
print(3 / 2 == 1.5 * 1)
print(8 + 1 != 7 - 2)

#Task 7

#and
print(True and False)#False
print(False and True)#False
print(True and True)#True
print(False and False)#False

#or
print(True or False)#True
print(True or True)#True
print(False or True)#True
print(False or False)#False


#Task 8

print(5 != 6 or False) #True
print(True and 7 <= 3) #False
print(False and 6 >= 1) #False
print(3 == 3 or True) #True
print(4 > 2 and True) #True

#Task 9

for i in range(1,11):
    print(i)


#Task 10


    list1 = [1, 2, 3, 4, 5]

total_sum = 0

for i in list1:
    total_sum += i

print(total_sum)

#Task 11

str = "Hello, World!"

for i in str:
    print(i)


#Task 12
i = 1

while i <= 10:
    print(i)
    i += 1  

#Task 13

num = 1

while num <= 100:
    if 50 <= num <= 60:
    
        num += 1
        continue

    print(num)
    
    num += 1


#Task 15
num = int(input("Enter number: "))

if num % 5 == 0:
    print("This number can be divided by 5 ")

elif num % 3 == 0:
    print("This number can be dvided by 3")

#Task 18

#.lower()
print("HELLO".lower())

#.upper()
print("hello".upper())

#.capitalize()
print("hOMEWORK".capitalize())

#.find()
print("Dog".find("o"))

#len()
Colors = ["Red", "Blue", "Green", "Black"]
print(len(Colors))

#.append()
list = ["1", "2", "3", "4"]
list.append("5")
print(list)

#.insert()
list1 = ["one", "two", "four"]
list1.insert(2, "three")
print(list1)

#.pop()

fruit = ["peach", "strawberry", "banana", "potato"]
fruit.pop(3)
print(fruit)

