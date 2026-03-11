"""
Day 12 Portfolio Project — StudyFlow CLI (List Manager)

Goal:
Build a terminal app to manage study tasks using lists.
This project uses everything up to Day 12:
- input/output
- if/elif/else
- for/while
- break/continue
- lists (create, access, modify)

Project idea:
Create a menu-based app where the user can:
1) Add a task
2) List tasks
3) Edit a task by index
4) Remove a task by index
5) Mark a task as done / undone
6) Show progress (done vs pending)
7) Exit

Data model (use lists only):
- tasks: list of task names (str)
- done_flags: list of booleans, same index as tasks
  Example:
    tasks = ["Study loops", "Read docs"]
    done_flags = [True, False]

Rules:
- Never let the two lists have different lengths.
- Validate indexes before editing/removing.
- Handle invalid menu options safely.
- Keep looping until user chooses Exit.

Portfolio extras (recommended):
- Skip empty task names (use continue).
- Ask confirmation before delete ("yes"/"no").
- Show task numbers starting at 1 for the user.
- Convert user index (1-based) to Python index (0-based).
"""

# -----------------------------
# Starter structure (implement)
# -----------------------------

tasks = []
done_flags = []

while True:
    print("\n=== StudyFlow CLI ===")
    print("1) Add task")
    print("2) List tasks")
    print("3) Edit task")
    print("4) Remove task")
    print("5) Toggle done/undone")
    print("6) Show progress")
    print("7) Exit")

    option = input("Choose an option: ").strip()

    if option == "1":
        task_name = input("Task name: ").strip()
        if task_name == "":
            print("Task cannot be empty.")
            continue
        tasks.append(task_name)
        done_flags.append(False)
        print("Task added.")

    elif option == "2":
        if len(tasks) == 0:
            print("No tasks yet.")
            continue
        print("\nTasks:")
        for i in range(len(tasks)):
            status = "Done" if done_flags[i] else "Pending"
            print(f"{i + 1}. [{status}] {tasks[i]}")

    elif option == "3":
        if len(tasks) == 0:
            print("No tasks to edit.")
            continue
        index = int(input("Task number to edit: ")) - 1
        if index < 0 or index >= len(tasks):
            print("Invalid task number.")
            continue
        new_name = input("New task name: ").strip()
        if new_name == "":
            print("Task cannot be empty.")
            continue
        tasks[index] = new_name
        print("Task updated.")

    elif option == "4":
        if len(tasks) == 0:
            print("No tasks to remove.")
            continue
        index = int(input("Task number to remove: ")) - 1
        if index < 0 or index >= len(tasks):
            print("Invalid task number.")
            continue
        confirm = input("Are you sure? (yes/no): ").strip().lower()
        if confirm != "yes":
            print("Removal canceled.")
            continue
        tasks.pop(index)
        done_flags.pop(index)
        print("Task removed.")

    elif option == "5":
        if len(tasks) == 0:
            print("No tasks to toggle.")
            continue
        index = int(input("Task number to toggle: ")) - 1
        if index < 0 or index >= len(tasks):
            print("Invalid task number.")
            continue
        done_flags[index] = not done_flags[index]
        print("Task status toggled.")

    elif option == "6":
        total = len(tasks)
        done = 0
        for flag in done_flags:
            if flag:
                done += 1
        pending = total - done
        print(f"Total: {total} | Done: {done} | Pending: {pending}")

    elif option == "7":
        print("Goodbye.")
        break

    else:
        print("Invalid option. Try again.")
