import tkinter as tk
from tkinter import messagebox
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('medication_tracker.db')
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS medications
              (id INTEGER PRIMARY KEY, name TEXT, dosage TEXT, schedule TEXT)''')
conn.commit()

def add_medication():
    name = name_entry.get()
    dosage = dosage_entry.get()
    schedule = schedule_entry.get()
    
    if name and dosage and schedule:
        cursor.execute("INSERT INTO medications (name, dosage, schedule) VALUES (?, ?, ?)", (name, dosage, schedule))
        conn.commit()
        messagebox.showinfo("Success", "Medication added successfully!")
        name_entry.delete(0, tk.END)
        dosage_entry.delete(0, tk.END)
        schedule_entry.delete(0, tk.END)
        display_medications()
    else:
        messagebox.showwarning("Input Error", "Please fill all fields.")

def display_medications():
    cursor.execute("SELECT * FROM medications")
    rows = cursor.fetchall()
    listbox.delete(0, tk.END)
    for row in rows:
        listbox.insert(tk.END, f"Name: {row[1]}, Dosage: {row[2]}, Schedule: {row[3]}")

# Create main window
root = tk.Tk()
root.title("Medication Tracker")

# Create and place labels and entries for medication details
tk.Label(root, text="Medication Name:").grid(row=0, column=0, padx=10, pady=10)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Dosage:").grid(row=1, column=0, padx=10, pady=10)
dosage_entry = tk.Entry(root)
dosage_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Schedule:").grid(row=2, column=0, padx=10, pady=10)
schedule_entry = tk.Entry(root)
schedule_entry.grid(row=2, column=1, padx=10, pady=10)

# Create and place Add button
add_button = tk.Button(root, text="Add Medication", command=add_medication)
add_button.grid(row=3, column=0, columnspan=2, pady=10)

# Create and place listbox to display medications
listbox = tk.Listbox(root, width=50)
listbox.grid(row=4, column=0, columnspan=2, pady=10)

# Display medications
display_medications()

# Run the application
root.mainloop()
