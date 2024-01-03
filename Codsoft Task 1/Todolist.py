import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x250+500+300")
root.resizable(100,100)
root.configure(bg="#F0F8FF")


def add_task():
    task = enterTaskField.get()
    if len(task)==0:
        messagebox.showinfo('Error', 'TaskField is Empty!') 
    else:
        messagebox.showinfo('Great!','Task added Successfully.') 
    listbox.insert(tk.END, task)
    enterTaskField.delete(0, tk.END)
    
    
def delete_task():
    selected_index = listbox.curselection()
    if selected_index:
        listbox.delete(selected_index)
        messagebox.showinfo('Great!','Task deleted successfully')


label1 = ttk.Label(root, text="Enter Your Task")
label1.grid(row=0, column=0, padx=5, pady=5)

enterTaskField = ttk.Entry(root)
enterTaskField.grid(row=0, column=1, padx=5, pady=5)

addTaskButton = ttk.Button(root, text="Add Task", command=add_task)
addTaskButton.grid(row=1, column=0, padx=5, pady=5)

listbox = tk.Listbox(root, height=10)
listbox.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

deleteTaskButton = ttk.Button(root, text="Delete Task", command=delete_task)
deleteTaskButton.grid(row=3, column=0, padx=5, pady=5)

exitButton = ttk.Button(root, text="Exit", command=root.quit)
exitButton.grid(row=3, column=1, padx=5, pady=5)

root.mainloop()
