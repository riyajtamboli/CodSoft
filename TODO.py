tasks = []

while True:
    print("*******************************************************************************")
    print("ToDo list")
    print("1.Add Task (**Sr. no starts from 0)")
    print("2.Edit Task")
    print("3.Done")
    print("4.Task list")
    ch = int(input("Select your option from above::"))
    if (ch == 1):
        print("*******************************************************************************")
        print("Adding Task::")
        value = input("Enter your task::")
        tasks.append(value)
        print("Task Added!!")

    elif (ch == 2):
        print("*******************************************************************************")
        print("Updating Task::")
        if len(tasks) != 0:
            key = int(input("Enter the Sr. no. of Task to Edit::"))
            if key < len(tasks):
                print(tasks[key])
                data = input("Update your task::")
                tasks[key] = data
                print("Task Updated!!")
            else:
                print("Enter valid Sr. no. of Task")
        else:
            print("ToDo list is empty!!")

    elif (ch == 3):
        print("*******************************************************************************")
        if len(tasks) != 0:
            key = int(input("Enter the Sr. no. of those Task which are Done::"))
            if key < len(tasks):
                print(tasks[key])
                x = tasks[key]
                tasks.remove(x)
                print("Task Done!!")
            else:
                print("Enter valid Sr. no. of Task")
        else:
            print("ToDo list is empty!!")

    elif (ch == 4):
        print("*******************************************************************************")
        print("Todo list is::")
        if len(tasks) != 0:
            for i in tasks:
                print("--", i)
        else:
            print("ToDo list is empty!!")

    else:
        print("Enter valid choice!!")

    ch = input("Do you want to Continue?(y/n)")
    if (ch == 'n'):
        print("Exiting")
        break
    elif (ch == 'y'):
        continue
    elif (ch != 'y'):
        print("Invalid Choice")
        break
