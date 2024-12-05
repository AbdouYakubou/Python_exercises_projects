import random
def get_choices():


    player_choice = int(input("Enter a number from 1 to 10: "))
    if player_choice < 1 or player_choice > 10:
        print("please enter a valid input between 1 to 10")
        return get_choices()
    options = [1,2,3,4,5,6,7,8,9,10]
    computer_choice = random.choice(options)
    choice = {"player":player_choice, "computer":computer_choice}
    return choice



def check_sum(player,computer,):
    print(f"you chose {player}, computer chose {computer}")
    total = player + computer
    print(f"the sum is : {total}")
    result = "even" if total % 2 == 0 else "odd"
 
    print(f"The sum is {result}")


choice = get_choices()
result = check_sum(choice["player"], choice["computer"])
print(result)





