def main():
    MAX = 10
    dishes = [None] * MAX
    count = 0
    while(count < MAX):
        food = input("Please enter a dish: ")
        dishes[count] = food
        count = count + 1
        print(count)
        print(dishes)

main()
    
