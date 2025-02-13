from decimal import Decimal, getcontext

# Set global precision
getcontext().prec = 4

# High precision calculation
result = Decimal('1.12345') + Decimal('2.6789')
print(result)

# Explanation:

# decimal.Decimal allows precise calculations.
# Useful for financial applications.
# Example Output:

# 3.802
