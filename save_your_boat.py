import random

def welcome_message():
    
    welcoming_message= "Welcome To Save Boat Game :D"
    desc = "Description: "
    desc1 = "1) You have a boat that have 5 lives end it will drwn"
    desc2 = "2) You should guess the word by choosing a letter from the English alphabet"
    desc3 = "3) If you got a letter wrong you will lose a live"
    desc5 = "4) If you guess everything right you will win"
    desc4 = "5) When you guess the letter right you will be provided with the update word"
    desc6 = "6) If you finish your lives and did not guess the word you will lose"
    desc7 = "7) To quit you can write exit"

    print("\t{} \n\n\t{} \n \n \t\t{} \n\t\t{} \n\t\t{} \n\t\t{} \n\t\t{} \n\t\t{} \n\t\t{} \n".format(welcoming_message,desc,desc1,desc2,desc3,desc4,desc5,desc6,desc7)) 

welcome_message()

question = input("Wanna Play ? (y,n) ? ")

fruit_hint = ['apple' , 'melon' , 'mango' , 'olive', 'lemon']


def give_hint(lives):
    hints = ["  - food", "  - maybe red, green, yellow"]

    
    
    print("guess this: \n _ _ _ _ _")
    print("\t\t Hint: \n\t\t", hints[0] , "\n\t\t" , hints[1])

def guess_letter():
    word_to_guess = random.choice(fruit_hint)
    word_display = "_" * len(word_to_guess)
    lives = 5
    hints_given = 0

    print("Let's play the game!\n")

    give_hint(lives)

    while lives > 0:
        print("Word to guess:", " ".join(word_display))
        print("Boat lives:", lives)
        
        guess = input("Choose a letter: ").lower()

        if guess == "exit":
            print("Exiting the game.")
            break

        if len(guess) != 1:
            print("Please enter a single letter.")
            continue

        if guess in word_to_guess:
            print("Yay! You got it right.")
            updated_word_display = ""
            for i in range(len(word_to_guess)):
                if word_to_guess[i] == guess:
                    updated_word_display += guess
                else:
                    updated_word_display += word_display[i]
            word_display = updated_word_display

        else:
            print("You got it wrong.")
            lives -= 1
            if lives == 1:
                print("Here's a hint:")
                print("  - Hint: It starts with the letter '{}'".format(word_to_guess[0]))

            if lives == 0:
                print("Game Over! You ran out of lives. The word was:", word_to_guess)
                break

        if "_" not in word_display:
            print("Congratulations! You guessed the word:", word_to_guess)
            print("You Win!")
            break


if __name__ == "__main__":
    if question.lower() == 'y':
        guess_letter()
    else:
        print("Maybe next time! Bye!")