numbers = []

while True:
      user_input = input("Enter an integer (or 'done' to finish): ")

      if user_input.lower() == "done":
          break

      try:
          number = int(user_input)
          numbers.append(number)
      except ValueError:
            print("Error: Please enter a valid number.")

      if numbers:
        print(f"Maximum: {max(numbers)}, Minimum: {min(numbers)}")
      else:
        print("No valid numbers were entered.")
