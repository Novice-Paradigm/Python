
def convertion_km_to_mile(params):

    miles_fact = 0.621371

    miles = params * miles_fact

    print('miles ={}'.format(miles))

    return miles


if __name__ == '__main__':
    convertion_km_to_mile(5.5)