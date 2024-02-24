def main():
    test_score = 

    while repeat == "y":
        test_1 = float(input('Enter your average for your first test: % '))
        test_2 = float(input('Enter your average for your second test: % '))
        test_3 = float(input('Enter your average for your third test: % '))
        calc = average(test_1, test_2, test_3)

        if calc > 95:
            print('Congratulations! You achieved an average test score higher than 95%!')
            repeat = input("""Do you want to calculate another test grade average?
(Type in a y for "yes" and an n for "no"): """)

        else:
            print('Sorry! You achieved an average test score lower than 95%! Good try anyway!')
            repeat = input("""Do you want to calculate another test grade average?
(Type in a y for "yes" and an n for "no"): """)

    if repeat == "n":
        print("Thanks for using this average calculator!")

def average(grade_1, grade_2, grade_3):
    average_calc = (grade_1 + grade_2 + grade_3) / 3
    print('Your average of all three tests is %{0:.2f}.'.format(average_calc))
    return average_calc

main()
