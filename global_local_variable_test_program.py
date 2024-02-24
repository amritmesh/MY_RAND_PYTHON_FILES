birds = 4000
def main():
    texas()
    california()

def texas():
    global birds
    birds = 2000
    
print('texas has', birds, 'birds.')

def california():
    print('california has', birds, 'birds.')

main()
