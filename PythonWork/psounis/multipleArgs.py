def float_average(*numbers):
    s = 0
    for number in numbers:
        s += number
    return s / len(numbers)


print(float_average(2.1, 3.3, 33.1))
