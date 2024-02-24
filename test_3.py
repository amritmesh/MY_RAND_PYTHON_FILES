grade_list = []
total = 0
grade = float(input("Enter a grade (type -9999 to exit and see your grade list): "))
while (grade != -9999):
    total = total + grade
    grade_list.append(grade)
    grade = float(input("Enter another grade (type -9999 to exit and see your grade list): "))
print("This is your finished grade list:")
print(grade_list)
average = total / len(grade_list)
print("Your average is: %{0:.2f}.".format(average))

