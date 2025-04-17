import tkinter as tk
from tkinter import ttk, messagebox

def reverse_string():
    input_text = entry.get().strip()
    if not input_text:
        messagebox.showwarning("Warning", "Please enter a string to reverse!")
        return
    reversed_text = input_text[::-1]
    output_text.config(state=tk.NORMAL)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, reversed_text)
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
    user_input = input("Enter a string to reverse: ").strip()
    print("Reversed String:", user_input[::-1])
    input("Press Enter to exit...")
    exit()
# Tkinter window setup
root = tk.Tk()
root.title("String Reversal App")
root.geometry("500x300")
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

# Reverse button
reverse_button = tk.Button(frame, text="Reverse", command=reverse_string, bg="#E63946", fg="white", font=("Arial", 12, "bold"), width=15, height=1, relief=tk.RAISED, bd=2, cursor="hand2")
reverse_button.pack(pady=10)

# Output text area with scrollbar
output_frame = tk.Frame(frame, bg="#0D1B2A")
output_frame.pack(pady=5, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(output_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

output_text = tk.Text(output_frame, height=4, wrap=tk.WORD, font=("Arial", 12), fg="#F4A261", bg="#0D1B2A", state=tk.DISABLED, yscrollcommand=scrollbar.set)
output_text.pack(fill=tk.BOTH, expand=True)

scrollbar.config(command=output_text.yview)

# Run the application
root.mainloop()
#commented the above code and use this
'''while True:
    text = input("Enter a string to reverse (or type 'exit' to quit): ").strip()
    if text.lower() == "exit":
        print("Exiting...")
        break
    print("Reversed String:", text[::-1])
'''