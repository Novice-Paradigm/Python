print("Enter 'x' for exit.");
fah = input("Enter Temperature in Fahrenheit: ");
if fah == 'x':
    exit();
else:
    fahrenheit = float(fah);
    celsius = (fahrenheit-32)/1.8;
    print("Temperature in Celsius =",celsius);