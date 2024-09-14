# Solution 1
def insert_value_at_index(arr, index, value):
    # Insert the value at the specified index in the array
    arr.insert(index, value)
    
    # Return the modified array
    return arr
my_array = [1, 2, 3, 4]
index_to_insert = 2
value_to_insert = 99

result = insert_value_at_index(my_array, index_to_insert, value_to_insert)
print(result)
#=====================================
# Solution 2
# Define a function to display the cart
def print_cart(cart):
    print("\nCurrent shopping cart:")
    if not cart:
        print("The cart is empty.")
    else:
        for item in cart:
            print(f"Item: {item['name']}, Quantity: {item['quantity']}")
    print("-" * 30)

# Function to add an item to the cart
def add_item(cart, item_name, quantity):
    cart.append({"name": item_name, "quantity": quantity})
    print(f"Added {quantity} of {item_name} to the cart.")
    print_cart(cart)

# Function to remove an item from the cart
def remove_item(cart, item_name):
    for item in cart:
        if item["name"] == item_name:
            cart.remove(item)
            print(f"Removed {item_name} from the cart.")
            break
    else:
        print(f"Item {item_name} not found in the cart.")
    print_cart(cart)

# Function to update the quantity of an item in the cart
def update_quantity(cart, item_name, new_quantity):
    for item in cart:
        if item["name"] == item_name:
            item["quantity"] = new_quantity
            print(f"Updated {item_name} quantity to {new_quantity}.")
            break
    else:
        print(f"Item {item_name} not found in the cart.")
    print_cart(cart)

# Main program
shopping_cart = []

# Adding items
add_item(shopping_cart, "Apple", 3)
add_item(shopping_cart, "Banana", 2)
add_item(shopping_cart, "Mangos", 9)

# Updating item quantity
update_quantity(shopping_cart, "Apple", 5)

# Removing an item
remove_item(shopping_cart, "Mangos")

# Final cart contents
print_cart(shopping_cart)
# ===================================

# Solution 3
# Initialize the starting integer
num = 1

# Use a while loop to print the first 25 integers
while num <= 25:
    print(num)
    num += 1  # Increment the number

# ======================================
# Solution 4
# Initialize the first even number
num = 2

# Counter to track how many even numbers have been printed
count = 0

# Use a while loop to print the first 10 even numbers
while count < 10:
    print(num)
    num += 2  # Increment by 2 to get the next even number
    count += 1  # Increment the count of even numbers printed
# ====================================================
# Solution 5
def factorial(n):
    # Initialize the result to 1
    result = 1
    
    # Ensure the input is a positive integer
    if n < 0:
        return "Factorial is not defined for negative numbers."
    
    # Use a while loop to calculate the factorial
    while n > 0:
        result *= n  # Multiply result by the current value of n
        n -= 1  # Decrease n by 1
    
    return result

number = 5
fact = factorial(number)
print(f"The factorial of {number} is {fact}")

# =====================================================

#Solution 6

# Define a function to remove negative numbers from an array
def remove_negatives(arr):
    # Create a new list with only non-negative numbers
    positive_arr = [num for num in arr if num >= 0]
    return positive_arr

# Main program
numbers = [12, -7, 5, -3, 9, -14, 20]

# Remove negative numbers from the array
filtered_numbers = remove_negatives(numbers)

# Print the modified array
print("Array after removing negative numbers:", filtered_numbers)
# ==========================================================

# Solution 7
def sum_of_array(arr):
    # Initialize the sum to 0
    total_sum = 0
    
    # Initialize the index for the while loop
    index = 0
    
    # Use a while loop to iterate through the array
    while index < len(arr):
        total_sum += arr[index]  # Add the current element to the sum
        index += 1  # Move to the next element
    
    return total_sum
    
numbers = [10, 20, 30, 40, 50]

# Calculate the sum of the numbers in the array
result = sum_of_array(numbers)
print(f"The sum of the array is: {result}")

# ====================================================

# Solution 8
# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Function to convert a list of Celsius temperatures to Fahrenheit
def convert_temperatures(celsius_list):
    fahrenheit_list = []
    index = 0
    
    # Use a while loop to convert each temperature
    while index < len(celsius_list):
        fahrenheit = celsius_to_fahrenheit(celsius_list[index])
        fahrenheit_list.append(fahrenheit)  # Store the converted temperature
        index += 1
    
    return fahrenheit_list

# Main program
# Get a list of temperatures in Celsius from the user, splitting input by spaces
celsius_input = input("Enter a list of temperatures in Celsius, separated by spaces: ")
celsius_list = list(map(float, celsius_input.split()))  # Convert input to a list of floats

# Convert the list of temperatures to Fahrenheit
fahrenheit_list = convert_temperatures(celsius_list)

# Print the converted temperatures
print("Temperatures in Fahrenheit:", fahrenheit_list)
#=========================================================

# Solution 9
# Define a function to remove odd numbers from an array
def remove_odds(arr):
    # Create a new list with only even numbers
    even_arr = [num for num in arr if num % 2 == 0]
    return even_arr

# Main program
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Remove odd numbers from the array
filtered_numbers = remove_odds(numbers)

# Print the modified array
print("Array after removing odd numbers:", filtered_numbers)


