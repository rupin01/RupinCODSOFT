import tkinter as tk

# Define an empty list to store the tasks
tasks = []

# Define a function to add a task to the list
def add_task():
    task = task_entry.get()
    if task != "":
        tasks.append(task)
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)

# Define a function to remove a task from the list
def remove_task():
    selected_tasks = task_list.curselection()
    for i in selected_tasks:
        task_list.delete(i)
        tasks.pop(i)

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create the task entry field and button
task_entry = tk.Entry(root, width=30)
task_entry.pack(side=tk.LEFT, padx=5)
add_button = tk.Button(root, text="Add", command=add_task)
add_button.pack(side=tk.LEFT, padx=5)

# Create the task list and scrollbar
task_list = tk.Listbox(root, height=10, width=50)
task_list.pack(side=tk.LEFT, padx=5, pady=5)
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
task_list.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=task_list.yview)

# Create the remove button
remove_button = tk.Button(root, text="Remove", command=remove_task)
remove_button.pack(side=tk.BOTTOM, pady=5)

# Start the main event loop
root.mainloop()