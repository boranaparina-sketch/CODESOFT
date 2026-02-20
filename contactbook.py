from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Modern Contact Book")
root.geometry("500x600")
root.config(bg="#d9e6f2")

contacts = []


def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name == "" or phone == "":
        messagebox.showwarning("Warning", "Name and Phone are required!")
        return

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)

    result_text.insert(END,
        f"Name: {name}\n"
        f"Phone: {phone}\n"
        f"Email: {email}\n"
        f"Address: {address}\n"
        "-------------------------\n"
    )

    messagebox.showinfo("Success", "Contact Added Successfully!")
    clear_fields()

    contacts.append(contact)
    messagebox.showinfo("Success", "Contact Added Successfully!")

    clear_fields()


def search_contact():
    search_name = name_entry.get()
    result_text.delete(1.0, END)

    for contact in contacts:
        if contact["name"].lower() == search_name.lower():
            result_text.insert(END,
                f"Name: {contact['name']}\n"
                f"Phone: {contact['phone']}\n"
                f"Email: {contact['email']}\n"
                f"Address: {contact['address']}\n"
                "--------------------------\n"
            )
            return

    messagebox.showinfo("Not Found", "Contact not found!")


def delete_contact():
    delete_name = name_entry.get()

    for contact in contacts:
        if contact["name"].lower() == delete_name.lower():
            contacts.remove(contact)
            messagebox.showinfo("Deleted", "Contact Deleted Successfully!")
            return

    messagebox.showinfo("Not Found", "Contact not found!")


def show_all_contacts():
    result_text.delete(1.0, END)

    if not contacts:
        result_text.insert(END, "No contacts available.\n")
        return

    for contact in contacts:
        result_text.insert(END,
            f"Name: {contact['name']}\n"
            f"Phone: {contact['phone']}\n"
            f"Email: {contact['email']}\n"
            f"Address: {contact['address']}\n"
            "--------------------------\n"
        )


def clear_fields():
    name_entry.delete(0, END)
    phone_entry.delete(0, END)
    email_entry.delete(0, END)
    address_entry.delete(0, END)


Label(root, text="My Contact Book", font=("Arial", 20, "bold"), bg="#d9e6f2", fg="#1f4e79").pack(pady=10)

Label(root, text="Name", bg="#d9e6f2").pack()
name_entry = Entry(root, width=40)
name_entry.pack(pady=5)

Label(root, text="Phone", bg="#d9e6f2").pack()
phone_entry = Entry(root, width=40)
phone_entry.pack(pady=5)

Label(root, text="Email", bg="#d9e6f2").pack()
email_entry = Entry(root, width=40)
email_entry.pack(pady=5)

Label(root, text="Address", bg="#d9e6f2").pack()
address_entry = Entry(root, width=40)
address_entry.pack(pady=5)

Button(root, text="Add Contact", bg="green", fg="white", width=20, command=add_contact).pack(pady=5)
Button(root, text="Search Contact", bg="blue", fg="white", width=20, command=search_contact).pack(pady=5)
Button(root, text="Delete Contact", bg="red", fg="white", width=20, command=delete_contact).pack(pady=5)
Button(root, text="Show All Contacts", bg="gray", fg="white", width=20, command=show_all_contacts).pack(pady=5)

result_text = Text(root, height=10, width=55)
result_text.pack(pady=10)

root.mainloop()
