# temp_conversion_tool.py

# Define Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit: float) -> float:
  # Use the global FAHRENHEIT_TO_CELSIUS_FACTOR
  celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
  return celsius

def convert_to_fahrenheit(celsius: float) -> float:
  # Use the global CELSIUS_TO_FAHRENHEIT_FACTOR
  fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
  return fahrenheit

def main():
  print("--- Temperature Conversion Tool ---")

  while True:
    try:
      temp_str = input("Enter the temperature: ").strip()
      temperature = float(temp_str) # Attempt to convert input to float
      break # Exit loop if conversion is successful
    except ValueError:
      print("Invalid temperature. Please enter a numeric value.")

  unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ").strip().upper()

  if unit == 'C':
    converted_temp = convert_to_fahrenheit(temperature)
    print(f"{temperature}°C is {converted_temp:.2f}°F")
  elif unit == 'F':
    converted_temp = convert_to_celsius(temperature)
    print(f"{temperature}°F is {converted_temp:.2f}°C")
  else:
    print("Invalid unit. Please enter 'C' or 'F'.")

if __name__ == "__main__":
  main()
