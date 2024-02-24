def main():
    guess = int(input('Guess my age: '))

    if guess == 13:
        print('You are correct!')
    elif guess > 13:
        print('Your guess is too high.')
    else:
        print('Your guess is too low.')
main()
