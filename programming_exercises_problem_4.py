def main():
    month_date = int(input("Enter a month (in numeric form): "))
    day_date = int(input("Enter a day (in numeric form): "))
    year_date = int(input("Enter a a two_digit year (in numeric form): "))

    calculation_condition(month_date, day_date, year_date)

def calculation_condition(month, day, year):
    if month * day == year:
        print("The date you entered is magic!")
    else:
        print("The date you entered is not magic.")
main()
                    
    
    
