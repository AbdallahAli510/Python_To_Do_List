print("| Welcome In To-Do List App 📃|\n\n")

tasks = []

while True:
    print(
        "Choose an option: \n 1. Add Task \n 2. View Tasks \n 3. Delete Tasks \n 4. Exit"
    )

    print("\n")

    choise = input("Enter Your Choice (1-4) : ")

    if choise == "1":
        value = input("Please Enter Task: ")
        tasks.append(value)
        print("✅ Your Task Added Succesfully")
        print("\n")

    elif choise == "2":
        if not tasks:
            print("No Tasks Added Yet !")
            print("\n")
        else:
            print("Your Tasks 😊")
            i = 1
            for v in tasks:
                print(i, ".", v)
                i += 1

            print("\n")

    elif choise == "3":
        if not tasks:
            print("There Is No Tasks !")
            print("\n")
        else:
            print("Your Tasks is ⬇️")
            i = 1
            for v in tasks:
                print(i, ".", v)
                i += 1
            num = int(input("Please Enter Number Task You Want To Delete: "))

            s = len(tasks)

            if num > s:
                print("Please Enter Number Task Correctly")
                print("\n")

            elif num <= (s - s):
                print("Please Enter Number Task Correctly")
                print("\n")

            else:
                nu = num - 1
                tasks.pop(nu)

                print("✅ Task Deleted Succesfully")
                print("\n")

    elif choise == "4":

        print("GoodBye See You Soon 👋")
        print("\n")
        print("Made By Eng/ Boda")
        exit()

    else:
        print("\n")
        print("Please Enter Chooise From ( 1-4 )")
        print("\n")
