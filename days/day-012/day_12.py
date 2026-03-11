"""
Day 12 — Portfolio Project Brief (No Code)
Project: StudyFlow CLI — Task and Progress Manager

Important:
- Do NOT write the solution in this file now.
- Use this file as your project specification.
- You will implement the full project by yourself in a separate coding section below.

Main topic of today:
- Lists and list modification (index update, append, remove, pop)

You should also reuse previous topics:
- input/output
- if/elif/else
- for and while
- break and continue

------------------------------------------------------------
PROJECT CONTEXT
------------------------------------------------------------
You are building a command-line tool for students to manage daily study tasks.
The app should be practical, simple to use, and complete enough to be portfolio-ready.

------------------------------------------------------------
PROJECT GOAL
------------------------------------------------------------
Create a menu-driven CLI that lets a user:
1) Add tasks
2) View tasks
3) Edit tasks
4) Remove tasks
5) Mark tasks as done/undone
6) See progress summary
7) Exit

------------------------------------------------------------
DATA MODEL REQUIREMENT (DAY 12 FOCUS)
------------------------------------------------------------
Use lists as the core data structure.
Required approach:
- A list to store task names (strings)
- A list to store task status (booleans), aligned by index

Example concept:
- tasks[i] and done_flags[i] represent the same task

Rule:
- Never let list sizes get out of sync.

------------------------------------------------------------
FUNCTIONAL REQUIREMENTS
------------------------------------------------------------
1) Add task
   - Ask user for task name
   - Reject empty names
   - Add task with default status = pending

2) List tasks
   - If no tasks, show clear message
   - If tasks exist, show task number, name, and status
   - Display task numbers starting at 1 (user-friendly)

3) Edit task
   - Ask which task number to edit
   - Validate number range
   - Ask new task name
   - Reject empty name
   - Update task by index

4) Remove task
   - Ask which task number to remove
   - Validate number range
   - Ask confirmation (yes/no)
   - If confirmed, remove task and status from both lists

5) Toggle done/undone
   - Ask which task number
   - Validate number range
   - If done -> pending, if pending -> done

6) Show progress
   - Show total tasks
   - Show done tasks
   - Show pending tasks
   - Optional: show completion percentage

7) Exit
   - End loop safely with a goodbye message

------------------------------------------------------------
VALIDATION RULES
------------------------------------------------------------
- Invalid menu option must not crash the app
- Invalid index must not crash the app
- Non-empty task names only
- Keep asking for actions until user chooses Exit

------------------------------------------------------------
FLOW REQUIREMENT
------------------------------------------------------------
Use a main while loop for the menu.
Use if/elif/else to handle options.
Use continue to skip invalid actions and return to menu quickly.
Use break to exit.

------------------------------------------------------------
PORTFOLIO QUALITY CHECKLIST
------------------------------------------------------------
Your final implementation should:
- Run from start to finish without errors
- Handle edge cases (empty list, invalid option, invalid index)
- Be readable (clear variable names)
- Show a complete user flow (not a loose snippet)
- Be easy to demo in GitHub

------------------------------------------------------------
DELIVERABLE
------------------------------------------------------------
Implement this specification below.
When you finish, test all menu options before committing.
"""

# Implement your solution below this line:

