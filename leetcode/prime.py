def is_lucky(num):
    factors = set()
    for i in range(1, num + 1):
        if num % i == 0:
            factors.add(i)
            factors.add(num // i)
    # Power to the factors can only be 1
    return len(factors) == 2 * num - 1


def count_lucky_numbers(L, R):
    count = 0
    for num in range(L, R + 1):
        if num > 1 and is_lucky(num):
            count += 1
    return count


# Example usage:
L = 1
R = 20
result = count_lucky_numbers(L, R)
print(result)
