import random

def monty_hall(rounds, switch):
    # Initialize counters for wins and losses
    wins = 0
    losses = 0

    for round_num in range(1, rounds + 1):
        # Step 1: Randomly place the car behind one of the doors
        doors = [0, 0, 0]  # 0 means no car, 1 means car
        car_position = random.randint(0, 2)
        doors[car_position] = 1
        
        # Step 2: Automatically choose a random door (simulate user's choice)
        user_choice = random.randint(0, 2)  # Random choice between door 0, 1, or 2
        print(f"Round {round_num} - Your automatic choice is door {user_choice + 1}")
        
        # Step 3: Reveal a wrong door
        possible_reveal = [i for i in range(3) if i != user_choice and doors[i] != 1]
        revealed_door = random.choice(possible_reveal)
        print(f"I reveal door {revealed_door + 1} and there is no car behind it.")
        
        # Step 4: If the user is switching, change their choice
        if switch:
            user_choice = 3 - user_choice - revealed_door  # The remaining door is the switch option
        
        # Step 5: Reveal if the user won
        if doors[user_choice] == 1:
            print("Congratulations! You won the car!")
            wins += 1
        else:
            print("Sorry, no car behind that door. Better luck next time!")
            losses += 1
        
        print(f"Current score: {wins} Wins, {losses} Losses\n")
    
    # Final results after all rounds
    print(f"Game Over! Final score: {wins} Wins, {losses} Losses")

if __name__ == "__main__":
    print("How many rounds would you like to play?")
    rounds = int(input())  # Input for number of rounds
    
    print("Do you want to switch your answer every time? (yes or no)")
    switch_choice = input().lower()
    
    # Convert input to boolean
    switch = switch_choice == "yes"
    
    monty_hall(rounds, switch)
