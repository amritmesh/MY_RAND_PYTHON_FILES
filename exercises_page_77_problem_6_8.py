# Question 6
purchase = (float(input("Please enter the amount of your purchase: ")))

state_sales_tax = (purchase * .04)
county_sales_tax = (purchase * .02)
total_sales_tax = state_sales_tax + county_sales_tax
total_sale_price = purchase + total_sales_tax

print('These are your purchase details: ')
print('The amount of your purchase is ${0:.2f}.'.format(purchase))
print('The amount of state sales tax is ${0:.2f}.'.format(state_sales_tax))
print('The amount of county sales tax is ${0:.2}.'.format(county_sales_tax))
print('The total sales tax is ${0:.2f}.'.format(total_sales_tax))
print('The total sale price is ${0:.2f}.'.format(total_sale_price))

#Question 8
meal_purchase = (float(input('Please ONLY enter the price of your meal: ')))

tip = meal_purchase * .15
sales_tax = (meal_purchase + tip) * .07
total_sale_price = meal_purchase + tip + sales_tax

print('These are your meal purchase details: ')
print('The tip on your meal purchase is ${0:.2f}.'.format(tip))
print('The sales tax on your meal purchase is ${0:.2f}.'.format(sales_tax))
print('The total sale price of your meal is ${0:.2f}.'.format(total_sale_price))
