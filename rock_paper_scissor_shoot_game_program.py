import random

def main():
    print("""Hi! This is the "Rock, Paper, Scissor, Shoot! Game"! The play the
game, respond to all of the questions below. You will choose what item to use
in each game, and the computer will keep score of how many times you or the CPU
won. Enjoy!""")
    play_game = input('Do you want to play this game? (Yes/No): ')
    CPU_WIN_COUNT = 0
    USER_WIN_COUNT = 0
    while play_game == "Yes":
        CPU_choice = random.choice(["Rock!", "Paper!", "Scissor!"])
        user_choice = input('What is your choice of your item? (Rock!, Paper!, Scissor!): ')
        print('Rock, paper, scissor, SHOOT!')
        print("My item choice:", CPU_choice)
        print("Your item choice:", user_choice)
        outcome = win(CPU_choice, user_choice)
        if outcome == -1:
            CPU_WIN_COUNT = CPU_WIN_COUNT + 1
            print("I win!")
            print("My score is", CPU_WIN_COUNT, ".")
            print("Your score is", USER_WIN_COUNT, ".")
        elif outcome == 0:
            CPU_WIN_COUNT = CPU_WIN_COUNT + 1
            USER_WIN_COUNT = USER_WIN_COUNT + 1
            print("It's a tie!")
            print("My score is", CPU_WIN_COUNT, ".")
            print("Your score is", USER_WIN_COUNT,  ".")
        else:
            USER_WIN_COUNT = USER_WIN_COUNT + 1
            print("You win!")
            print("My score is", CPU_WIN_COUNT, ".")
            print("Your score is", USER_WIN_COUNT, ".")
        play_game = input('Do you want to play this game again?(Yes/No): ')

def win(CPU_choice, user_choice):
        if CPU_choice == user_choice:
            return 0
        elif CPU_choice == "Rock!" and user_choice == "Scissor!":
            return -1
        elif CPU_choice == "Paper!" and user_choice == "Rock!":
            return -1
        elif CPU_choice == "Scissor!" and user_choice == "Paper!":
            return -1
        else:
            return 1

main()
print("Thanks, for playing this game!")
            
            
        
        
        
        
