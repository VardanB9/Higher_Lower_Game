from art import logo
from art import vs
from game_data import data
import random
from replit import clear

total_point = 0
higher_follower_count = ""
game = ""

random_number_a = random.randint(0, 51)
random_number_b = random.randint(0, 51)
inst_acc_a = data[random_number_a].get("follower_count")
inst_acc_b = data[random_number_b].get("follower_count")
 
print(data[random_number_a].get("name"))

while game != "loose":
    clear()
    print(logo)
    print(f"Total point: {total_point}")
    if inst_acc_a > inst_acc_b:
        higher_follower_count = "a"
    else:
        higher_follower_count = "b"

    print(f"Compare A:{data[random_number_a].get('name')}, a {data[random_number_a].get('description')}, from {data[random_number_a].get('country')}")

    print(vs)

    print(f"Against B:{data[random_number_b].get('name')}, a {data[random_number_b].get('description')}, from {data[random_number_b].get('country')}")

    user_choice = str(input("Who has more followers? Type 'A' or 'B':"))

    if user_choice == higher_follower_count:
        total_point += 1
        random_number_a = random_number_b
        inst_acc_a = inst_acc_b
        random_number_b = random.randint(0, 51)
        inst_acc_b = data[random_number_b].get("follower_count")
        
    else:
        game = "loose"
        print(f"Sorry, that's wrong. Final score:{total_point}")
    
