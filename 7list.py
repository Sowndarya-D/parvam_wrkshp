# List of fruits
fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes", "Pineapple", "Strawberry"]

print("List of Fruits:")
print("===============")

# Print the list with numbers
for i, fruit in enumerate(fruits, 1):
    print(f"{i}. {fruit}")

#list indexing
#list comprehensive
#list slicing
#list iterating
#list methods

# Print total number of fruits
print(f"\nTotal fruits in the list: {len(fruits)}")

#using list comprehension
l4 = [i for i in fruits if 'a' in i.lower()]
print("\nFruits containing the letter 'a':")
for i in l4:
    print(i)