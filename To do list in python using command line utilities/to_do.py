import argparse 
from functools import reduce

parser = argparse.ArgumentParser(description = "To Do list")
 
# parser.add_argument("action", choices = ["add", "view", "remove", "done"])
# parser.add_argument("--task", type = str, help = "Enter the task description")
# parser.add_argument("--index", type = int, help = "Index of the task for(remove / done)")

parser.add_argument("--add", type = str, help =  "Add a new task")
parser.add_argument("--view", action = "store_true", help =  "View all the tasks")
parser.add_argument("--delete", type = int, help = "Delete a task by its number")
parser.add_argument("--done", type = int, help = "Marks taks number as done")

args = parser.parse_args()
if args.add:
    with open("tasks.txt", "a") as f:
        f.write(f"{args.add} \n")
    print(f"Task added : {args.add}")

elif args.view:
    try:
        with open("tasks.txt", "r") as f:
            tasks = f.readlines()
            if tasks:
                print("Your tasks : ")
                for i, task in enumerate (tasks, start = 1):
                    print(f"{i}. {task.strip()}")
            else:
                print("No task found.")
    except FileNotFoundError:
        print("Task list is empty")
    
elif args.delete:
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        
        if 1 <= args.delete <= len(tasks):
            deleted_task = tasks.pop(args.delete - 1)
            with open("tasks.txt", "w") as file:
                file.writelines(tasks)
            print(f"Deleted task : {deleted_task.strip()}")
        else:
            print("Invalid task number.")
    except FileNotFoundError:
        print("No task file found.")

elif args.done:
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()

        if 1 <= args.done <= len(tasks):
            index = args.done - 1
            if not tasks[index].startswith("[x] "):
                tasks[index] = "[x]" + tasks[index]
                with open("tasks.txt", "w") as file:
                    file.writelines(tasks)
                print(f"Marked task {args.done} as done.")
            else:
                print("Task is already marked as done")
        else:
            print("Invalid task number.")

    except FileNotFoundError:
        print("Task list is empty.")


# Add More Features to Your To-Do App (Mini Extensions).

# Make it even better:

#  Add due dates (--due)

#  Add priorities (--priority high/medium/low)

#  Save tasks as JSON instead of plain text

#  Add a --clear option to remove all tasks

# Great way to polish your current skills.