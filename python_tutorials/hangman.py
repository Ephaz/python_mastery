# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
  
    '''
        secret_word: string, the word the user is guessing; assumes all letters are
          lowercase
        letters_guessed: list (of letters), which letters have been guessed so far;
          assumes that all letters are lowercase
        returns: boolean, True if all the letters of secret_word are in letters_guessed;
          False otherwise
    '''   
    #loop through the secret letters compared to the guessed letter
    i = 0
    while i < len(secret_word):
        # a is a boolean, as a result of an iterative loop checking if all letters are in the secret word
        a = secret_word[i] in letters_guessed     
        i +=1
    return a


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    i = 0
    # the loops goes throug the words and checks if they are in the secret word and fills in the complete word list
    complete_word = []
    
    while i < len(secret_word):
        # a is a boolean, as a result of an iterative loop checking if all letters are in the secret word.
        a = secret_word[i] in letters_guessed
        # condition to give user feedback, when the word exists, they get the word filled in. 
        if a == True:
          complete_word += secret_word[i]
          # print(complete_word)
        else:
          complete_word += "_"
          # print(complete_word)
        i +=1
    # to return a string we use the join method to convert the list to a string and we return that value.
    complete_guessed_word = ''.join(complete_word)
    return complete_guessed_word
   
    
def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    m = 0
    i = 0
    while m < len(string.ascii_lowercase):
      if string.ascii_lowercase[i] in letters_guessed:
        string.ascii_lowercase = string.ascii_lowercase.replace(string.ascii_lowercase[i],"")
      i += 1
      m += 1
    return string.ascii_lowercase


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    
    '''
    # loading words from file
    loaded_words = print("   Loading word list from file...")
    
    # output the number of words available to user
    number_of_words_loaded = print("  ", len(wordlist), "words loaded.")
    
    #hangman starts and introduces game to user
    welcome_to_hangman = print("   Welcome to the game Hangman!")
    
    # calling the random word function
    random_word = random.choice(wordlist)
    
    # counting the length of the word to give a user the length of the word
    wordlist_count = len(random_word)
    
    # calling the get_guessed function and displaying the spaces and words filled in.
    secret_word = random_word
    gueses_done = get_guessed_word(secret_word, letters_guessed)
    
    # print("  ","Welcome to the game Hangman!")
    word_length = print("  ",f"I am thinking of a word that is {wordlist_count} letters long.")
    
    # display the number of spaces the user has before the game starts from the get_guessed function
    user_gueses = print("   ",gueses_done)
    
    user_gueses_left = print("   You have 6 guesses left")
  
    # call the get_available_letters funtion to display the words available
    get_available_letters(letters_guessed)
  
    # display available letters to the user
    available_letters_left = print("   "f"Available letters: {get_available_letters(letters_guessed)}")
    
    # when hangman is called, it will do the following actions
    actions  = [loaded_words ,number_of_words_loaded,welcome_to_hangman, word_length, user_gueses, user_gueses_left, available_letters_left]
    
    return actions 
      
letters_guessed = [] 

# letters guessed will be an input from the user
def user_input():

  # number of guesses the user has when they start the game
  guesses = 6
  
  secret_word = "apple"
  
  # user has 3 warnings everytime they start
  

  # user letters are taken in as the while loop iterates throught the game
  user_letters = []
    
  while guesses != 0:
    letters_guessed = input("Please guess a letter: \n")
     
  #taking user input and making sure it is always lowercase
    letters_guessed = letters_guessed.lower()
  
  # populate the user list with all letters from the user
    user_letters += letters_guessed
    
  # print the guesses the user has everytime they try to guess the correct word
    print(f"You have {guesses} guesses left\n")
  
  # user has 3 warnings everytime they start
    # user_warnings = 
  
  # the user loses a guess only when they guess a letter that is not in the secret word
    if letters_guessed in secret_word:
      print(f"Available letters:{get_available_letters(letters_guessed)}\n")
      print(f"Good guess: {get_guessed_word(secret_word, letters_guessed = user_letters)} \n")
      print("---------------------")
      
      warnings = 3
      warnings_to_user = []
      while warnings != 0:
        if letters_guessed in user_letters:
          warnings -= 1
          print(f"You have {warnings} warnings left")
        else:
          continue
    
    else:
      print(f"Available letters:{get_available_letters(letters_guessed)}\n")
      print(f"Oops! That letter is not in my word :{get_guessed_word(secret_word, letters_guessed = user_letters)} \n")
      print("---------------------")
      guesses -= 1
      

   

  get_guessed_word(secret_word, letters_guessed)
  # get_available_letters(letters_guessed)
  
  
user_input()
# secret_word = choose_word(wordlist)
# hangman(secret_word)


# warnings available to the user





  
# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
   
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
  secret_word = choose_word(wordlist)
  hangman_with_hints(secret_word)
  