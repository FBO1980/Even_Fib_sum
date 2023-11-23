# Even_Fib_sum
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms

## You
write in Pyhton a script with the folowing functionality: 
print the even numbers in the Fibonacci sequence whose values do not exceed four million. then print the sum 

## ChatGPT
Certainly! Here's a Python script that accomplishes the specified functionality:

```
def generate_fibonacci(limit):
    fib_sequence = [1, 2]
    while fib_sequence[-1] + fib_sequence[-2] <= limit:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def filter_even_numbers(sequence):
    return [num for num in sequence if num % 2 == 0]

def main():
    limit = 4000000

    # Generate Fibonacci sequence
    fibonacci_sequence = generate_fibonacci(limit)

    # Filter even numbers
    even_numbers = filter_even_numbers(fibonacci_sequence)

    # Print even numbers
    print("Even numbers in the Fibonacci sequence up to 4 million:")
    print(even_numbers)

    # Print the sum of even numbers
    even_sum = sum(even_numbers)
    print(f"\nSum of even numbers: {even_sum}")

if __name__ == "__main__":
    main()
```
Copy and paste this code into a Python script (e.g., a .py file) and run it. It will generate the Fibonacci sequence up to four million, filter out the even numbers, print them, and finally, print the sum of those even numbers.
