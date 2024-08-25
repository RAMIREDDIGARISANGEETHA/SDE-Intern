'''[2:51 PM, 8/25/2024] Sangeetha Reddy: Task-01

Build a Temperature Conversion Program

Create a program that converts temperatures between Celsius, Fahrenheit, and Kelvin scales. 
The program should prompt the user to Input a temperature value and the original unit of measurement.
 It should then convert the temperature to the other two units and display the converted values to the user. 
 For exomple, if the user enters a temperature of 25 degrees Celsius, the program should convert it to Fahrenheit and Kelvin, and present the converted values as outputs''''

def convert_temperature():
    print("Temperature Conversion Program")
    print("-------------------------------")

    # Get user input
    temp_value = float(input("Enter a temperature value: "))
    original_unit = input("Enter the original unit (C/F/K): ").upper()

    # Convert temperature
    if original_unit == "C":
        fahrenheit = (temp_value * 9/5) + 32
        kelvin = temp_value + 273.15
        print(f"{temp_value}°C is equal to:")
        print(f"{fahrenheit}°F")
        print(f"{kelvin} K")
    elif original_unit == "F":
        celsius = (temp_value - 32) * 5/9
        kelvin = (temp_value - 32) * 5/9 + 273.15
        print(f"{temp_value}°F is equal to:")
        print(f"{celsius}°C")
        print(f"{kelvin} K")
    elif original_unit == "K":
        celsius = temp_value - 273.15
        fahrenheit = (temp_value - 273.15) * 9/5 + 32
        print(f"{temp_value} K is equal to:")
        print(f"{celsius}°C")
        print(f"{fahrenheit}°F")
    else:
        print("Invalid unit. Please enter C, F, or K.")

convert_temperature()
