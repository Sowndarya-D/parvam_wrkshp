# Creating a tuple from user input
fruit_list = []

print("Enter fruit names (type 'done' when finished):")

while True:
    fruit = input("Enter a fruit: ").strip()
    if fruit.lower() == 'done':
        break
    if fruit:
        fruit_list.append(fruit.title())

# Convert list to tuple (once finished)
fruits = tuple(fruit_list)

print("\nYour Fruits Tuple:")
print("==================")
for i, fruit in enumerate(fruits, 1):
    print(f"{i}. {fruit}")

print(f"\nTotal fruits in tuple: {len(fruits)}")