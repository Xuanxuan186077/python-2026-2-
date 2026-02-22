import random
low = 1
high = 1000000000
count = 0
the_answer = random.randint(low, high)
print("Welcome to the Guess the Number Game!")
print("I have selected a number between 1 and 1,000,000,000.")
print("Try to guess it in as few attempts as possible!")
print("You can also type 'exit' to quit the game.")
while True:
    the_mid_number = (low + high) // 2
    if the_mid_number > the_answer:
        high = the_mid_number - 1
    elif the_mid_number < the_answer:
        low = the_mid_number + 1
    else:
        print(f"Congratulations! You've guessed the number {the_answer} in {count} attempts.")
        break
    count += 1
    #print(f"Is your number {the_mid_number}?")