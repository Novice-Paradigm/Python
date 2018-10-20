def is_palindrome(word):

    letters = list(word)
    is_palindrome = True

    for letter in letters:
        if letter == letters[-1]:
            letters.pop(-1)
        else:
            is_palindrome = False
            break

    return is_palindrome
