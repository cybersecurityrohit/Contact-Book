import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Contact Manager")
root.geometry("500x500")
root.configure(bg="#e6f7ff")

contacts = {}

def add_contact():
    """Add a new contact."""
    name = entry_name.get().strip()
    phone = entry_phone.get().strip()
    email = entry_email.get().strip()
    address = entry_address.get().strip()

    if name == "" or phone == "":
        messagebox.showwarning("Input Error", "Name and phone number are required.")
        return
    
    contacts[name] = {"Phone": phone, "Email": email, "Address": address}
    messagebox.showinfo("Contact Added", f"Contact '{name}' added successfully.")
    clear_entries()
    display_contacts()

def display_contacts():
    """Display all contacts in the listbox."""
    listbox_contacts.delete(0, tk.END)
    for name, details in contacts.items():
        listbox_contacts.insert(tk.END, f"{name} - {details['Phone']}")

def search_contact():
    """Search for a contact by name or phone number."""
    query = entry_search.get().strip()
    listbox_contacts.delete(0, tk.END)
    found = False
    for name, details in contacts.items():
        if query.lower() in name.lower() or query == details["Phone"]:
            listbox_contacts.insert(tk.END, f"{name} - {details['Phone']}")
            found = True
    if not found:
        listbox_contacts.insert(tk.END, "No contacts found.")

def update_contact():
    """Update an existing contact's details."""
    name = entry_name.get().strip()
    if name in contacts:
        contacts[name] = {
            "Phone": entry_phone.get().strip(),
            "Email": entry_email.get().strip(),
            "Address": entry_address.get().strip(),
        }
        messagebox.showinfo("Contact Updated", f"Contact '{name}' updated successfully.")
        clear_entries()
        display_contacts()
    else:
        messagebox.showerror("Error", "Contact not found.")

def delete_contact():
    """Delete a contact by name."""
    name = entry_name.get().strip()
    if name in contacts:
        del contacts[name]
        messagebox.showinfo("Contact Deleted", f"Contact '{name}' deleted successfully.")
        clear_entries()
        display_contacts()
    else:
        messagebox.showerror("Error", "Contact not found.")

def clear_entries():
    """Clear all entry fields."""
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_address.delete(0, tk.END)
    entry_search.delete(0, tk.END)

label_title = tk.Label(root, text="Contact Manager", font=("Arial", 20, "bold"), bg="#e6f7ff")
label_title.pack(pady=10)

frame_entry = tk.Frame(root, bg="#e6f7ff")
frame_entry.pack(pady=10)

label_name = tk.Label(frame_entry, text="Name:", bg="#e6f7ff")
label_name.grid(row=0, column=0, sticky="e")
entry_name = tk.Entry(frame_entry, width=30)
entry_name.grid(row=0, column=1, padx=10, pady=5)

label_phone = tk.Label(frame_entry, text="Phone:", bg="#e6f7ff")
label_phone.grid(row=1, column=0, sticky="e")
entry_phone = tk.Entry(frame_entry, width=30)
entry_phone.grid(row=1, column=1, padx=10, pady=5)

label_email = tk.Label(frame_entry, text="Email:", bg="#e6f7ff")
label_email.grid(row=2, column=0, sticky="e")
entry_email = tk.Entry(frame_entry, width=30)
entry_email.grid(row=2, column=1, padx=10, pady=5)

label_address = tk.Label(frame_entry, text="Address:", bg="#e6f7ff")
label_address.grid(row=3, column=0, sticky="e")
entry_address = tk.Entry(frame_entry, width=30)
entry_address.grid(row=3, column=1, padx=10, pady=5)

btn_add = tk.Button(root, text="Add Contact", width=15, command=add_contact)
btn_add.pack(pady=5)

btn_update = tk.Button(root, text="Update Contact", width=15, command=update_contact)
btn_update.pack(pady=5)

btn_delete = tk.Button(root, text="Delete Contact", width=15, command=delete_contact)
btn_delete.pack(pady=5)

frame_search = tk.Frame(root, bg="#e6f7ff")
frame_search.pack(pady=10)

label_search = tk.Label(frame_search, text="Search:", bg="#e6f7ff")
label_search.grid(row=0, column=0)
entry_search = tk.Entry(frame_search, width=20)
entry_search.grid(row=0, column=1, padx=10)
btn_search = tk.Button(frame_search, text="Search", command=search_contact)
btn_search.grid(row=0, column=2)

listbox_contacts = tk.Listbox(root, width=50, height=10)
listbox_contacts.pack(pady=10)

display_contacts()

root.mainloop()
