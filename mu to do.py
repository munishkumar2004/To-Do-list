import tkinter as tk
from tkinter import messagebox
from tkinter import*

class ToDoList:
    def __init__(main, root):
        main.root = root
        main.root.title("To-Do List App")
        main.root.geometry("500x400")
          
        main.tasks = []

        main.task_entry = tk.Entry(root, width=40, font=('Arial', 16))
        main.task_entry.grid(row=0, column=0, padx=10, pady=10)

        create_button = tk.Button(root, text="create Task", command=main.create_task, font=('Arial', 16), fg="red") 
        create_button.grid(row=0, column=1, padx=10, pady=10)

        main.task_listbox = tk.Listbox(root, width=40, height=10, font=('Arial', 16), fg="white", selectbackground="white")  
        main.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        
        complete_button = tk.Button(root, text="Complete Task", command=main.complete_task, font=('Arial', 16), fg="blue")  
        complete_button.grid(row=2, column=1, padx=10, pady=10, sticky = "es")

        remove_button = tk.Button(root, text="Remove Task", command=main.remove_task, font=('Arial', 16), fg="green")  
        remove_button.grid(row=2, column=0, padx=10, pady=10, sticky="es")

        update_button = tk.Button(root, text="update Task", command=main.update_task_list, font=('Arial', 16), fg="blue")  
        update_button.grid(row=0, column=2, padx=10, pady=10, sticky = "es")


        main.task_listbox.bind('<Triple-Button-1>', lambda event: main.complete_task())


    def create_task(main):
        task = main.task_entry.get()
        if task:
            main.tasks.append(task)
            main.update_task_list()
            main.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "you must have enter a task.")

    def update_task(main):
        selected_task_index = main.task_listbox.curselection()
        if selected_task_index:

            new_task =main.task("Update Task", "Enter new task:")
            if new_task:
                main.tasks[selected_task_index[0]] = new_task
                main.update_task_list()
        else:
            messagebox.showwarning("Warning", "You must select a task to update.")
        

    def remove_task(main):
        selected_task_index = main.task_listbox.curselection()
        if selected_task_index:
            main.tasks.pop(selected_task_index[0])
            main.update_task_list()
        else:
            messagebox.showwarning("Warning", "You must select a task to remove.")
    

    def complete_task(main):
        selected_task_index = main.task_listbox.curselection()
        if selected_task_index:
            completed_task = main.tasks.pop(selected_task_index[0])
            completed_task = "[Done] {completed_task}"
            main.tasks.append(completed_task)
            main.update_task_list()
        else:
            messagebox.showwarning("Warning", "You must select a task to complete.")
    
    
    def update_task_list(main):
        main.task_listbox.delete(0, tk.END)
        for task in main.tasks:
            main.task_listbox.insert(tk.END, task)

root = Tk()
root.title("Python To-Do List")
to_do_list = ToDoList(root)
root.mainloop()