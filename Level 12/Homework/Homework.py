#Task 1
Guess = int(input("Enter your guess:"))
if Guess == 1:
    print("Your Guess is incorrect!")

elif Guess == 2:
    print("Your Guess is incorrect!")

elif Guess == 3:
   print("Your Guess is incorrect!")

elif Guess == 4:
    print("Your Gues is incorrect!")

elif Guess == 5:
    print("Youa are Correct!")

elif Guess == 6:
    print("You are incorrect!")

#Task 2
sum = 0
for i in range(1, 100):
    sum = sum + 1

    print(sum)

#Task 3
total_sum = 0

for i in range(1000):
    if i not in range(500, 600):

        total_sum += i

print(total_sum)

#Task 4
number = 5
while True:
    num = int(input("Enter a number here: "))
    if num == number:
        print("Correct")
        break
    else:
        print("Incorrect")

#Task 5
i = 1
mult1 = 1

while i < 10:
    mult1 = mult1 * i
    i = i + 1

    print(mult1)  
#Task 6
num = int(input("Enter number here: "))

if num % 2 == 0:
    print("This number is even")

elif num % 2 == 1:
    print("This number is odd")

#Task 6
Grade = int(input("Enter Your Grade:"))

if Grade <= 90 and Grade <= 100:
    print("Grade A")

elif Grade <= 80 and Grade <= 89:
    print("Grade B")

elif Grade <= 70 and Grade <= 79:
    print("Grade C")  

elif Grade <= 60 and Grade <= 69:
    print("Grade D")

elif Grade <= 59:
    print("Grade F")


