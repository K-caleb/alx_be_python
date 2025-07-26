# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
  """
  Displays the current date and time in 'YYYY-MM-DD HH:MM:SS' format.
  """
  # Get the current date and time
  current_date = datetime.now()

  # Format the current date and time
  formatted_current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")

  print(f"Current Date and Time: {formatted_current_date}")

def calculate_future_date():
  """
  Prompts the user for a number of days, calculates a future date,
  and prints it in 'YYYY-MM-DD' format.
  """
  while True:
    try:
      days_to_add_str = input("Enter the number of days to add to the current date (integer): ")
      days_to_add = int(days_to_add_str)
      break # Exit loop if input is a valid integer
    except ValueError:
      print("Invalid input. Please enter an integer for the number of days.")

  # Get the current date (without time for future date calculation context)
  current_date_only = datetime.now().date()

  # Calculate the future date
  future_date = current_date_only + timedelta(days=days_to_add)

  # Format the future date
  formatted_future_date = future_date.strftime("%Y-%m-%d")

  print(f"Future Date ({days_to_add} days from now): {formatted_future_date}")

def main():
  """
  Main function to run the datetime exploration script.
  """
  print("--- Date and Time Explorer ---")
  display_current_datetime()
  print("\n") # Add a newline for better readability between parts
  calculate_future_date()
  print("\n--- End of Script ---")

if __name__ == "__main__":
  main()