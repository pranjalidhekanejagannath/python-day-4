# loop_tasks.py

# 1. For loop to print numbers 1–100
print("Numbers from 1 to 100:")
for i in range(1, 101):
    print(i, end=" ")

print("\n" + "-" * 40)

# 2. While loop for countdown timer
print("Countdown Timer:")
count = 10
while count > 0:
    print(count)
    count -= 1
print("Time's up!")

print("-" * 40)

# 3. Break and Continue example
print("Break and Continue Example:")
for i in range(1, 11):
    if i == 5:
        continue   # skip 5
    if i == 9:
        break      # stop loop at 9
    print(i)

print("-" * 40)

# 4. Iterate over string characters
name = "Pranjali"
print("Characters in string:")
for ch in name:
    print(ch)

print("-" * 40)

# 5. Multiplication table
num = 5
print(f"Multiplication Table of {num}:")
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

print("-" * 40)

# 6. Range with steps
print("Even numbers from 2 to 20:")
for i in range(2, 21, 2):
    print(i, end=" ")

print("\n" + "-" * 40)

# 7. Loop with conditions
print("Check even or odd:")
for i in range(1, 11):
    if i % 2 == 0:
        print(i, "is Even")
    else:
        print(i, "is Odd")

print("-" * 40)

# 8. Real-world example: ATM PIN attempts
correct_pin = 1234
attempts = 3

while attempts > 0:
    pin = int(input("Enter ATM PIN: "))
    if pin == correct_pin:
        print("Access Granted")
        break
    else:
        attempts -= 1
        print("Wrong PIN. Attempts left:", attempts)

if attempts == 0:
    print("Card Blocked")
