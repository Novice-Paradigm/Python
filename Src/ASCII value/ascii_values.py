
while True:
    char = input("Enter a character or type 'quit' to exit: ")

    if len(str(char)) == 1:
        print('The ASCII value of {} is {}\n'.format(char, ord(char)))
    if 'quit' in str(char).lower():
        quit()
