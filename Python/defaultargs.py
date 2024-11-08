# Default-arguments, variable-length arguments and scope

#Scope and user-defined functions

#instructions
'''Use the keyword global to alter the object team in the global scope.
Change the value of team in the global scope to the string "justice league". Assign the result to team.
Hit the Submit button to see how executing your newly defined function change_team() changes the value of the name team!'''

# Create a string: team
team = "teen titans"

# Define change_team()
def change_team():
    """Change the value of the global variable team."""

    # Use team in global scope
    global team

    # Change the value of team in global: team
    team = 'justice league'
# Print team
print(team)

# Call change_team()
change_team()

# Print team
print(team)



# Nested functions
#instructions
'''Complete the function header of the nested function with the function name inner() and a single parameter word.
Complete the return value: each element of the tuple should be a call to inner(), passing in the parameters from three_shouts() as arguments to each call.'''

# Define three_shouts
def three_shouts(word1, word2, word3):
    """Returns a tuple of strings
    concatenated with '!!!'."""

    # Define inner
    def inner(word):
        """Returns a string concatenated with '!!!'."""
        return word + '!!!'

    # Return a tuple of strings
    return (inner(word1), inner(word2), inner(word3))

# Call three_shouts() and print
print(three_shouts('a', 'b', 'c'))


#instructions
'''Complete the function header of the inner function with the function name inner_echo() and a single parameter word1.
Complete the function echo() so that it returns inner_echo.
We have called echo(), passing 2 as an argument, and assigned the resulting function to twice. Your job is to call echo(), passing 3 as an argument. Assign the resulting function to thrice.
Hit Submit to call twice() and thrice() and print the results.'''

# Define echo
def echo(n):
    """Return the inner_echo function."""

    # Define inner_echo
    def inner_echo(word1):
        """Concatenate n copies of word1."""
        echo_word = word1 * n
        return echo_word

    # Return inner_echo
    return inner_echo

# Call echo: twice
twice = echo(2)

# Call echo: thrice
thrice = echo(3)

# Call twice() and thrice() then print
print(twice('hello'), thrice('hello'))


#instructions
'''Assign to echo_word the string word, concatenated with itself.
Use the keyword nonlocal to alter the value of echo_word in the enclosing scope.
Alter echo_word to echo_word concatenated with '!!!'.
Call the function echo_shout(), passing it a single argument 'hello'.'''

# Define echo_shout()
def echo_shout(word):
    """Change the value of a nonlocal variable"""
    
    # Concatenate word with itself: echo_word
    echo_word = word * 2
    
    # Print echo_word
    print(echo_word)
    
    # Define inner function shout()
    def shout():
        """Alter a variable in the enclosing scope"""    
        # Use echo_word in nonlocal scope
        nonlocal echo_word
        
        # Change echo_word to echo_word concatenated with '!!!'
        echo_word = echo_word + '!!!'
    
    # Call function shout()
    shout()
    
    # Print echo_word
    print(echo_word)

# Call function echo_shout() with argument 'hello'
echo_shout('hello')



#Default and flexible arguments
#instructions
'''Complete the function header with the function name shout_echo. It accepts an argument word1 and a default argument echo with default value 1, in that order.
Use the * operator to concatenate echo copies of word1. Assign the result to echo_word.
Call shout_echo() with just the string, "Hey". Assign the result to no_echo.
Call shout_echo() with the string "Hey" and the value 5 for the default argument, echo. Assign the result to with_echo.'''

# Define shout_echo
def shout_echo(word1, echo = 1):
    """Concatenate echo copies of word1 and three
     exclamation marks at the end of the string."""

    # Concatenate echo copies of word1 using *: echo_word
    echo_word = word1 * echo

    # Concatenate '!!!' to echo_word: shout_word
    shout_word = echo_word + '!!!'

    # Return shout_word
    return shout_word

# Call shout_echo() with "Hey": no_echo
no_echo = shout_echo("Hey")

# Call shout_echo() with "Hey" and echo=5: with_echo
with_echo = shout_echo("Hey", echo = 5)

# Print no_echo and with_echo
print(no_echo)
print(with_echo)



#instructions
'''Complete the function header with the function name shout_echo. It accepts an argument word1, a default argument echo with default value 1 and a default argument intense with default value False, in that order.
In the body of the if statement, make the string object echo_word upper case by applying the method .upper() on it.
Call shout_echo() with the string, "Hey", the value 5 for echo and the value True for intense. Assign the result to with_big_echo.
Call shout_echo() with the string "Hey" and the value True for intense. Assign the result to big_no_echo.'''

