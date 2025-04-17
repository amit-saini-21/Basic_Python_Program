import random
import json
import os

# Generate a random number between 1 and 100
ran = random.randint(1, 100)

# JSON file for storing the lowest score
high_score_file = "guess.json"

# Check if high score file exists; if not, create one with a default score
if not os.path.exists(high_score_file):
    with open(high_score_file, "w") as f:
        json.dump({"score": {"lowest": 100}}, f)

# Read the current high score
with open(high_score_file, "r") as f:
    data = json.load(f)
    lowest = data["score"]["lowest"]

print("Welcome to the Number Guessing Game!")
print("Try to guess the number between 1 and 100.")
print(f"🏆 Current High Score (Least Attempts): {lowest} attempts")

guess_count = 0

#loop until the correct number is guessed
while True:
    #Prevent from the wrong input
    try:
       num=int(input("Enter a Number: ")) #taking input until the user not guessed the number successfully
       guess_count+=1
       if num==ran:
        print(f"🎉 Congratulations! You guessed the number in {guess_count} attempts.") #print when the number is guessed successfully
        new=input("Exiting....")
        # Check if the new score is the best
        if guess_count < lowest:
            print(f"🏆 New High Score! You set a record of {guess_count} attempts.")
            new=input("Exiting....")
            data["score"]["lowest"] = guess_count  # Update the high score

            # Save new high score to JSON
            with open(high_score_file, "w") as f:
                json.dump(data, f)
        break
       elif num<ran:
        print("Too low! Try Again.")
       else:
        print("Too High! Try Again.") 
    except ValueError:
       print("Invalid input! Please enter a valid integer.")
