# Python program to check if a number is a Perfect Number

# Take input from the user
num = int(input("Enter a number: "))

# Initialize sum of divisors
sum_of_divisors = 0

# Find all divisors of num (excluding itself)
for i in range(1, num):
    if num % i == 0:
        sum_of_divisors += i

# Check if the number is perfect
if sum_of_divisors == num:
    print(f"{num} is a Perfect Number.")
else:
    print(f"{num} is not a Perfect Number.")
