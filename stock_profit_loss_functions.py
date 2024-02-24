def main():
    intro()

    number_of_shares_bought = (int(input("Please enter amount of shares you bought (as an integer or decimal): ")))
    share_price_bought = (float(input("Please enter the price per share (as an integer or decimal): ")))
    commission_bought = (float(input("Please enter the commission rate (as an integer or decimal): ")))

    buy = buying(number_of_shares_bought, share_price_bought, commission_bought)
    print_info(number_of_shares_bought, share_price_bought, commission_bought, buy)

    number_of_shares_sold = (int(input("Please enter the amount of shares you sold (as an integer or decimal): ")))
    share_price_sold = (float(input("Please enter the price per share (as an integer or decimal): ")))
    commission_sold = (float(input("Please enter the commission rate (as an integer or decimal): ")))

    sell = selling(number_of_shares_sold, share_price_sold, commission_sold)
    print_info(number_of_shares_sold, share_price_sold, commission_sold, sell)

    total_difference = buy - sell
    display(total_difference)

def intro():
    print("""Hi! This is a program that calculates \
whether you made a profit or lost money \
in your process of buying and selling stocks! \
Please enter the info asked below \
to find out whether you were a smart stock buyer and seller!""")

def buying(num_bought, share_bought, com_bought):
    total_purchase_price = (num_bought * share_bought) + \
                       ((num_bought * share_bought) * (com_bought))
    return total_purchase_price

def print_info(num_shares, share_price, comm, total):
    print("This is the information you entered:")
    print( num_shares,'shares.')
    print("The price per share is ${0:.2f}.".format(share_price))
    print("The rate of commission is {0:.0%}.".format(comm))
    print("The total price with commission is ${0:.2f}.".format(total))

def selling(num_sold, share_sold, comm_sold):
    total_sale_price = (num_sold * share_sold) + \
                   ((num_sold * share_sold) * (comm_sold))
    return total_sale_price

def display(tot):
    if tot > 0:
        print('''Congratulations! You made a profit of ${0:.2f}.'''.format(tot))
    elif tot == 0:
        print('''Sorry! You did not make or lose any money.'''.format(tot))
    else:
        tot = -1 * tot
        print('''Better luck next time! You lost ${0:.2f}.'''.format(tot))

main()
