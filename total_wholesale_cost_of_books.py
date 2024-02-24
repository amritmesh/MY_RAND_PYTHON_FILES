# This program calculates the total wholesale cost of books for a bookstore
# My variables
cover_price = 24.95 # cost of book
discount = (cover_price * 0.4) # discount on book
shipping_cost_1 = 3.00 # shipping cost for first copy of book
shipping_cost_2 = 0.75
''' shipping cost for each additional copy of book
after first one'''
copies = 60 # number of copies needed

amt = cover_price - discount + shipping_cost_1
amt2 = 59 * shipping_cost_2
# My calculation/final answer
print("The total wholesale cost is " , '$' , amt + amt2, '.')
