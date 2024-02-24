def main():
    weight_input = float(input('Enter your weight (in pounds): '))
    height_input = float(input('Enter your height (in inches): '))

    calc_bmi = calc(weight_input, height_input)
    print_info(calc_bmi)

def calc(weight, height):
    bmi = (weight * 703) / (height ** 2)
    return bmi

def print_info(bmi_info):
    print("Your bmi is {0:.2f} lb/in ** 2.".format(bmi_info))

main()
