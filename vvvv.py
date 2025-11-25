# Dictionary that will store the inventory
inventory = {}

# Function to create or add a product to inventory
def create_inventory(inventory, name, price, amount):
    # Add the product to the inventory as a dictionary with name, price and quantity
    inventory[name] = {"name": name, "price": price, "amount": amount}
    return inventory

# Function to check if a product exists in the inventory
def product_existence(inventory, name):
    if name in inventory:
        print("The product exists.")
        return inventory[name]  # Returns the found product
    else:
        print("NO FOUND.")
        return None  # Returns None if not found

# Function to update the price of an existing product
def update_price(inventory, name, price):
    variable = product_existence(inventory, name)  # Check existence
    if variable:
        variable["price"] = float(price)  # Update the price
    return variable  # Returns the updated product or None

#Function to remove a product from inventory
def delete_inventory(inventory, name):
    if name in inventory:
        inventory.pop(name)  # Remove the product from the dictionary
        print(f"Product '{name}'removed.")
    else:
        print("Product not found.")  # If not found
    return inventory  #  Returns the updated inventory

# Lambda function to calculate the total inventory value
# Multiplies the price by the quantity of each product and adds the results
valor_total = lambda: sum(item["price"] * item["amount"] for item in inventory.values())

# Función principal que controla el menú y la interacción con el usuario
def main():
    while True:
        print("=" * 50)
        print("""
        1 = Create inventory
        2 = Check existing product
        3 = Update price
        4 = Delete product
        5 = Add inventory
        6 = Exit
        """)
        try:
            opcion = input("Enter the option you need: ")

            # Option 1: Create product
            if opcion == "1":
                try:
                    while True:
                        name = input("Enter the product name: ")
                        price = float(input("Enter the price of the product: "))
                        amount = float(input("Enter the amount: "))
                        if price > 0 and amount > 0 : 
                            create_inventory(inventory, name, price, amount)  #Call the function to add
                            print(inventory)  # Shows updated inventory
                            break
                        else:
                            print("both values ​​must be positive")
                except ValueError:
                    print("Error: Price and quantity must be valid numbers")
            # Option 2: Check if a product exists
            elif opcion == "2":
                name = input("Enter the product name: ")
                product_existence(inventory, name)  # Call the verification function
                print(inventory[name])

            # Option 3: Update the price of a product
            elif opcion == "3":
                try:
                    while True:
                        name = input("Enter the product name: ")
                        price = float(input("Enter the new value: "))
                        if price > 0:
                    
                            update_price(inventory, name, price)  # Update the price
                            print(inventory[name])
                            break
                        else:
                            print("the value has to be positive")
                except ValueError:
                    print("Error: Price must be a valid number.")

            # Option 4: Delete product from inventory
            elif opcion == "4":
                name = input("Enter the product name:")
                delete_inventory(inventory, name)  # Call the delete function
                print(inventory)

            # Option 5: Calculate the total value of the inventory
            elif opcion == "5":
                print(f"The total value of the inventory is: {valor_total():.2f}")

            # Option 6: Exit the program
            elif opcion == "6":
                print("Going out...")
                break  # Exits the loop and ends the program

            # If an invalid option is entered
            else:
                print("Invalid option. Please enter a valid option.")

        # Catch any unexpected errors
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

# Program entry point
if __name__ == "__main__":
    main()