Blue = My answers
1.  What will be printed from this script?

''' This program gives information about the number of available cars, available drivers, empty cars, people
they can transport, people to carpool today, and people in each car. '''

# My variables
cars = 100 # The number of cars the company has
space_in_a_car = 4.0 # The amount of space in a car
drivers = 30 # The amount of drivers the company has employed
passengers = 90 # The amount of passengers needed to be transported
cars_not_driven = cars - drivers # The number of cars not used
cars_driven = drivers # The number of cars being driven/used
carpool_capacity = cars_driven * space_in_a_car # The number of people able to carpooled today
average_passengers_per_car = passengers // cars_driven # The average number of people in each car

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")


# From this script, this will be printed:

There are 100 cars available.
There are only 30 drivers available.
There will be 70 empty cars today.
We can transport 120 people today.
We have 90 to carpool today.
We need to put about 3 in each car.

2.  In the above program add comments that you think would help explain
the code.  Be sure to use all three types of comments.

3.  In the program below which of lines of code contain syntax errors?

	pi = 3.14159
	area = pi * r * r
	r = 6.5
	r + 5 = r_new

''' Lines 2 and 4 contain syntax errors. Line 2 is a syntax error because r was assigned a value after line 2, so Python won't
apply the variable r to the line before it, because code is always read from left to right, and from top to bottom. Line 4 is a
syntax error because variables can't have special characters in them, and r + 5, has the special character, +, or the plus sign,
so it will have a syntax error.'''
