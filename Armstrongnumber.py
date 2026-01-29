


num = int(input("Enter a number: "))
sum_of_digits = 0


num_str = str(num)
num_digits = len(num_str)

for digit in num_str:
    sum_of_digits += int(digit) ** num_digits
if sum_of_digits == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")


