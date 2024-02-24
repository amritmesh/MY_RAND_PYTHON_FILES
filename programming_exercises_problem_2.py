def main():
    length_1 = float(input("Enter the length of the first rectangle: "))
    width_1 = float(input("Enter the width of the first rectangle: "))
    length_2 = float(input("Enter the length of the second rectangle: "))
    width_2 = float(input("Enter the width of the second rectangle: "))

    rectangle_1 = calculation(length_1, width_1)
    rectangle_2 = calculation(length_2, width_2)

    if rectangle_1 > rectangle_2:
        print("The first rectangle has a greater area than the second rectangle.")
    elif rectangle_2 > rectangle_1:
        print("The second rectangle has a greater area than the first rectangle.")
    elif rectangle_1 == rectangle_2:
        print("The first and the second rectangles have the same area.")

def calculation(length, width):
    area = length * width
    return area

main()
    
