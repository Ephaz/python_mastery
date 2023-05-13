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
 
x = is_word_guessed(secret_word= "apple",letters_guessed=['a', 'p', 'e', 'l'])
