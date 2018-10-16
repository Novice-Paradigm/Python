from math import sqrt


# Heron's Method
def sqrt_heron(n, error):
    prev, new = 1.0, 0.5 * (1 + n)
    while abs(new - prev) > error:
        prev, new = new, 0.5 * (new + n/new)
    return new


if __name__ == '__main__':
    print("Built-In Function")
    x = float(input("Enter a number: "))
    print("Square Root: {}\n".format(sqrt(x)))

    print("Heron Method")
    x = float(input("Enter number: "))
    error_margin = float(input("Error Margin: "))
    print("Square Root: {}".format(sqrt_heron(x, error_margin)))
