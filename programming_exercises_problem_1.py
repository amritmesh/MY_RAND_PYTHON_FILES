def main():
    num = int(input("Enter any whole number between 1 and 10: "))

    question_condition(num)
    
def question_condition(number):

    if number == 1:
        print("The Roman numeral version of your number is I.")
    elif number == 2:
        print("The Roman numeral version of your number is II.")
    elif number == 3:
        print("The Roman numeral version of your number is III.")
    elif number == 4:
        print("The Roman numeral version of your number is IV.")
    elif number == 5:
        print("The Roman numeral version of your number is V.")
    elif number == 6:
        print("The Roman numeral version of your number is VI.")
    elif number == 7:
        print("The Roman numeral version of your number is VII.")
    elif number == 8:
        print("The Roman numeral version of your number is VIII.")
    elif number == 9:
        print("The Roman numeral version of your number is IX.")
    elif number == 10:
        print("The Roman numeral version of your number is X.")
    elif number < 1:
        print("Your number is outside the 1 to 10 range. Enter another number.")
    elif number > 10:
        print("Your number is outside the 1 to 10 range. Enter another number.")
        
main()
