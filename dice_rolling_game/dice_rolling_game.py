# dice rolling game

import random
life = int(input("How many time do you want to roll? "))
count = 1
#infinite loop
while True:
    #take input from user
    user_input = input("Roll the dice? (y/n): ").lower()
    if count >= life: #logic for counter
        print("Your roll completed! Play again.")
        exit()
    else:
        if user_input == 'y':
            result = (random.randint(1, 6), random.randint(1, 6))#generate two number and storing it as tuple
            count = count + 1 #incrementing the count
            print(result)
        elif user_input =='n': #logic for stop playing
            print("Thanks for Playing! ")
            exit()
        else:
            print("Invalid choice!")

#end of program