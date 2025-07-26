# shopping_list_manager.py

def display_menu():
  """Displays the main menu options to the user."""
  print("\n--- Shopping List Manager ---")
  print("1. Add item")
  print("2. Remove item")
  print("3. View list")
  print("4. Exit")
  print("-----------------------------")

def add_item(shopping_list: list):
  """
  Prompts the user for an item name and adds it to the shopping list.

  Args:
    shopping_list: The list to which the item will be added.
  """
  item = input("Enter the item to add: ").strip()
  if item: # Ensure item is not empty
    shopping_list.append(item)
    print(f"'{item}' has been added to your shopping list.")
  else:
    print("Item name cannot be empty. Please try again.")

def remove_item(shopping_list: list):
  """
  Prompts the user for an item name and removes it from the shopping list.
  Displays a message if the item is not found.

  Args:
    shopping_list: The list from which the item will be removed.
  """
  item = input("Enter the item to remove: ").strip()
  if item:
    if item in shopping_list:
      shopping_list.remove(item)
      print(f"'{item}' has been removed from your shopping list.")
    else:
      print(f"'{item}' not found in the shopping list.")
  else:
    print("Item name cannot be empty. Please try again.")

def view_list(shopping_list: list):
  """
  Displays all items currently in the shopping list.
  Indicates if the list is empty.

  Args:
    shopping_list: The list to be displayed.
  """
  print("\n--- Your Shopping List ---")
  if not shopping_list:
    print("Your shopping list is empty.")
  else:
    for i, item in enumerate(shopping_list, 1):
      print(f"{i}. {item}")
  print("--------------------------")

def main():
  """
  Main function to run the shopping list manager application.
  Initializes the shopping list and handles user interactions.
  """
  shopping_list = []
  
  while True:
    display_menu()
    choice = input("Enter your choice (1-4): ").strip()

    if choice == '1':
      add_item(shopping_list)
    elif choice == '2':
      remove_item(shopping_list)
    elif choice == '3':
      view_list(shopping_list)
    elif choice == '4':
      print("Exiting Shopping List Manager. Goodbye!")
      break
    else:
      print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
  main()