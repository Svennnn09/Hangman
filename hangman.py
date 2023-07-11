import random as r
import turtle as t
from words import word_list
from words import s_alphabet

t.penup()
t.sety(-360)
t.setx(180)
t.left(90)
t.pendown()

word = ""
guesses = 9

def man():
    if guesses == 9:
        t.forward(500)
        t.left(90)
    if guesses == 8:
        t.forward(200)
        t.left(90)
    if guesses == 7:
        t.forward(50)
        t.right(90)
    if guesses == 6:
        t.circle(50)
        t.penup()
        t.left(90)
        t.forward(100)
        t.pendown()
    if guesses == 5:
        t.forward(200)
        t.left(45)
    if guesses == 4:
        t.forward(75)
        t.right(180)
        t.forward(75)
        t.left(90)
    if guesses == 3:
        t.forward(75)
        t.left(180)
        t.forward(75)
        t.left(45)
    if guesses == 2:
        t.forward(175)
        t.left(45)
        t.right(180)
        t.forward(75)
        t.left(180)
    if guesses == 1:
        t.forward(75)
        t.left(90)
        t.forward(75)
        t.left(180)
        t.forward(75)
        t.left(45)

def valid_word():
    global word
    word = r.choice(word_list)
    while "-" in word or " " in word:
        word = r.choice(word_list)
    return word

valid_word()

word_length = len(word)
correct_letters = list(word)
blanks = []

for n in range(word_length):
    blanks.append('_')

print("")
print(blanks)

while blanks != correct_letters and guesses > 0:
    w_check = False
    print("")
    print("If you think you know the correct word, enter I know")
    letter = input("Enter a letter: ")
    while letter not in s_alphabet and letter != "I know":
        print("")
        letter = input("Either you've already guessed that letter or it is not a letter, please enter another letter: ")
    if letter == "I know":
        w_check = True
        guess_word = input("Enter the word: ")
        if guess_word == word:
            for n in range(word_length):
                blanks.pop(n)
                blanks.insert(n, correct_letters[n])
            print("")
            print("Your guess is correct")
            print(blanks)
        if guess_word != word:
            print("")
            print("Your guess is incorrect")
            print(blanks)
            man()
            guesses -= 1
    if w_check == False:
        if letter in correct_letters:
            for n in range(word_length):
                if letter == correct_letters[n]:
                    blanks.pop(n)
                    blanks.insert(n, letter)
            s_alphabet.remove(letter)
            print("")
            print("You've guessed correctly!")
            print(blanks)
        else:
            s_alphabet.remove(letter)
            print("")
            print("You've guessed incorrectly")
            print(blanks)
            man()
            guesses -= 1
    if blanks == correct_letters:
        print("")
        print("Congrats! You have won!")
        print("The word is", word)
        print("You had", guesses, "guesses left")
    elif guesses == 0:
        print("")
        print("Sorry, you've lost the game, the man has died")
        print("The word is", word)

while guesses >= 0:
    t.penup()