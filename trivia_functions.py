import json
import os

# Let the user know which questions they got right and which they got wrong
def errors(wrongs, score, total):
# calculate the user's percentage
    percent = score / len(total) * 100

# retrieve the list of original questions and answers
    with open("game.json", "r") as quiz:
        checks = json.load(quiz)

# loop through the user input    
    for wrong in wrongs:
        for key, value in wrong.items():
# check for incorrect answers
            if key in checks and checks[key] != value:
                print(f"{key}: You got this wrong. The correct answer is '{checks[key]}' \n")
# check for correct answers
            else:
                print(f"Your answer was correct: {key}: {checks[key]}) \n")
        break
# Print each user's score before allowing someone else to play
    print(f"Your score is {score} out of 10 or {percent}%")

# Store scors
def record_score(name, score):
# Create the dictionary containing the data to save
    attempt = {name: score}
# - Check if the file exists, and read existing data if it does
    if os.path.exists("score.json"):
        with open("score.json", "r") as scoreboard:
            try:
                data = json.load(scoreboard)
            except json.JSONDecodeError:
                data = [] 
    else:
        data = []
# - Append the new entry to the data
    data.append(attempt)
# - Write the updated data back to the JSON file
    with open("score.json", "w") as scoreboard:
        json.dump(data, scoreboard, indent=4)