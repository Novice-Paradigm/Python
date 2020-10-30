cancel = " "

while cancel != 'n':  # Until the user does not type 'n' at line 17, the process will loop
    # An input that asks for the value to check (and also lowercases the value [if letter])
    Value = input('Please enter the value you would like to check: ').lower()

    def reverse(Value):  # The function for the reversal of the string
        if len(Value) == 0:  # If there is only 1 value in the string it returns the same value itself
            return Value
        else:
            # Otherwise it will slice each value in the string and reverse it
            return reverse(Value[1:]) + Value[0]

    # Here there is a conditional statement that checks if the entered string and the reverse of it mathches with each other
    if reverse(Value) == Value:
        # If yes then it prints out saying yes the value entered is a palindrome
        print(f'Yes! {Value} is a palindrome ')
    else:
        # If no then it prints out saying no the value entered is not a palindrome
        print(f'No {Value} is not a palindrome ')

    # Here it asks if the user wants to continue of not inorder to continue or break the loop
    cancel = input('Would you like to continue (y/n): ')
