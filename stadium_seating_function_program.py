price_a = 15.00
price_b = 12.00
price_c = 9.00
def main():
    intro()
    class_a = int(input('Enter the amount of Class A seatings sold: '))
    a(class_a)
    class_b = int(input('Enter the amount of Class B seatings sold: '))
    b(class_b)
    class_c = int(input('Enter the amount of Class C seatings sold: '))
    c(class_c)

def intro():
    print('''This program takes your choice of the amount of seatings sold \
for each class of seatings, and gives the amount of income made for each \
class of seating. For your reference, class A seatings are $15.00 each, \
class B seatings are $12.00 each, and class C seatings are $9.00 each.''')

def a(seats_a):
    result_a = seats_a * price_a
    print('The income made for the Class A seatings is ${0:.2f}.'.format(result_a))
    
def b(seats_b):
    result_b = seats_b * price_b
    print('The income made for the Class B seatings is ${0:.2f}.'.format(result_b))

def c(seats_c):
    result_c = seats_c * price_c
    print('The income made for the Class C seatings is ${0:.2f}.'. format(result_c))

main()
    
    
