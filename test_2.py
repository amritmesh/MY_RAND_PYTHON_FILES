friend_list = []
name = input("Enter the name of another friend (type xxx to exit and see your friend list): ")
while name != 'xxx':
    friend_list.append(name)
    name = input("Enter the name of another friend (type xxx to exit and see your friend list): ")
    print(friend_list)
print("This is your finished friend name list:")
print(friend_list)
