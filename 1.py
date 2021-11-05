number = int(input("Please enter a number: "))

evenSum = 0
oddSum = 0
i = 1
count = 0

for i in range(number+1):
    if i % 2 == 0:
        evenSum += i
        count += 1
    else:
        oddSum += i

print(f"Sum of the odd numbers: {oddSum}")
print(f"Average of the even numbers: {evenSum / count}")

# We can make millions of solutions but it's just an exercise
# Such as, actually we don't need count and evenSum, we can do just
# use number value for calculating average.
