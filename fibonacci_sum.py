def fibonacci_sum(limit):
    a, b = 1, 2
    even_sum = 0
    
    while a <= limit:
        if a % 2 == 0:
            even_sum += a
        a, b = b, a + b
    
    return even_sum

# Set the limit to four million
limit = 4000000

# Calculate the sum of even-valued terms in the Fibonacci sequence
result = fibonacci_sum(limit)

print("Sum of even-valued terms in the Fibonacci sequence below", limit, "is:", result)
