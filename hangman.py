import random
from words import word_list

def get_word():
    word = random.choice(word_list)
    return word.upper()

def play(word):
    word_completion = "_"*len(word)
    tries = 6
    guessed = False
    guessed_letter = []
    guessed_word = []
    print("Welcome to Hangman! Let's Play!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Enter a guess or word:").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letter:
                print("You already guessed the letter",guess)
            elif guess not in word:
                print(guess,"not in the word")
                tries-=1
                guessed_letter.append(guess)
            else:
                print("Good job",guess, "is in the word")
                guessed_letter.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True

        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_word:
                print("you already guessed the word")
            elif guess != word:
                print(guess,"is not the word")
                tries -= 1
                guessed_word.append(guess)
            else:
                 guessed = True
                 word_completion = word

        else:
            print("Not a valid guess")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Congrats!!",word," is the correct answer")
    else:
        print("Sorry you ran out of tries")
        print("Word was",word)


def display_hangman(tries):
    stages = [
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,

                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,

                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,

                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,

                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,

                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,

                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]

def main():
    word = get_word()
    play(word)
    while input("Play agan (Y/N)").upper == "Y":
        word = get_word(word)
        play(word)

if __name__ == "__main__":
    main()