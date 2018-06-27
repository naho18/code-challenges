###############################################################################
# Write a function that takes an integer flight_length (in minutes) and a list 
# of integers movie_lengths (in minutes) and returns a boolean indicating whether 
# there are two numbers in movie_lengths whose sum equals flight_length.

def matching_movies_to_flight(flight_length, movie_lengths):

    # create a set
    seen_movie_lengths = set()


    # iterate through the list of movies lengths
    for first_movie in movie_lengths:

        # find matching second movie
        second_movie = flight_length - first_movie

        # if matching second movie in set
        if second_movie in seen_movie_lengths:
            return True

        # add first movie length to set
        seen_movie_lengths.add(first_movie)

    # if no matches found
    return False

# O(n) time & O(n) space


###############################################################################
# palindrome?
def is_palindrome(string):
    
    # check to see if first & last letter are the same, move toward middle
    for i,v in enumerate(string):
        if v == string[-i-1]:
            continue
        else:
            return False
    return True

# O(n) runtime

# Permutation Palindrome 
# check if string has palindrome permutation (ex. racecar, aaccerr)

def has_palindrome_permutation(string):
    
    #create a set to hold letters of string
    letters = set()

    for char in string:
        if char in letters:
            letters.remove(char)
        else:
            letters.add(char)
    # if length of string is even, set length should be zero
    if len(string) % 2 == 0:
        return len(letters) == 0

    # if length of string is odd, set length should be one
    else:
        return len(letters) == 1


# O(n) runtime

