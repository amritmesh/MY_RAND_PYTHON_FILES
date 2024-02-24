print("""Hi! This is a program that calculates whether you made a profit or lost money \
in your process of buying and selling stocks! Please enter the info asked below \
to find out whether you were a smart stock buyer and seller!""")

number_of_shares_1 = (float(input("Please enter amount of shares you bought (as an integer or decimal): ")))
share_price_1 = (float(input("Please enter the price per share (as an integer or decimal): ")))
commission_1 = (float(input("Please enter the commission rate (as an integer or decimal): ")))
total_purchase_price = (number_of_shares_1 * share_price_1) + \
                       ((number_of_shares_1 * share_price_1) * (commission_1))

print("This is the information you entered:")
print("You bought ",number_of_shares_1,'shares.')
print("The price per share is ${0:.2f}.".format(share_price_1))
print("The rate of commission is {0:.0%}.".format(commission_1))
print("The total purchase price with commission is ${0:.2f}.".format(total_purchase_price))

number_of_shares_2 = (float(input("Please enter the amount of shares you sold (as an integer or decimal): ")))
share_price_2 = (float(input("Please enter the price per share (as an integer or decimal): ")))
commission_2 = (float(input("Please enter the commission rate (as an integer or decimal): ")))
total_sale_price = (number_of_shares_2 * share_price_2) + \
                   ((number_of_shares_2 * share_price_2) * (commission_2))

print("This is the information you entered: ")
print("You sold ",number_of_shares_2,'shares.')
print("The price per share is ${0:.2f}.".format(share_price_2))
print("The rate of commission is {0:.0%}.".format(commission_2))
print("The total sale price with commission is ${0:.2f}.".format(total_sale_price))

profit = float(total_purchase_price - total_sale_price)

print("The amount of profit or loss you made is ${0:.2f}.".format(profit))

if profit > 0:
    print('Congratulations! Since the amount you made is positive, you made a profit.')

else:
    print('Better luck next time! Since the amount you made is negative, you lost money.')
