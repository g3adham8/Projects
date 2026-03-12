
file_path = r"E:\python\app.txt"

my_list = ['a', 'd', 'u', 'q', 'r', 's', 'c']
user_input_text = """
-------------------------
what do you want to do?
'a' => add a task
'd' => delete a task
'u' => update a task 
'c' => complete a task (Mark with 💯)
's' => show current tasks
'r' => reset everything
'q' => quit the program
-------------------------
you choose: """


def add_task():
    # استخدام encoding='utf-8' 
    with open(file_path, 'a', encoding='utf-8') as my_file:
        while True:
            task = input("Write The Task Here: ").capitalize().strip()
            my_file.write(f"-{task}\n")

            choice = input(
                "Do You Want To Add More Tasks? (y/n): ").lower().strip()
            if choice != 'y':
                break

    print("\nYour Tasks Now:")
    with open(file_path, 'r', encoding='utf-8') as my_file:
        print(my_file.read())


def delete_task():
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        if not lines:
            print("The list is empty!")
            return

        print("\nHere are your tasks:")
        for line in lines:
            print(line.strip())

        delete = input("Write The Task You want to delete (exactly): ").strip()
        new_lines = [line for line in lines if delete not in line]

        if len(new_lines) < len(lines):
            with open(file_path, 'w', encoding='utf-8') as f:
                f.writelines(new_lines)
            print("--- Task deleted successfully ---")
        else:
            print("--- Task not found ---")
    except FileNotFoundError:
        print("File not found yet. Add a task first.")


def update_task():
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        if not lines:
            print("\n--- Your list is empty! ---")
            return

        print("\nChoose the number of the task you want to update:")
        for index, line in enumerate(lines):
            print(f"{index + 1}- {line.strip()}")

        choice = input("Enter task number: ").strip()
        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(lines):
                old_task = lines[idx].strip()
                new_text = input(
                    f"Updating '{old_task}' to: ").capitalize().strip()
                lines[idx] = f"-{new_text}\n"

                with open(file_path, 'w', encoding='utf-8') as f:
                    f.writelines(lines)
                print("--- Task updated successfully! ---")
            else:
                print("--- Invalid number! ---")
        else:
            print("--- Please enter a valid number! ---")
    except FileNotFoundError:
        print("--- File not found. ---")


def reset_and_add():
    confirm = input(
        "Are you sure you want to delete EVERYTHING? (y/n): ").lower().strip()
    if confirm == 'y':
        with open(file_path, 'w', encoding='utf-8') as my_file:
            print("--- File cleared! ---")
            add_task() 
    else:
        print("--- Operation cancelled. ---")


def complete_task():
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        if not lines:
            print("\n--- Your list is empty! ---")
            return

        print("\nWhich task did you complete? (Choose a number):")
        for index, line in enumerate(lines):
            print(f"{index + 1}- {line.strip()}")

        choice = input("Enter task number: ").strip()
        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(lines):
                if "(Done 💯)" in lines[idx]:
                    print("--- This task is already marked! ---")
                else:
                   
                    lines[idx] = lines[idx].strip() + " (Done 💯)\n"

                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.writelines(lines)
                    print("--- Great job! Task marked as completed. ---")
            else:
                print("--- Invalid task number! ---")
        else:
            print("--- Please enter a valid number! ---")
    except FileNotFoundError:
        print("--- File not found. ---")


while True:
    user = input(user_input_text).lower().strip()

    if user == 'a':
        add_task()
    elif user == 'd':
        delete_task()
    elif user == 'u':
        update_task()
    elif user == 'c':
        complete_task()
    elif user == 's':
        print("\n--- Current Tasks ---")
        try:
            with open(file_path, 'r', encoding='utf-8') as my_file:
                content = my_file.read()
                print(content if content else "List is empty.")
        except FileNotFoundError:
            print("File not found.")
    elif user == 'r':
        reset_and_add()
    elif user == 'q':
        print("Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")