# Define shout_echo
def shout_echo(word1, echo = 1, intense = False):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string."""

    # Concatenate echo copies of word1 using *: echo_word
    echo_word = word1 * echo

    # Make echo_word uppercase if intense is True
    if intense is True:
        # Make uppercase and concatenate '!!!': echo_word_new
        echo_word_new = echo_word.upper() + '!!!'
    else:
        # Concatenate '!!!' to echo_word: echo_word_new
        echo_word_new = echo_word + '!!!'

    # Return echo_word_new
    return echo_word_new

# Call shout_echo() with "Hey", echo=5 and intense=True: with_big_echo
with_big_echo = shout_echo('Hey', echo = 5, intense = True)

# Call shout_echo() with "Hey" and intense=True: big_no_echo
big_no_echo = shout_echo('Hey', intense = True)

# Print values
print(with_big_echo)
print(big_no_echo)



#instructions
'''Complete the function header with the function name gibberish. It accepts a single flexible argument *args.
Initialize a variable hodgepodge to an empty string.
Return the variable hodgepodge at the end of the function body.
Call gibberish() with the single string, "luke". Assign the result to one_word.
Hit the Submit button to call gibberish() with multiple arguments and to print the value to the Shell.'''

# Define gibberish
def gibberish(*args):
    """Concatenate strings in *args together."""

    # Initialize an empty string: hodgepodge
    hodgepodge = ''

    # Concatenate the strings in args
    for word in args:
        hodgepodge += word

    # Return hodgepodge
    return(hodgepodge)

# Call gibberish() with one string: one_word
one_word = gibberish('luke')

# Call gibberish() with five strings: many_words
many_words = gibberish("luke", "leia", "han", "obi", "darth")

# Print one_word and many_words
print(one_word)
print(many_words)




#instructions
'''Complete the function header with the function name report_status. It accepts a single flexible argument **kwargs.
Iterate over the key-value pairs of kwargs to print out the keys and values, separated by a colon ':'.
In the first call to report_status(), pass the following keyword-value pairs: name="luke", affiliation="jedi" and status="missing".
In the second call to report_status(), pass the following keyword-value pairs: name="anakin", affiliation="sith lord" and status="deceased".'''

# Define report_status
def report_status(**kwargs):
    """Print out the status of a movie character."""

    print("\nBEGIN: REPORT\n")

    # Iterate over the key-value pairs of kwargs
    for key, value in kwargs.items():
        # Print out the keys and values, separated by a colon ':'
        print(key + ": " + value)

    print("\nEND REPORT")

# First call to report_status()
report_status(name="luke", affiliation="jedi", status="missing")

# Second call to report_status()
report_status(name= 'anakin', affiliation= 'sith lord', status= 'deceased')



#instructions
'''Complete the function header by supplying the parameter for a DataFrame df and the parameter col_name with a default value of 'lang' for the DataFrame column name.
Call count_entries() by passing the tweets_df DataFrame and the column name 'lang'. Assign the result to result1. Note that since 'lang' is the default value of the col_name parameter, you don't have to specify it here.
Call count_entries() by passing the tweets_df DataFrame and the column name 'source'. Assign the result to result2.'''

# Define count_entries()
def count_entries(df, col_name = 'lang'):
    """Return a dictionary with counts of
    occurrences as value for each key."""

    # Initialize an empty dictionary: cols_count
    cols_count = {}

    # Extract column from DataFrame: col
    col = df[col_name]
    
    # Iterate over the column in DataFrame
    for entry in col:

        # If entry is in cols_count, add 1
        if entry in cols_count.keys():
            cols_count[entry] += 1

        # Else add the entry to cols_count, set the value to 1
        else:
            cols_count[entry] = 1

    # Return the cols_count dictionary
    return cols_count

# Call count_entries(): result1
result1 = count_entries(tweets_df)

# Call count_entries(): result2
result2 = count_entries(tweets_df,'source')

# Print result1 and result2
print(result1)
print(result2)



#instructions
'''Complete the function header by supplying the parameter for the DataFrame df and the flexible argument *args.
Complete the for loop within the function definition so that the loop occurs over the tuple args.
Call count_entries() by passing the tweets_df DataFrame and the column name 'lang'. Assign the result to result1.
Call count_entries() by passing the tweets_df DataFrame and the column names 'lang' and 'source'. Assign the result to result2.
'''

# Define count_entries()
def count_entries(df, *args):
    """Return a dictionary with counts of
    occurrences as value for each key."""
    
    #Initialize an empty dictionary: cols_count
    cols_count = {}
    
    # Iterate over column names in args
    for col_name in args:
    
        # Extract column from DataFrame: col
        col = df[col_name]
    
        # Iterate over the column in DataFrame
        for entry in col:
    
            # If entry is in cols_count, add 1
            if entry in cols_count.keys():
                cols_count[entry] += 1
    
            # Else add the entry to cols_count, set the value to 1
            else:
                cols_count[entry] = 1

    # Return the cols_count dictionary
    return cols_count

# Call count_entries(): result1
result1 = count_entries(tweets_df, 'lang')

# Call count_entries(): result2
result2 = count_entries(tweets_df, 'lang', 'source')

# Print result1 and result2
print(result1)
print(result2)