import random


def get_difficulty():
    word = ""
    difficulty = input(
        "Please select difficulty level, type e for easy, n for normal, and h for hard ")
    if difficulty == "e":
        word = random.choice(easy_list)
    elif difficulty == "n":
        word = random.choice(normal_list)
    elif difficulty == "h":
        word = random.choice(hard_list)
    return word



file = open("words.txt", "r")
text = file.read().split()


attempts = 0
max_attempts = 8


easy_list = [
    word.upper()
    for word in text
    if 4 <= len(word) <= 6
]

normal_list = [
    word.upper()
    for word in text
    if 6 <= len(word) <= 8
]

hard_list = [
    word.upper()
    for word in text
    if 8 <= len(word)
]


word = (get_difficulty())

word = list(word.upper())


hidden = []
for letter in word:
    hidden.append("_")


print(f"The mystery word is {len(word)} characters long.")
print("".join(word))


is_game_over = False
while not is_game_over:

   
    hidden_string = " ".join(hidden)
    print(f"You have {max_attempts - attempts} attempts remaining")

    guess = input("Please guess a letter: ")
    correct_guesses = []
    wrong_guesses = []
    statement = ""

    guess = guess.upper()

    if guess in word:
        for i in range(len(word)):
            character = word[i]  
            if character == guess:
                hidden[i] = word[i]
                word[i] = "_"
        print(f'correct! "{guess}" is in the word')
        print("".join(hidden))
        
    elif guess not in word:
        print(f'Nope! "{guess}" is not in this word')
        attempts += 1
      
    if (all('_' == char for char in word)):  
        print("Correct!")
        answer = "".join(hidden)
        print(f"The word was '{answer}'!")
        restart = input("would you like to play again? Y / N")
        if restart == "Y" or restart == "y"
            continue
        if restart == "N" or restart == "n"
            is_game_over = True


    if attempts >= max_attempts:
        print("sorry you are out of guesses and therefore out of time")
        restart = input("would you like to play again? Y/N ")
        if restart == "Y" or restart == "y"
            continue
        if restart == "N" or restart == "n"
            is_game_over = True