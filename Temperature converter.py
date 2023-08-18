def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

choice = input("Choose conversion (1: Celsius to Fahrenheit, 2: Fahrenheit to Celsius): ")

if choice == '1':
    celsius = float(input("Enter temperature in Celsius: "))
    print(f"{celsius}°C = {celsius_to_fahrenheit(celsius):.2f}°F")
elif choice == '2':
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    print(f"{fahrenheit}°F = {fahrenheit_to_celsius(fahrenheit):.2f}°C")
else:
    print("Invalid choice")


