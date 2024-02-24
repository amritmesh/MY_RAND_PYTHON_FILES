import random

def main():
    guess_again = input('Do you want to guess my number? (yes/no): ')
    if guess_again == "yes":
        guess = int(input('Guess a number between 1 and 20: '))
        guess_number(guess)
    elif guess_again == "no":
        print('Thanks for playing this game!')
        
def guess_number(user_guess):
    choose_number = random.randint(1,20)
    while user_guess != choose_number:
        if user_guess > choose_number:
            print('Your guess is too high.')
        elif user_guess < choose_number:
            print('Your guess is too low.')
        guess_again = input('Do you want to guess my number? (yes/no): ')
        if guess_again == "yes":
            user_guess = int(input('Guess a number between 1 and 20: '))
        if user_guess == choose_number:
            print('You are correct!')
            main()

main()
            

