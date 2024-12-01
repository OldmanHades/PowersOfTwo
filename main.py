from numba import njit
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

# Example usage:
numbers = [2, 4, 7, 8, 15, 32, 64, 1024, 2048, 3000, 9000, 10000, 34567, 879045]
for number in numbers:
    if is_power_of_two(number):
        print(f"{number} is divisible by a power of 2.")
    else:
        print(f"{number} is not divisible by a power of 2.")