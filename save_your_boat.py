import random

desc1 = "\t\t1) You have a boat that have 5 lives end it will drwn"
desc2 = "\t\t2) You should guess the word by choosing a letter from the English alphabet"
desc3 = "\t\t3) If you got a letter wrong you will lose a live"
desc5 = "\t\t4) If you guess everything right you will win"
desc4 = "\t\t5) When you guess the letter right you will be provided with the update word"
desc6 = "\t\t6) If you finish your lives and did not guess the word you will lose"
desc7 = "\t\t7) To quit you can write exit"

print("\tWelcome To Save Boat Game :D \n\n\tDescription :\n\n {}\n {}\n {}\n {}\n {}\n {}\n {}".format(desc1,desc2, desc3, desc4, desc5, desc6, desc7)) 

answer = input("\n\nWanna play ? (y,n) : ")

hints = ["apple" , "orange" , "banana" ,  "lemon" , "mango"]

def give_hint(hints_given):
    hints = ["food", "maybe red, green, yellow"]
    if hints_given == 0:
        print("Hint:", hints[0])
    elif hints_given == 1:
        print("Hint:", hints[1])
    elif hints_given == 2:
        print("Hint: It starts with the letter 'a'")

def save_your_boat():
    word_to_guess = random.choice(hints)
    word_display = "_" * len(word_to_guess)
    lives = 5
    hints_given = 0

    print("Let's play the game!\n")

    while lives > 0:
        print("Word to guess:", " ".join(word_display))
        print("Boat lives:", lives)
        
        guess = input("Choose a letter: ").lower()

        if guess == "exit":
            print("Exiting the game.")
            break

        if len(guess) != 1 or not guess.isalpha():
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
            lives -= 1
            print("You got it wrong.")
            give_hint(hints_given)
            hints_given += 1
            if lives == 0:
                print("Game Over! You ran out of lives. The word was:", word_to_guess)
                break

        if "_" not in word_display:
            print("Congratulations! You guessed the word:", word_to_guess)
            print("You Win!")
            break


if __name__ == "__main__":
    if answer.lower() == 'y':
        save_your_boat()
    else:
        print("Maybe next time! Bye!")
