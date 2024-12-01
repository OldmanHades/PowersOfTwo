from numba import njit, prange
import random

@njit
def is_power_of_two(n):
    """Check if a given number is divisible by a power of 2."""
    if n == 0:
        return True

    digits = str(n)
    for i in range(1, len(digits)):
        if digits[-i] not in ('0', '5') or (digits[-i] == '5' and digits[-i - 1] != '0'):
            return False

    return True

def generate_random_array(size, min_value, max_value):
    """Generate a random array of specified size with elements within the given range."""
    return [random.randint(min_value, max_value) for _ in range(size)]

def find_powers_of_two(arr):
    powers = []

    for number in arr:
        if is_power_of_two(number):
            powers.append(number)

    return powers

# Generate a random array and check for powers of 2
size, min_value, max_value = 10, 1, 10000
numbers_found = 0
while numbers_found == 0:
    arr = generate_random_array(size, min_value, max_value)
    powers = find_powers_of_two(arr)
    numbers_found = len(powers)
print("Numbers divisible by a power of 2 in the generated array: ", powers)