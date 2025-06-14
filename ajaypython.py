def sum_natural_numbers(n):
    return n * (n + 1) // 2

# Example usage:
n = int(input("Enter a positive integer: "))
print(f"Sum of first {n} natural numbers is {sum_natural_numbers(n)}")