tasks = []
while True:
    print("\n1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        if not tasks:
            print("No tasks yet.")
        else:
            for i, task in enumerate(tasks, 1):
                print(i, task)
    elif choice == "2":
        task = input("Enter task: ")
        tasks.append(task)
    elif choice == "3":
        num = int(input("Enter task number to remove: "))
        if 1 <= num <= len(tasks):
            tasks.pop(num - 1)
        else:
            print("Invalid task number")
    elif choice == "4":
        break
    else:
        print("Invalid choice")
