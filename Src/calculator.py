def calculate():

    operator = input('Type in the math operator (+, -, *, /, **): ')

    number_1 = int(input('First number: '))
    number_2 = int(input('Second number: '))

    calculated_string='{} {} {} ='.format(number_1, operator, number_2)

    if operator == '+':
        print(calculated_string, number_1 + number_2)

    elif operator == '-':
        print(calculated_string, number_1 - number_2)

    elif operator == '*':
        print(calculated_string, number_1 * number_2)

    elif operator == '/':
        print(calculated_string, number_1 / number_2)

    elif operator == '**':
        print(calculated_string, number_1 ** number_2)
    
    else: print('Not a valid operator')

calculate()