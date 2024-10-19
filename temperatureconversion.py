# def temperature_conversion()
    
#     print("Temperature conversion options")
#     print("convert fahrenheit to celsius")
#     print("convert celsius to fahrenheit")

#     # Get the user choice
#     choice = int(input("enter 1 or 2: "))


#     if choice == 1:
#         #convert  fahrenheit to celsius
#         fahrenheit = float(input("enter the temperature in fahrenheit: "))
#         celsius = (fahrenheit - 32) * 5/9
#         print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
#     elif choice == 2:
#         #convert celsius to fahrenheit
#         celsius = float(input("enter the temperature in celsius: "))
#         fahrenheit = (celsius * 5/9)+32
#         print(f"{celsius}°C is equal to {fahrenheit:.2}°F")
#     else:
#         #handle invalid input
#         print("invailed choice.please enter 1 or 2")
# # call function to run the programme
# temperature_conversion()


def temperature_conversion():
    # Display conversion options
    print("Temperature Conversion Options:")
    print("1. Convert Fahrenheit to Celsius")
    print("2. Convert Celsius to Fahrenheit")

    # Get the user's choice
    choice = int(input("Enter 1 or 2: "))

    # Perform the appropriate conversion
    if choice == 1:
        # Convert Fahrenheit to Celsius
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
    
    elif choice == 2:
        # Convert Celsius to Fahrenheit
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
    
    else:
        # Handle invalid input
        print("Invalid choice. Please enter 1 or 2.")

# Call the function to run the program
temperature_conversion()

      