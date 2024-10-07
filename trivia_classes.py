import json
import os
import random
import statistics

class Game:
# Create a welcome message that also contains instructions on how the game is played
    def welcome(self):
# initialise begin
        begin = ""
# make sure the user is always prompted to enter y as long as they don't do so
        while begin != "y":
            begin = input("Welcome to ATrivia of Ice and Fire, a game to test how well you know the world of George RR Martin\'s A Song of Ice and Fire Universe. \n Please ensure that you use correct spellings when entering answers. \n Press the enter key after answering each question. \n Capitalise the first letter of each word you enter. \n The game cannot be stopped once started. However, feel free to press the key to input a blank entry if you do not know the answer. \n Enter the letter 'y' if you have read and understood these instructions: ").lower()
# make sure that users only proceed after acknowledging they understand how things work
            if begin.lower() != "y":
                print("Sorry. That input is invalid")
        return begin

# get the user's prefered name
    def username(self):
# initialise name
        self.name = ""
# ask for the name as long as the input is empty or is not made up of alphabetical characters
        while self.name == "" or not self.name.isalpha():
            self.name = input("What is your name? ")
# make sure this is not left blank
            if self.name == "":
                print("Oops. Name cannot be blank.")
# prevent users from entering non-alphabetical characters
            elif not self.name.isalpha():
                print("Your name can only contain alphabetical letters.")
        return self.name

# check how many questions the user wants to answer
    def range_num(self):
        while True:
# Ask the user for input
            quiz_range = input("You can only answer up to 10 questions. How many questions do you want to answer? Please only write a number between 1 and 10: ")
# Check if only digits have been entered
            if quiz_range.isdigit():
# Convert the string to int
                self.question_range = int(quiz_range)
# Check if the number is within the valid range
                if self.question_range in range(1, 11):
                    break
                else:
                    print("Invalid number of questions! Please choose a number between 1 and 10.")
            else:
                print("Invalid input. Only numerical values are accepted.")
        return self.question_range

# retrieve and display questions
    def ask(self):
# open json file containing questions
        quiz = open("game.json", "r")
# retrieve questions as a dictionary
        data = json.load(quiz)
# close the file
        quiz.close()
# convert dictionary keys to list to make shuffling possible
        rando = list(data.keys())
# shuffle the questions so that they appear to the user in any order
        random.shuffle(rando)
# allow the user to choose the number of questions they want to answer. This also calls the function that allows the user to choose this, and then enacts it.
        questions = rando[:self.range_num()]
# create an empty dictionary for storing user input
        answers = {}
# ask the questions
        for play in questions:
            ask = input(play)
# store user input
            answers[play] = ask
# returning answers allows us to access user input later on, while returning questions allows us to access only the list of questions asked, which is useful for calculating accurate percentages
        return answers, questions

class UserInput (Game):
# method to check if correct answers were entered
    def marking(self, results):
# create an empty list to store the incorrect questions
        self.mistakes = list()
# open the file containing questions and answers in order to check user answers
        quiz = open("game.json", "r")
        questions = json.load(quiz)
# close the file
        quiz.close()
# start counting the number of correct questions
        self.score = 0
# loop through questions
        for key, value in questions.items():
# increment score by 1 every time the user enters a correct answer
            if key in results and results[key] == value:
                self.score +=1
# create a list of questions that don't match
            else:
                self.mistakes.append(results)
# these values will be used in other functions later on
        return self.mistakes, self.score

# method to display results
    def results(self):
# retrieve the results
        scores = open("score.json", "r")
        results = json.load(scores)
# close the file for now
        scores.close()
# Convert list of dictionaries to a single dictionary
        combined = {key_list: value_list for dict_list in results for key_list, value_list in dict_list.items()}
 # assign the results to a variable and sort them from highest to lowest
        announce = dict(sorted(combined.items(), key=lambda item: item[1], reverse=True))
        print(f"{announce} \n")
# convert the scores to int to allow calculations
        avg = [int(avg_marks) for avg_marks in announce.values()]
# get the average
        user_avg =statistics.mean(avg)
        print(f"The average score is {user_avg}")
# empty the file so that the next round of players are starting with fresh scores
        scores = open("score.json", "w")
        pass
        scores.close()