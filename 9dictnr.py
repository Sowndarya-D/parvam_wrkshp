# Dictionary of fruits (Fruit name : Color)
fruits = {
    "Apple": "Red",
    "Banana": "Yellow",
    "Mango": "Orange",
    "Orange": "Orange",
    "Grapes": "Purple",
    "Pineapple": "Yellow",
    "Strawberry": "Red"
}

print("Fruits Dictionary:")
print("==================")

# Print dictionary items nicely
for i, (fruit, color) in enumerate(fruits.items(), 1):
    print(f"{i}. {fruit} → {color}")

print(f"\nTotal fruits: {len(fruits)}")