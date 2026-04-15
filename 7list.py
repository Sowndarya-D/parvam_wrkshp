# List of fruits
fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes", "Pineapple", "Strawberry"]

print("List of Fruits:")
print("===============")

# Print the list with numbers
for i, fruit in enumerate(fruits, 1):
    print(f"{i}. {fruit}")

# Print total number of fruits
print(f"\nTotal fruits in the list: {len(fruits)}")