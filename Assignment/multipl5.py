# Combined Program:
# 1. Greatest among three numbers
# 2. Print numbers divisible by 5 in one line

print("=== Program Started ===\n")

# Part 1: Greatest among three numbers
print("--- Find Greatest of Three Numbers ---")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a >= b and a >= c:
    print(f"The greatest number is: {a}")
elif b >= a and b >= c:
    print(f"The greatest number is: {b}")
else:
    print(f"The greatest number is: {c}")

print("\n")  # Blank line for separation

# Part 2: Numbers divisible by 5 in one line
print("--- Numbers Divisible by 5 ---")
n = int(input("Enter the last number (N): "))

print("Numbers divisible by 5:", end=" ")

for i in range(5, n+1, 5):
    print(i, end=" ")

print()  # Move to next line

print("\n=== Program Ended ===")