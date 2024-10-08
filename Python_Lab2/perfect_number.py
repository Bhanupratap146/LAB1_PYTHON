# Input the number to check
number = int(input("Enter a number to check if it's a perfect number: "))

# Initialize the sum of divisors
sum_of_divisors = 0

# Calculate the sum of proper divisors
for i in range(1, number):
    if number % i == 0:
        sum_of_divisors += i

# Check if the sum of divisors equals the original number
if sum_of_divisors == number:
    print(f"{number} is a perfect number.")
else:
    print(f"{number} is not a perfect number.")