print("Enter 'x' for exit.");
octal = input("Enter any number in Octal Format: ");
if octal == 'x':
    exit();
else:
    dec = str(int(octal, 8));
    decm = int(dec);
    print(octal,"in Binary =",bin(decm));