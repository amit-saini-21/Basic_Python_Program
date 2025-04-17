import re
import tkinter as tk
from tkinter import ttk, messagebox

# Email Validation Function
def validate_email():
    email = entry.get().strip()
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if re.match(pattern, email):
        result_label.config(text=f"✅ Valid Email: {email}", foreground="green")
    else:
        result_label.config(text="❌ Invalid Email!", foreground="red")

def ask_mode():
    response = messagebox.askquestion("Mode Selection", "Do you want to use GUI mode? (Click 'No' for CLI mode)")
    if response == 'no':
        cli_mode()
    else:
        root.deiconify()
        root.lift()
        root.focus_force()

def cli_mode():
    root.destroy() 
    print("Note*:- Type 'exit' to quit.\n")

    while True:
        email = input("Enter Email: ").strip()

        if email.lower() == "exit":
            print("Exiting CLI Mode...") 
            break  
        
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        if re.match(pattern, email):
            print(f"✅ Valid Email: {email}")
        else:
            print("❌ Invalid Email!")
    
    exit()  

# Tkinter Window Setup
root = tk.Tk()
root.title("Email Validator")
root.geometry("400x250")
root.configure(bg="#1B263B")
root.resizable(False, False)  # Fix min and max size
root.withdraw()

# Ask Mode Selection
ask_mode()

# Frame
frame = tk.Frame(root, bg="#0D1B2A", padx=20, pady=20)
frame.pack(expand=True)

# Email Entry Label
entry_label = ttk.Label(frame, text="Enter Email:", font=("Arial", 12, "bold"), foreground="White", background="#0D1B2A")
entry_label.grid(row=0, column=0, pady=5, padx=5, sticky="w")

# Email Entry Box
entry = tk.Entry(frame, width=25, font=("Arial", 12), relief=tk.FLAT)
entry.grid(row=0, column=1, pady=5, padx=5)

# Validate Button
validate_button = tk.Button(frame, text="Validate", command=validate_email, bg="#E63946", fg="white", font=("Arial", 12, "bold"), width=15, height=1, relief=tk.RAISED, bd=2, cursor="hand2")
validate_button.grid(row=1, columnspan=2, pady=15)

# Output Label
result_label = ttk.Label(frame, text="Result: --", font=("Arial", 12, "bold"), foreground="#F4A261", background="#0D1B2A")
result_label.grid(row=2, columnspan=2, pady=10)

# Run Application
root.mainloop()
#commented the above code and use this
'''import re

while True:
    email = input("Enter an email to validate (or type 'exit' to quit): ").strip()
    
    if email.lower() == "exit":
        print("Exiting...")
        break
    
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if re.match(pattern, email):
        print(f"✅ Valid Email: {email}")
    else:
        print("❌ Invalid Email! Please enter a valid email.")
'''