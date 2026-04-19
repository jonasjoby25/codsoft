tasks = []

def showtasks():
    if not tasks:
        print("No tasks available")
    else:
        for i in range(len(tasks)):
            print(i+1, tasks[i])

def addtask():
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added")

def deletetask():
    showtasks()
    try:
        num = int(input("Enter task number to delete: "))
        tasks.pop(num - 1)
        print("Task deleted!")
    except:
        print("Invalid input")

while True:
    print("\n1. View Tasks\n2. Add Task\n3. Delete Task\n4. Exit")
    choice = input("Choose: ")

    if choice == '1':
        showtasks()
    elif choice == '2':
        addtask()
    elif choice == '3':
        deletetask()
    elif choice == '4':
        break
    else:
        print("Invalid choice")