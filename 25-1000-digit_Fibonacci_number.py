def FibonacciIndex(digits: int) -> int:
    if digits < 1:
        return -1
    elif digits == 1:
        return 1
    first = second = 1
    count = 2

    while len(str(second)) < digits:
        next = first + second
        first = second
        second = next
        count += 1

    return count


print(FibonacciIndex(1000))
