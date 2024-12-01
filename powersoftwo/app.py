from numba import njit
import random
from tqdm import tqdm

@njit
def is_power_of_two(n):
    """Check if a given number is a power of 2."""
    return n > 0 and (n & (n - 1)) == 0

def generate_random_array(size, min_value, max_value):
    """Generate a random array of specified size with elements within the given range."""
    return [random.randint(min_value, max_value) for _ in range(size)]

@njit
def find_powers_of_two(arr):
    powers = []
    for number in arr:
        if is_power_of_two(number):
            powers.append(number)
    return powers

# Generate random arrays and check for powers of 2
size, min_value, max_value = 10, 1, 10000
numbers_needed, numbers_found = 5, 0
powers = []

with tqdm(total=numbers_needed) as pbar:
    while numbers_found < numbers_needed:
        arr = generate_random_array(size, min_value, max_value)
        new_powers = find_powers_of_two(arr)
        powers.extend(new_powers)
        new_found = len(new_powers)
        numbers_found += new_found
        pbar.update(new_found)

        print(f"Array: {arr}")
        print(f"Numbers divisible by a power of 2 so far: {numbers_found}")

print("Numbers divisible by a power of 2 found: ", powers[:numbers_needed])