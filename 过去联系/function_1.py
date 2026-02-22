def calc_square(number):
    square = number ** 2
    return square
def calc_cube(number):
    cube = number ** 3
    return cube
def calc_square_and_cube(number):
    number_1 = calc_square(number)
    number_2 = calc_cube(number)
    return number_1, number_2
c = int(input("Enter a number: "))
number_1, number_2 = calc_square_and_cube(c)
print(f"The square of {c} is {number_1}")
print(f"The cube of {c} is {number_2}")
