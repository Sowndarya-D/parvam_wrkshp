 
"""
 task:
 1. functio taking parameter and returning value
 2. function without parameter and not returning value
 3. function with parameter and not returning value
 4. function without parameter and returning value"""

# ========================================================
# Python Functions - All 4 Types
# ========================================================

#print("=== PYTHON FUNCTIONS - 4 TYPES DEMO ===\n")


# TASK 1: Function with parameters and returning value
print("TASK 1: Function with parameters and returning value")

def add(a, b):
    return a + b

print("5 + 3 =", add(5, 3))
print("10 + 20 =", add(10, 20))
print("-2 + 7 =", add(-2, 7))
print("-" * 50)


# TASK 2: Function without parameter and not returning value
print("TASK 2: Function without parameter and not returning value")

def welcome_message():
    print("Hello Everyone!")
    print("Welcome to Python Programming Class.")
    print("Today we are learning different types of functions.")

welcome_message()
print("-" * 50)


# TASK 3: Function with parameter and not returning value
print("TASK 3: Function with parameter and not returning value")

def print_fruits(fruit_list):
    print("List of Fruits:")
    for i, fruit in enumerate(fruit_list, 1):
        print(f"{i}. {fruit}")

fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes", "Pineapple", "Strawberry"]
print_fruits(fruits)
print("-" * 50)


# TASK 4: Function without parameter and returning value
print("TASK 4: Function without parameter and returning value")

def get_current_year():
    return 2026

year = get_current_year()
print("Current Year is:", year)
print("-" * 50)


print("All 4 types of functions executed successfully!")