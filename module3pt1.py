total = 0
count = 0

    while True:
        user_input = input("Enter an integer or 'done' to finish: ")

        if user_input.lower() == "done":
            break

        try:
            number = int(user_input)
            total += number
            count += 1
        except ValueError:
            print("Error: Please enter a valid number.")

    if count > 0:
        average = total / count
        print(f"Total: {total}, Count: {count}, Average: {average:.2f}")
    else:
        print("No valid numbers were entered.")
