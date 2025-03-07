import tkinter as tk
from tkinter import messagebox

def submit_feedback():
    name = name_entry.get()
    email = email_entry.get()
    rating = rating_var.get()
    comments = comments_text.get("1.0", tk.END).strip()
    
    if not name or not email or not rating:
        messagebox.showerror("Error", "Please fill out all required fields.")
        return

    feedback = f"\nName: {name}\nEmail: {email}\nRating: {rating}\nComments: {comments}\nm"
    print(feedback)  # You can save this data to a file or database
    # feedback = '\nvery nice'
    with open('mydata.txt', 'a') as f:
        f.write(feedback)
    messagebox.showinfo("Thank You!", "Your feedback has been submitted.")
    root.destroy()


# Create the main window
root = tk.Tk()
root.title("Customer Feedback Form")
root.geometry("400x500")


# Name label and entry
tk.Label(root, text="Name:").pack(pady=5)
name_entry = tk.Entry(root, width=40)
name_entry.pack()

# Email label and entry
tk.Label(root, text="Email:").pack(pady=5)
email_entry = tk.Entry(root, width=40)
email_entry.pack()

# Rating label and radio buttons
tk.Label(root, text="Rating:").pack(pady=5)
rating_var = tk.StringVar(value="")
for i in range(1, 6):
    tk.Radiobutton(root, text=str(i), variable=rating_var, value=str(i)).pack()

# Comments label and text box
tk.Label(root, text="Comments:").pack(pady=5)
comments_text = tk.Text(root, height=5, width=40)
comments_text.pack()

# Submit button
tk.Button(root, text="Submit", command=submit_feedback).pack(pady=20)

root.mainloop()
