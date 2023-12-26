def prime(start, end):
    primes = []
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    return primes

start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))

prime_numbers = prime(start_range, end_range)

if prime_numbers:
    print(f"Prime numbers between {start_range} and {end_range}:")
    print(prime_numbers)
else:
    print(f"No prime numbers found between {start_range} and {end_range}")
