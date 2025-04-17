import tkinter as tk
from tkinter import ttk, messagebox

def convert_temperature():
    try:
        temp_value = float(entry.get().strip())
        from_unit = from_unit_var.get()
        to_unit = to_unit_var.get()

        if from_unit == to_unit:
            converted_temp = temp_value  # Same unit
        elif from_unit == "Celsius" and to_unit == "Fahrenheit":
            converted_temp = (temp_value * 9/5) + 32
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            converted_temp = (temp_value - 32) * 5/9
        else:
            messagebox.showerror("Error", "Invalid Conversion")
            return

        output_label.config(text=f"Converted Temperature: {converted_temp:.2f}° {to_unit}")

    except ValueError:
        messagebox.showwarning("Warning", "Please enter a valid number!")

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
    try:
        temp_value = float(input("Enter Temperature Value: ").strip())
        from_unit = input("Enter Current Unit (Celsius/Fahrenheit): ").strip().capitalize()
        to_unit = input("Convert to (Celsius/Fahrenheit): ").strip().capitalize()

        if from_unit == to_unit:
            converted_temp = temp_value
        elif from_unit == "Celsius" and to_unit == "Fahrenheit":
            converted_temp = (temp_value * 9/5) + 32
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            converted_temp = (temp_value - 32) * 5/9
        else:
            print("Invalid conversion!")
            return

        print(f"Converted Temperature: {converted_temp:.2f}° {to_unit}")
    except ValueError:
        print("Invalid input! Please enter a valid number.")
    
    input("Press Enter to exit...")  # CLI Window tab tak open rahega jab tak enter na ho
    exit()

# Tkinter window setup
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("400x300")
root.configure(bg="#1B263B")
root.resizable(False, False)  # Fix min and max size
root.withdraw()

# Ask mode selection
ask_mode()

# Frame
frame = tk.Frame(root, bg="#0D1B2A", padx=20, pady=20)
frame.pack(expand=True)

# Input Temperature
entry_label = ttk.Label(frame, text="Enter Temperature:", font=("Arial", 12, "bold"), foreground="White", background="#0D1B2A")
entry_label.grid(row=0, column=0, pady=5, padx=5, sticky="w")
entry = tk.Entry(frame, width=15, font=("Arial", 12), relief=tk.FLAT)
entry.grid(row=0, column=1, pady=5, padx=5)

# Input Unit Dropdown
from_unit_var = tk.StringVar(value="Celsius")
from_unit_label = ttk.Label(frame, text="From:", font=("Arial", 12), foreground="White", background="#0D1B2A")
from_unit_label.grid(row=1, column=0, pady=5, padx=5, sticky="w")
from_unit_menu = ttk.Combobox(frame, textvariable=from_unit_var, values=["Celsius", "Fahrenheit"], state="readonly", width=12)
from_unit_menu.grid(row=1, column=1, pady=5, padx=5)

# Output Unit Dropdown
to_unit_var = tk.StringVar(value="Fahrenheit")
to_unit_label = ttk.Label(frame, text="To:", font=("Arial", 12), foreground="White", background="#0D1B2A")
to_unit_label.grid(row=2, column=0, pady=5, padx=5, sticky="w")
to_unit_menu = ttk.Combobox(frame, textvariable=to_unit_var, values=["Celsius", "Fahrenheit"], state="readonly", width=12)
to_unit_menu.grid(row=2, column=1, pady=5, padx=5)

# Convert Button
convert_button = tk.Button(frame, text="Convert", command=convert_temperature, bg="#E63946", fg="white", font=("Arial", 12, "bold"), width=15, height=1, relief=tk.RAISED, bd=2, cursor="hand2")
convert_button.grid(row=3, columnspan=2, pady=15)

# Output Label
output_label = ttk.Label(frame, text="Converted Temperature: --", font=("Arial", 12, "bold"), foreground="#F4A261", background="#0D1B2A")
output_label.grid(row=4, columnspan=2, pady=10)

# Run the application
root.mainloop()

#commented the above code and use this
'''def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

while True:
    print("\nTemperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Exit")

    choice = input("Choose an option (1/2/3): ").strip()

    if choice == '1':
        temp = float(input("Enter temperature in Celsius: "))
        print(f"Converted Temperature: {celsius_to_fahrenheit(temp):.2f}°F")
    elif choice == '2':
        temp = float(input("Enter temperature in Fahrenheit: "))
        print(f"Converted Temperature: {fahrenheit_to_celsius(temp):.2f}°C")
    elif choice == '3':
        print("Exiting...")
        break
    else:
        print("Invalid choice! Please enter 1, 2, or 3.")
'''