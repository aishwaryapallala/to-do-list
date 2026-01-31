# To-Do List Application
# Project 3 - Beginner Version (No enumerate)

tasks = []

while True:
    print("\nTo-Do List Menu")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == '2':
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            i = 1
            for task in tasks:
                print(i, ".", task)
                i = i + 1

    elif choice == '3':
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            print("\nYour Tasks:")
            i = 1
            for task in tasks:
                print(i, ".", task)
                i = i + 1

            num = int(input("Enter task number to remove: "))
            if num >= 1 and num <= len(tasks):
                removed = tasks.pop(num - 1)
                print("Removed task:", removed)
            else:
                print("Invalid task number.")

    elif choice == '4':
        print("Exiting To-Do List. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")

             
