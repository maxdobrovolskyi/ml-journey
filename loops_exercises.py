import random

# 1
num = int(input("enter number: "))

if num > 0:
    print("+")
elif num < 0:
    print("-")
else:
    print("0")


# 2
total = 0
for i in range(1, 101):
    if i % 5 == 0:
        total += i

print(total)


# 3
op = input("enter op: ")
first_num = int(input("enter first num: "))
second_num = int(input("enter second num: "))
match op:
    case "+":
        print(first_num + second_num)
    case "-":
        print(first_num - second_num)
    case "*":
        print(first_num * second_num)
    case "/":
        if second_num == 0:
            print("error")
        else:
            print(first_num / second_num)
    case _:
        print("error")

# 4

ran = random.randrange(1, 11)
guess = int(input("Enter your number: "))
while guess != ran:
    if guess > ran:
        print("big")
        guess = int(input("Enter your number: "))
    elif guess < ran:
        print("small")
        guess = int(input("Enter your number: "))
print("you won")


# 5
star = "*"

for i in range(1, 6):
    print(i * star)
