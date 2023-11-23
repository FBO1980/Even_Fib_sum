# Even_Fib_sum
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms

## You
Write in Pyhton a script with the following functionality: By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms

## ChatGPT
Certainly! You can use the following Python script to find the sum of even-valued terms in the Fibonacci sequence that do not exceed four million:

```
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
```


This script defines a function fibonacci_sum that calculates the sum of even-valued terms in the Fibonacci sequence up to a given limit. The main part of the script sets the limit to four million and prints the result.
