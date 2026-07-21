print("--- Tuple Creation and Access ---")
empty_tuple = ()
print(f"Empty tuple: {empty_tuple}")

colors = ("red", "green", "blue", "yellow")
print(f"Original colors tuple: {colors}")

# Single item tuple requires a comma
single_item_tuple = ("single",)
print(f"Single item tuple: {single_item_tuple}, Type: {type(single_item_tuple)}")
not_a_tuple = ("single") # This is just a string in parentheses
print(f"Not a tuple: {not_a_tuple}, Type: {type(not_a_tuple)}")


# Accessing elements by index
print(f"First color: {colors[0]}") # red
print(f"Last color (negative index): {colors[-1]}") # yellow

# Slicing
print(f"Colors from index 1 to 2 (exclusive): {colors[1:3]}") # ('green', 'blue')

print("\n--- Demonstrating Tuple Immutability ---")
try:
    colors[0] = "orange" # Attempt to change an element
except TypeError as e:
    print(f"Error trying to modify tuple: {e}")

try:
    colors.append("purple") # Attempt to add an element
except AttributeError as e:
    print(f"Error trying to append to tuple: {e}")

try:
    del colors[0] # Attempt to delete an element
except TypeError as e:
    print(f"Error trying to delete from tuple: {e}")

print(f"Tuple remains unchanged: {colors}") # The tuple is still the same

print("\n--- Other Tuple Operations ---")
point = (10, 20)
x_coord, y_coord = point # Tuple unpacking
print(f"x_coord: {x_coord}, y_coord: {y_coord}")

print(f"Count of 'blue': {colors.count('blue')}")
print(f"Index of 'yellow': {colors.index('yellow')}")

print("\n--- Converting between List and Tuple ---")
my_list = [1, 2, 3, 4]
my_tuple_from_list = tuple(my_list)
print(f"List converted to tuple: {my_tuple_from_list}, Type: {type(my_tuple_from_list)}")

my_tuple = ("alpha", "beta", "gamma")
my_list_from_tuple = list(my_tuple)
print(f"Tuple converted to list: {my_list_from_tuple}, Type: {type(my_list_from_tuple)}")
