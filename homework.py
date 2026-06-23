# Square Root Calculator

# Step 1: Get user input
user_input = float(input("Enter a positive number: "))

# Step 2: Check if the number is valid using conditional statements
if user_input < 0:
    print("Error: Cannot calculate the square root of a negative number!")
elif user_input == 0:
    print("The square root of 0 is 0.00")
else:
    # Calculate square root using the exponent operator (power of 0.5)
    square_root = user_input ** 0.5
    
    # Step 3: Display the final result
    print(f"The square root of {user_input} is: {square_root:.2f}")
