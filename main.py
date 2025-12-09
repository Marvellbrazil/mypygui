import crud_user as crud
import connection as conpy
import tkinter as tk
from tkinter import messagebox, ttk

# Prepared Helper Functions
def showmsg(type, msg):
    match type:
        case 1:
            messagebox.showerror("Error", msg)
        case 2:
            messagebox.showinfo("Info", msg)
        case 3:
            messagebox.showwarning("Warning", msg)

# GUI Functions
def submit_form():
    name = txt_name.get()
    age = txt_age.get()
    email = txt_email.get()
    
    if not name or not age or not email:
        showmsg(3, "All fields must be filled")
        return
    
    res = crud.create(name, age, email)
    if res:
        showmsg(2, "Successfully created user")
    txt_name.delete(0, tk.END)
    txt_age.delete(0, tk.END)
    txt_email.delete(0, tk.END)

def show_data():
    data = crud.read()
    
    window_list = tk.Toplevel(root)
    window_list.title("User List")
    window_list.geometry("800x800")
    
    tree = ttk.Treeview(window_list, columns=("id", "name", "age", "email"), show="headings")
    tree.heading("id", text="ID")
    tree.heading("name", text="Name")
    tree.heading("age", text="Age")
    tree.heading("email", text="Email")
    tree.pack(fill=tk.BOTH, expand=True)
    
    for row in data:
        tree.insert("", tk.END, values=row)


# Main Window
root = tk.Tk()
root.title("User Form")
root.geometry("450x350")

tk.Label(root, text="Name").pack(anchor="w", pady=5, padx=15)
txt_name = tk.Entry(root, width=30)
txt_name.pack(anchor="w", padx=15)

tk.Label(root, text="Age").pack(anchor="w", pady=5, padx=15)
txt_age = tk.Entry(root, width=30)
txt_age.pack(anchor="w", padx=15)

tk.Label(root, text="Email").pack(anchor="w", pady=5, padx=15)
txt_email = tk.Entry(root, width=30)
txt_email.pack(anchor="w", padx=15)

tk.Button(root, text="Submit", width=15, command=submit_form).pack(anchor="w", pady=10, padx=15)
tk.Button(root, text="Show Data", width=15, command=show_data).pack(anchor="w", padx=15)


# INIT
conpy.init_db()
root.mainloop()