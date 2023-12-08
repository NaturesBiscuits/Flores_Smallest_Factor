print("---------------------------------------------------------------")
print("Enter an integer, and it will the smallest factor other than 1.")
print("---------------------------------------------------------------")

while True:
    n = int(input("\nEnter an integer >= 2: "))

    if n < 2:
        print("Invalid input, Enter a number greater than 2.")
        continue

    smallest_factor = None
    for i in range(2, n):
        if n % i == 0:
            smallest_factor = i
            break

    if smallest_factor:
        print(f"The smallest factor other than 1 for {n} is {smallest_factor}.")
    else:
        print(f"The smallest factor other than 1 for {n} is {n}.")
