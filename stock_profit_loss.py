number_of_shares_1 = (int(input("Enter amount of shares you bought: ")))
share_price_1 = (float(input("Enter the price per share: ")))
commission_1 = (float(input("Enter the commission rate: ")))
total_purchase_price = (number_of_shares_1 * share_price_1) + ((number_of_shares_1 * share_price_1) * (commission_1))
print("This is the information you entered: ")
print("This is the number of shares you bought: ", number_of_shares_1)
print("This is the price per share: ", share_price_1)
print("This is the rate of commission: ", commission_1)
print("This is the total purchase price with commission: ", total_purchase_price)

number_of_shares_2 = (int(input("Enter the amount of shares you sold: ")))
share_price_2 = (float(input("Enter the price per share: ")))
commission_2 = (float(input("Enter the commission rate: ")))
total_sale_price = (number_of_shares_2 * share_price_2) + ((number_of_shares_2 * share_price_2) * (commission_2))
print("This is the information you entered: ")
print("This is the number of shares you sold: ", number_of_shares_2)
print("This is the price per share: ", share_price_2)
print("This is the rate of commission: ", commission_2)
print("This is the total sale price with commission: ", total_sale_price)

profit = float(total_purchase_price - total_sale_price)

print("This is the amount of profit or loss you made: ", '$',profit)

if profit > 0:
    print('You made a profit.')

else:
    print('You lost money.')




