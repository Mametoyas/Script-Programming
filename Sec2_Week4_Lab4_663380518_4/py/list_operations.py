print("--- List Creation and Access ---")
empty_list = []
print(f"Empty list: {empty_list}")

fruits = ["apple", "banana", "cherry", "date"]
print(f"Original fruits list: {fruits}")

# Accessing elements by index
print(f"First fruit: {fruits[0]}") # apple
print(f"Last fruit (negative index): {fruits[-1]}") # date

# Slicing
print(f"Fruits from index 1 to 2 (exclusive): {fruits[1:3]}") # ['banana', 'cherry']
print(f"All fruits except first: {fruits[1:]}") # ['banana', 'cherry', 'date']
print(f"Last two fruits: {fruits[-2:]}") # ['cherry', 'date']
print(f"Every second fruit: {fruits[::2]}") # ['apple', 'cherry']

print("\n--- Modifying List Elements ---")
fruits[1] = "blueberry" # Change an element
print(f"After changing index 1: {fruits}")

print("\n--- Adding Elements to List ---")
fruits.append("elderberry") # Add to the end
print(f"After append: {fruits}")

fruits.insert(1, "grape") # Insert at specific index
print(f"After insert at index 1: {fruits}")

more_fruits = ["kiwi", "lemon"]
fruits.extend(more_fruits) # Add elements from another list
print(f"After extend: {fruits}")

print("\n--- Removing Elements from List ---")
fruits.remove("cherry") # Remove by value (first occurrence)
print(f"After remove 'cherry': {fruits}")

popped_fruit = fruits.pop(2) # Remove by index (and get the item)
print(f"Popped fruit at index 2: {popped_fruit}")
print(f"After pop at index 2: {fruits}")

del fruits[0] # Delete by index
print(f"After del index 0: {fruits}")

# fruits.clear() # Empties the list
# print(f"After clear: {fruits}")

print("\n--- Other List Operations ---")
numbers = [3, 1, 4, 1, 5, 9, 2]
print(f"Original numbers: {numbers}")

print(f"Length of numbers list: {len(numbers)}")
print(f"Count of 1 in numbers: {numbers.count(1)}")
print(f"Index of first '4': {numbers.index(4)}")

numbers.sort() # Sorts in-place (modifies the original list)
print(f"Sorted numbers (in-place): {numbers}")

numbers.reverse() # Reverses in-place
print(f"Reversed numbers (in-place): {numbers}")

# Using sorted() to get a new sorted list without changing original
unsorted_numbers = [5, 2, 8, 1, 9]
new_sorted_numbers = sorted(unsorted_numbers)
print(f"Unsorted numbers: {unsorted_numbers}")
print(f"New sorted list: {new_sorted_numbers}")

print("\n--- Iterating through a List ---")
for fruit in fruits:
    print(f"I like {fruit}")

for i in range(len(fruits)):
    print(f"Fruit at index {i}: {fruits[i]}")

