def print_upper_words(in_words, must_start_with={}):
    """
        Prints a supplied list of words in UPPERCASE, one word per line. 

        in_words = a list of words to print out, one per line, in UPPERCASE

        must_start_with, is a set of letters and, when provided, only words 
            in in_words that begin with the letter in must_start_with are 
            printed. must_start_with defaults to {}.

    """

    #print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], must_start_with={"h", "y"})

    if (len(must_start_with) == 0):
        # print all the words provided via in_words as uppercase
        # for exists in this part of the loop because there is no need to add the
        #  overhead of checking the first letter when must_start_with is empty.
        for word in in_words:
            print(word.upper())
    else:
        must_start_with_uc = set()
        for letter in must_start_with:
            must_start_with_uc.add(letter[0].upper())

        for word in in_words:
            if (word[0].upper() in must_start_with_uc):
                print(word.upper())


print(
    f'\n1. words: {["hello", "hey", "goodbye", "yo", "yes"]}, must_start_with: {"h", "y"}')
print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                  must_start_with={"h", "y"})

print(
    f'\n\n2. words: {["hello", "hey", "goodbye", "yo", "yes"]}, must_start_with: {"h", "y"}')
print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                  must_start_with={"hell", "yuck"})

print(
    f'\n\n3. words: {["hello", "hey", "goodbye", "yo", "yes"]}, must_start_with: not provided')
print_upper_words(["hello", "hey", "goodbye", "yo", "yes"])
