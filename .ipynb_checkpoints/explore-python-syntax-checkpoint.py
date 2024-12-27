def get_float(prompt="Provide a float number as input:"):
    """Prompts the user to enter a float and validates that it is not an integer."""
    while True:
        user_input = input(prompt)
        try:
            user_input_float = float(user_input)
            # Reject if the input is a valid integer (e.g., "2" or "3")
            if user_input_float.is_integer():
                print("Invalid input. Please enter a decimal number, not an integer.")
            else:
                return user_input_float
        except ValueError:
            print("Invalid input. Please enter a decimal number.")


def get_integer(prompt="Provide an integer as input:"):
    """Prompts the user to enter an integer and validates the input."""
    while True:
        try:
            user_input = int(input(prompt))
            return user_input
        except ValueError:
            print("Invalid input. Please enter an integer.")

def get_string(prompt="Provide a string as input:"):
    """Prompts the user to enter a string."""
    while True:
        user_input = input(prompt)
        if user_input.strip():  # Ensures the input is not just whitespace
            return user_input
        print("Invalid input. Please enter a non-empty string.")

# Example usage:
if __name__ == "__main__":
    float_value = get_float()
    print(f"You entered the float: {float_value}")
    
    integer_value = get_integer()
    print(f"You entered the integer: {integer_value}")
    
    string_value = get_string()
    print(f"You entered the string: '{string_value}'")
