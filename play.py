import trivia_classes
import trivia_functions as funcs

# create instances of classes
trivia = trivia_classes.Game()
scoring = trivia_classes.UserInput()

# create a variable called instructions and assign it "y" This allows us to create the loop for letting multiple users play.
instructions = "y"

# create a loop so that as many users as possible can play the game
while instructions == "y":
# Provide the user with instructions on how the game works
    trivia.welcome()
# get the player's name
    user = trivia.username()
# ask the questions and capture responses. Also grab the list of questions the user chose to answer for calculation purposes.
    entries, user_total = trivia.ask()
# check if questions were correctly answered
    incorrect, tally = scoring.marking(entries)
# display incorrectly answered  questions with correct answers
    funcs.errors(incorrect, tally, user_total)
# record the scores
    funcs.record_score(user, tally)
# check if other users still want to play
    play_again = ""
    while play_again not in ["y", "n"]:
        play_again = input("Does anyone else want to play? Type 'y' for yes and 'n' for no. ").lower()
        if play_again.lower() == "n":
            instructions = "n"
            break

# display results
scoring.results()