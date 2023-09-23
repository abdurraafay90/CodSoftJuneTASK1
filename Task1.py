import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry('300x300')
        self.root.title("To-Do List")

        self.tasks = []

        self.task_entry = tk.Entry(root)
        self.task_entry.pack()

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.task_listbox = tk.Listbox(root)
        self.task_listbox.pack()

        self.complete_button = tk.Button(root, text="Delete Task", command=self.complete_task)
        self.complete_button.pack()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")

    def complete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            completed_task = self.tasks.pop(selected_index[0])
            self.update_task_list()
            messagebox.showinfo("Task Deleted", f"Deleted: {completed_task}")
        else:
            messagebox.showwarning("Warning", "Select a task to complete!")

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

def main():
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()

main()