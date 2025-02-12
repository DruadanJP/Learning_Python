# Generate squares of numbers from 0 to 9
squares = [x**2 for x in range(10)]
print(squares)

# Filter even numbers from a list
numbers = [1, 2, 3, 4, 5, 6]
evens = [num for num in numbers if num % 2 == 0]
print(evens)

# Explanation:

# A list comprehension creates lists concisely.
# The second example filters only even numbers.
# Example Output:

# 0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# [2, 4, 6]