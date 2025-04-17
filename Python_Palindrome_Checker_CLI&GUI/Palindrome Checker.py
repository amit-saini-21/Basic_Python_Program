import tkinter as tk
from tkinter import ttk, messagebox
import re

def check_palindrome():
    input_text = entry.get().strip()
    if not input_text:
        messagebox.showwarning("Warning", "Please enter a string to check!")
        return
    
    cleaned_text = re.sub(r'[^a-zA-Z0-9]', '', input_text).lower()  # Remove non-alphanumeric characters & convert to lowercase
    is_palindrome = cleaned_text == cleaned_text[::-1]
    
    output_text.config(state=tk.NORMAL)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, "✅ Palindrome" if is_palindrome else "❌ Not a Palindrome")
    output_text.config(state=tk.DISABLED)

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
        user_input = input("Enter a string to check palindrome: ").strip()

        if user_input.lower() == "exit":
            print("Exiting CLI Mode...")
            break

        cleaned_text = re.sub(r'[^a-zA-Z0-9]', '', user_input).lower()
        if cleaned_text == cleaned_text[::-1]:
            print(f"✅ '{user_input}' is a Palindrome")
        else:
            print(f"❌ '{user_input}' is NOT a Palindrome")
    
    exit()

# Tkinter window setup
root = tk.Tk()
root.title("Palindrome Checker")
root.geometry("500x300")
root.resizable(False, False)
root.configure(bg="#1B263B")
root.withdraw()

# Ask mode selection
ask_mode()

# Frame
frame = tk.Frame(root, bg="#0D1B2A", padx=20, pady=20)
frame.pack(expand=True)

# Input field
entry_label = ttk.Label(frame, text="Enter a string:", font=("Arial", 16, "bold"), foreground="White", background="#0D1B2A")
entry_label.pack(pady=5)
entry = tk.Entry(frame, width=40, font=("Arial", 12), relief=tk.FLAT)
entry.pack(pady=5)

# Check button
check_button = tk.Button(frame, text="Check Palindrome", command=check_palindrome, bg="#E63946", fg="white", font=("Arial", 12, "bold"), width=20, height=1, relief=tk.RAISED, bd=2, cursor="hand2")
check_button.pack(pady=10)

# Output text area
output_frame = tk.Frame(frame, bg="#0D1B2A")
output_frame.pack(pady=5, fill=tk.BOTH, expand=True)

output_text = tk.Text(output_frame, height=2, wrap=tk.WORD, font=("Arial", 14, "bold"), fg="#F4A261", bg="#0D1B2A", state=tk.DISABLED)
output_text.pack(fill=tk.BOTH, expand=True)

# Run the application
root.mainloop()

#comment the above code and use this
'''def is_palindrome(text):
    return text == text[::-1]

while True:
    text = input("Enter a string (or type 'exit' to quit): ").strip()
    if text.lower() == "exit":
        print("Exiting...")
        break
    if is_palindrome(text):
        print("✅ Palindrome")
    else:
        print("❌ Not a Palindrome")'''
