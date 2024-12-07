import random
min_value = int(input("Enter the minimum number: "))
max_value = int(input("Enter the maximum number: "))
attempts = int(input("Enter the number of attempts: "))

if(min_value>max_value):
    print("Minimum number should be less than maximum number")
    exit()

answer = random.randint(min_value, max_value)

while attempts > 0:
    guess = int(input("Enter your guess: "))
    if guess == answer:
        print("Congratulations! You guessed the correct number")
        break
    elif guess < answer:
        print("Your guess is too low")
    else:
        print("Your guess is too high")
    attempts = attempts - 1
    if attempts == 0:
        print("You have run out of attempts. The correct number was " + str(answer))
        break
