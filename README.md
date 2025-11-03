# Python_To_Do_List

# 📃 To-Do List App (Terminal)

A simple, terminal-based **To-Do List** application written in Python.  
Minimal, interactive, and dependency-free — great for learning Python and building small CLI tools.

---

## Table of Contents
- [About](#about)  
- [Features](#features)  
- [Requirements](#requirements)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Example Session](#example-session)  
- [How it works](#how-it-works)  
- [Customization](#customization)  
- [Contributing](#contributing)  
- [License](#license)  
- [Script (`todo.py`)](#script-todopy)

---

## About
This small script keeps an in-memory list of tasks that the user can add to, view, and delete from using a terminal menu. When the user exits, the list is not persisted — it's a lightweight example for learning basic Python control flow and lists.

---

## Features
- Add tasks interactively  
- View all added tasks with index numbers  
- Delete a task by its number  
- Clean, single-file implementation  
- No external libraries required

---

## Requirements
- Python 3.x

---

## Installation
1. Create a new repository on GitHub (or use an existing one).  
2. Add a file named `README.md` and paste the contents of this README.  
3. Add the script file (recommended name: `todo.py`) with the Python code below.  
4. Commit and push to GitHub.

---

## Usage
Save the script as `todo.py` and run it from a terminal:

```bash
python todo.py
```

Follow the menu prompts to add, view, or delete tasks, or to exit the application.

---

## Example Session

```
$ python todo.py
| Welcome In To-Do List App 📃|

Choose an option:
 1. Add Task
 2. View Tasks
 3. Delete Tasks
 4. Exit

Enter Your Choice (1-4) : 1
Please Enter Task: Buy groceries
✅ Your Task Added Succesfully

Enter Your Choice (1-4) : 2
Your Tasks 😊
1 . Buy groceries

Enter Your Choice (1-4) : 3
Your Tasks is ⬇️
1 . Buy groceries
Please Enter Number Task You Want To Delete: 1
✅ Task Deleted Succesfully

Enter Your Choice (1-4) : 4
GoodBye See You Soon 👋

Made By Eng/ Boda
```

---

## How it works
1. The program runs an infinite loop showing a menu with 4 choices.  
2. Choice `1` reads a task string and appends it to the in-memory `tasks` list.  
3. Choice `2` prints all tasks with numeric indices.  
4. Choice `3` shows the tasks, asks for the task number to delete, validates the number, and removes the selected task.  
5. Choice `4` exits the program.  
6. Input validation is performed to avoid deleting non-existent indices.

---

## Customization
- **Persist tasks**: Save and load tasks from a file (e.g., JSON or plain text) to keep them between runs.  
- **Search/filter**: Add a search or filter option to find tasks by keyword.  
- **Edit tasks**: Add an option to edit an existing task by index.  
- **Timestamps/priority**: Store timestamps, priority levels, or categories for each task.  
- **CLI flags**: Add command-line options for quick actions (e.g., `--add "Buy milk"`).

---

## Contributing
Small projects are great for practice:
- Open issues for feature requests or bugs.  
- Submit pull requests to add persistence, extra commands, or tests.

---

## License
This project is available under the **MIT License** — feel free to reuse and adapt.

---

## Script: `todo.py`
Copy the exact code below into a file named `todo.py`:

```python
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
```
