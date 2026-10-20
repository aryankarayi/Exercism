def is_armstrong_number(number):
    power = len(str(number))
    armstrong = 0
    for i in str(number):
        armstrong += int(i) ** power
    return armstrong == number
