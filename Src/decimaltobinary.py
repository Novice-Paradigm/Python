

def decimal_to_binary(num):
""" This function converts a decimal number (num ) to a binary number"""

    if (num > 1):
        decimal_to_binary(num // 2)
    print(num % 2, end ='')