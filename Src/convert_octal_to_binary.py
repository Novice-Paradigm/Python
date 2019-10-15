# Input a octal (number) and the output should be in binary

# Tells user to enter number
print("Enter 'x' for exit.");

# Takes user entered number
octal = input("Enter any number in Octal Format: ");

# TODO: Add check on user input
# If user inputs x exit run time
if octal == 'x':
    exit();
# If user enters anything else convert to binary    
else:
    # Built in method for conversion
    binary = bin(octal)

    # TODO: Strip 0b indicator for binary
    # Prints the result in binary
    print 'Binary output = %s' % binary
