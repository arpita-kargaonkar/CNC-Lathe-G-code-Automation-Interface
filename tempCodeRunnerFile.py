import tkinter as tk
from tkinter import ttk, messagebox
import preparation
import GUI

# Function to open page2 and save G-code
def open_page2_and_save_gcode(turret_option):
    code_number = code_number_var.get()
    code_name = code_name_var.get()
    nagasa = nagasa_var.get()
    tukidasi = tukidasi_var.get()
    zairyou = zairyou_var.get()

    if not code_number or not code_name or not nagasa or not tukidasi or not zairyou:
        messagebox.showerror("Input Error", "All fields are mandatory.")
        return

    if not (GUI.validate_float_with_decimal(nagasa) and GUI.validate_float_with_decimal(tukidasi) and GUI.validate_float_with_decimal(zairyou)):
        messagebox.showerror("Input Error", "Nagasa, Tukidasi, and Zairyou must be float numbers with at least one decimal point.")
        return

    gcode_start_lower = preparation.lower_turret_start_preparation(code_number, code_name, nagasa, tukidasi, zairyou)
    gcode_start_upper = preparation.upper_turret_start_preparation(code_number, code_name, nagasa, tukidasi, zairyou)

    GUI.show_page2_frame(page2_frame, turret_option, gcode_start_lower, gcode_start_upper, code_number)

# Create the main window
root = tk.Tk()
root.title("G-code Automation Interface")

# Add main frame
main_frame = ttk.Frame(root, padding="10")
main_frame.pack(fill="both", expand=True)

# Input fields
ttk.Label(main_frame, text="Code Number").grid(row=0, column=0, padx=5, pady=5)
code_number_var = tk.StringVar()
ttk.Entry(main_frame, textvariable=code_number_var).grid(row=0, column=1, padx=5, pady=5)

ttk.Label(main_frame, text="Code Name").grid(row=1, column=0, padx=5, pady=5)
code_name_var = tk.StringVar()
ttk.Entry(main_frame, textvariable=code_name_var).grid(row=1, column=1, padx=5, pady=5)

ttk.Label(main_frame, text="Nagasa").grid(row=2, column=0, padx=5, pady=5)
nagasa_var = tk.StringVar()
ttk.Entry(main_frame, textvariable=nagasa_var).grid(row=2, column=1, padx=5, pady=5)

ttk.Label(main_frame, text="Tukidasi").grid(row=3, column=0, padx=5, pady=5)
tukidasi_var = tk.StringVar()
ttk.Entry(main_frame, textvariable=tukidasi_var).grid(row=3, column=1, padx=5, pady=5)

ttk.Label(main_frame, text="Zairyou").grid(row=4, column=0, padx=5, pady=5)
zairyou_var = tk.StringVar()
ttk.Entry(main_frame, textvariable=zairyou_var).grid(row=4, column=1, padx=5, pady=5)

# Turret in play options
ttk.Label(main_frame, text="Turret in play *").grid(row=6, column=0, padx=10, pady=5, sticky="e")
ttk.Button(main_frame, text="only left", command=lambda: open_page2_and_save_gcode("only left")).grid(row=6, column=1, padx=10, pady=5, sticky="w")
ttk.Button(main_frame, text="left and right", command=lambda: open_page2_and_save_gcode("left and right")).grid(row=7, column=1, padx=10, pady=5, sticky="w")

# Page 2 Frame (hidden initially)
page2_frame = ttk.Frame(root, padding="10")
page2_frame.pack_forget()

# Start the Tkinter loop
root.mainloop()
