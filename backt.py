import tkinter as tk
from tkinter import messagebox
from typing import List

def combo(num, target, part = []):
    s = sum(part)
    
    if s == target:
        return part

    if s >= target:
        return None

    for i in range(0, len(num)):
        n = num[i]
        remaining = num[i+1:]
        result = combo(remaining, target, part + [n])
        
        if result is not None:
            return result

    return None

def find_combination():
    try:
        num = [float(x.strip()) for x in num_entry.get().split(",")]
        target = float(target_entry.get())
        result = combo(num, target)
        if result is not None:
            result_int = [int(x) if x.is_integer() else x for x in result]
            result_label.config(text=f"Combination: {result_int}")
        else:
            result_label.config(text="No combination found")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid input")

# Create the GUI
root = tk.Tk()
root.title("Find Combination")

num_label = tk.Label(root, text="List of integers:")
num_label.grid(row=0, column=0)

num_entry = tk.Entry(root)
num_entry.grid(row=0, column=1)

target_label = tk.Label(root, text="Target number:")
target_label.grid(row=1, column=0)

target_entry = tk.Entry(root)
target_entry.grid(row=1, column=1)

find_button = tk.Button(root, text="Find Combination", command=find_combination)
find_button.grid(row=2, column=0, columnspan=2)

result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2)

root.mainloop()