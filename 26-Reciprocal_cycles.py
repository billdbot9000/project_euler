def DecimalFractionString(numerator: int, denominator: int) -> (str, int):
    digit, remainder = int(), int()
    digit_place, cycle_length = 0, 0
    divisions = dict()
    decimal_string = str()

    digit = numerator // denominator
    remainder = numerator % denominator
    decimal_string += str(digit)
    if remainder > 0:
        decimal_string += "."

    while remainder > 0:
        if remainder not in divisions:
            divisions[remainder] = digit_place
        else:
            cycle_length = digit_place - divisions[remainder]
            break

        digit = 10 * remainder // denominator
        remainder = 10 * remainder % denominator
        digit_place += 1
        decimal_string += str(digit)

    return (decimal_string, cycle_length)


max_cycle = (1, 0)
cycle_length = int()
for den in range(2, 1000):
    cycle_length = DecimalFractionString(1, den)[1]

    if cycle_length > max_cycle[1]:
        max_cycle = (den, cycle_length)

print(max_cycle)
print("\n")
print(DecimalFractionString(1, 6))
