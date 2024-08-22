import tkinter as tk
from tkinter import ttk, messagebox
import os
import preparation
import list_of_tools_lower_left
import list_of_tools_lower_right
import list_of_tools_upper_left
import list_of_tools_upper_right

def validate_float_with_decimal(input):
    try:
        float(input)
        if '.' in input:
            return True
        return False
    except ValueError:
        return False

def show_page2_frame(page2_frame, turret_option, gcode_start_lower, gcode_start_upper, code_number):
    page2_frame.pack(fill="both", expand=True)
    # Add Upper Turret and Lower Turret labels
    upper_turret_label = ttk.Label(page2_frame, text="Upper Turret", background="lightblue", anchor="center")
    lower_turret_label = ttk.Label(page2_frame, text="Lower Turret", background="lightblue", anchor="center")
    
    lower_turret_label.grid(row=0, column=2, columnspan=2, sticky=(tk.W + tk.E), padx=5, pady=5)
    upper_turret_label.grid(row=0, column=0, columnspan=2, sticky=(tk.W + tk.E), padx=5, pady=5)

    
    def on_tool_name_selected(event, tool_type_box, parameters_label, parameters_entry):
        selected_tool_name = event.widget.get()
        if selected_tool_name in ["NEJI / Thread", "NEJI", "NEJI R"]:
            tool_type_box['values'] = list_of_tools_lower_left.neji_options
            tool_type_box.state(['!disabled'])
            parameters_entry.state(['disabled'])
            parameters_label.config(text="Parameters")
        elif selected_tool_name in ["ER NEJI", "ER NEJI R"]:
            tool_type_box['values'] = list_of_tools_lower_left.er_neji_options
            tool_type_box.state(['!disabled'])
            parameters_entry.state(['disabled'])
            parameters_label.config(text="Parameters")
        elif selected_tool_name in ["DRILL", "DRILL R"]:
            tool_type_box.set('')
            tool_type_box['values'] = []
            tool_type_box.state(['disabled'])
            parameters_entry.state(['!disabled'])
            parameters_label.config(text="Parameters - Diameter")
        elif selected_tool_name == "HEX MILLING":
            tool_type_box.set('')
            tool_type_box['values'] = []
            tool_type_box.state(['disabled'])
            parameters_entry.state(['!disabled'])
            parameters_label.config(text="Parameters - Wrench flat; -Y; +Y; Count")
        else:
            tool_type_box.set('')
            tool_type_box['values'] = []
            tool_type_box.state(['disabled'])
            parameters_entry.state(['disabled'])
            parameters_label.config(text="Parameters")

    def set_placeholder(widget, placeholder_text):
        def on_focus_in(event):
            if widget.get() == placeholder_text:
                widget.delete(0, tk.END)
                widget.config(foreground='black')

        def on_focus_out(event):
            if widget.get() == "":
                widget.insert(0, placeholder_text)
                widget.config(foreground='grey')

        widget.insert(0, placeholder_text)
        widget.config(foreground='grey')
        widget.bind("<FocusIn>", on_focus_in)
        widget.bind("<FocusOut>", on_focus_out)

    def add_rows(subcolumn_frame, side, tool_name_options):
        current_row = subcolumn_frame.grid_size()[1]
        index = current_row // 3 + 1  # Calculate index for naming purposes
        # Tool number text box
        tool_number_box = ttk.Entry(subcolumn_frame, width=10)
        tool_number_box.grid(row=current_row, column=0, padx=5, pady=5)
        set_placeholder(tool_number_box, "Tool No.")  # Add placeholder
        # Tool name dropdown menu
        #tool_name_options = ["3.0 BIT ARA", "1.5 BIT ARA", "NEJI / Thread", "NAKAGURI", "ER NEJI", "DRILL", "Others"]
        tool_name_box = ttk.Combobox(subcolumn_frame, values=tool_name_options, width=10)
        tool_name_box.grid(row=current_row, column=1, padx=5, pady=5)
        set_placeholder(tool_name_box, "Tool Name")  # Add placeholder
        # Tool type text box / dropdown
        tool_type_box = ttk.Combobox(subcolumn_frame, width=10)
        tool_type_box.grid(row=current_row, column=2, padx=5, pady=5)
        tool_type_box.state(['disabled'])  # Initially disable the tool type box
        # parameters label
        parameters_label = ttk.Label(subcolumn_frame, text="Parameters")
        parameters_label.grid(row=current_row + 1, column=0, columnspan=3, pady=5)
        # parameters text box
        parameters_entry = ttk.Entry(subcolumn_frame, width=30)
        parameters_entry.grid(row=current_row + 2, column=0, columnspan=3, padx=5, pady=5)
        parameters_entry.state(['disabled'])  # Initially disable the parameters text box
        parameters_label.config(text="Parameters")
        # Bind the event to handle tool name selection
        tool_name_box.bind("<<ComboboxSelected>>", lambda event, tool_type_box=tool_type_box,parameters_label=parameters_label, parameters_entry=parameters_entry: on_tool_name_selected(event, tool_type_box,parameters_label, parameters_entry))
        # Increment current_row by 3 to account for the newly added rows
        return current_row + 3, tool_number_box, tool_name_box, tool_type_box, parameters_label, parameters_entry, index




    def create_subcolumn(parent, col, subcol_title, side, tool_name_options):
        # Subcolumn frame
        subcolumn_frame = ttk.Frame(parent)
        subcolumn_frame.grid(row=1, column=col, padx=5, pady=5)

        # Subcolumn title
        subcol_label = ttk.Label(subcolumn_frame, text=subcol_title)
        subcol_label.grid(row=0, column=0, columnspan=3, pady=5)

        entries = []
        for _ in range(3):
            current_row, tool_number_box, tool_name_box, tool_type_box, parameters_label, parameters_entry, index = add_rows(subcolumn_frame, side, tool_name_options)
            entries.append((tool_number_box, tool_name_box, tool_type_box, parameters_label, parameters_entry, index))

        # Add subcolumn frame to the list
        return subcolumn_frame, entries

    left_upper_frame, left_upper_entries = create_subcolumn(page2_frame, 0, "Left Upper", "left", list_of_tools_upper_left.get_tool_name_options())
    right_upper_frame, right_upper_entries = create_subcolumn(page2_frame, 1, "Right Upper", "right", list_of_tools_upper_right.get_tool_name_options())
    left_lower_frame, left_lower_entries = create_subcolumn(page2_frame, 2, "Left Lower", "left", list_of_tools_lower_left.get_tool_name_options())
    right_lower_frame, right_lower_entries = create_subcolumn(page2_frame, 3, "Right Lower", "right", list_of_tools_lower_right.get_tool_name_options())

    # Function to disable all widgets in a frame
    def disable_frame(frame):
        for widget in frame.winfo_children():
            widget.config(state='disabled')
    # Function to enable all widgets in a frame
    def enable_frame(frame):
        for widget in frame.winfo_children():
            widget.config(state='normal')

    if turret_option == "only left":
        disable_frame(right_upper_frame)
        disable_frame(right_lower_frame)
        
    # Function to add rows to all subcolumns
    def add_rows_to_all():
        for subcolumn_frame, side in [(left_upper_frame, "left"), (right_upper_frame, "right"), (left_lower_frame, "left"), (right_lower_frame, "right")]:
            
            if side == "left":
                if subcolumn_frame == left_upper_frame:
                    tool_name_options=["HEX MILLING", "ABC"]
                else:
    # Apply turret option
                    tool_name_options=["CTR DRILL","DRILL", "3.0 BIT ARA", "1.5 BIT ARA", "NAKAGURI", "NEJI", "ER NEJI"]
            else:
                if subcolumn_frame == right_upper_frame:
                    tool_name_options=["HEX MILLING R"]
                else:
                    tool_name_options=["CTR DRILL R", "DRILL R", "3.0 BIT ARA R", "1.5 BIT ARA", "NAKAGURI R", "NEJI R", "ER NEJI R"]
            current_row, tool_number_box, tool_name_box, tool_type_box, parameters_label, parameters_entry, index = add_rows(subcolumn_frame, side, tool_name_options)
            if side == "left":
                if subcolumn_frame == left_upper_frame:
                    left_upper_entries.append((tool_number_box, tool_name_box, tool_type_box, parameters_label, parameters_entry, index))
                else:
                    left_lower_entries.append((tool_number_box, tool_name_box, tool_type_box, parameters_label, parameters_entry, index))
            else:
                if subcolumn_frame == right_upper_frame:
                    right_upper_entries.append((tool_number_box, tool_name_box, tool_type_box, parameters_label, parameters_entry, index))
                else:
                    right_lower_entries.append((tool_number_box, tool_name_box, tool_type_box, parameters_label, parameters_entry, index))
        # Reapply the disable settings after adding rows
        if turret_option == "only left":
            disable_frame(right_upper_frame)
            disable_frame(right_lower_frame)

    # Function to delete the last row from all subcolumns
    def delete_rows_from_all():
        for subcolumn_frame, entries, side in [(left_upper_frame, left_upper_entries, "left"), (right_upper_frame, right_upper_entries, "right"), (left_lower_frame, left_lower_entries, "left"), (right_lower_frame, right_lower_entries, "right")]:
            if entries:
                entry = entries.pop()
                tool_number_box, tool_name_box, tool_type_box, parameters_label, parameters_entry, index = entry

                # Destroy all widgets in the entry
                tool_number_box.destroy()
                tool_name_box.destroy()
                tool_type_box.destroy()
                parameters_label.destroy()
                parameters_entry.destroy()

                # Reapply the disable settings after deleting rows
                if turret_option == "only left":
                    disable_frame(right_upper_frame)
                    disable_frame(right_lower_frame)

    entries_dict = {
        'left_upper': left_upper_entries,
        'right_upper': right_upper_entries,
        'left_lower': left_lower_entries,
        'right_lower': right_lower_entries
    }

    # Function to clear all text boxes
    def clear_all_fields():
        for entry_group in entries_dict.values():
            for entry_set in entry_group:
                for widget in entry_set:
                    if isinstance(widget, ttk.Entry):
                        widget.delete(0, tk.END)
                    elif isinstance(widget, ttk.Combobox):
                        widget.set('')

    # Add button to add more rows
    add_rows_button = ttk.Button(page2_frame, text="Add Rows", command=add_rows_to_all)
    add_rows_button.grid(row=2, column=0)

    # Add button to delete rows from all subcolumns
    delete_button = ttk.Button(page2_frame, text="Delete Row", command=delete_rows_from_all)
    delete_button.grid(row=2, column=2)

    # Button to clear all text boxes
    clear_button = ttk.Button(page2_frame, text="Clear", command=clear_all_fields)
    clear_button.grid(row=2, column=3)


    def generate_and_save_gcode():
        combined_gcode_lower = gcode_start_lower # Start with page1 G-code
        combined_gcode_upper = gcode_start_upper  # Initialize lower turret G-code
        print(combined_gcode_lower)
        # Generate tool G-code for upper turret
        for entry in left_upper_entries:
            tool_number_box, tool_name_box, tool_type_box, parameters_label, parameters_entry, index = entry
            tool_number = tool_number_box.get()
            tool_name = tool_name_box.get()
            tool_type = tool_type_box.get()  # Get tool type
            parameters = parameters_entry.get()  # Get parameters

            if tool_number and tool_name:
                gcode = list_of_tools_upper_left.upper_left_gcode(tool_number, tool_name, index, parameters)
                if gcode:
                    combined_gcode_lower += gcode
            wait = f"""N{100 + 10 * (index)}\n            
            M{100 + 10 * (index)}(W)\n\n"""
            combined_gcode_upper += wait
            

        for entry in right_upper_entries:
            tool_number_box, tool_name_box, tool_type_box, parameters_label, parameters_entry, index = entry
            tool_number = tool_number_box.get()
            tool_name = tool_name_box.get()
            tool_type = tool_type_box.get()  # Get tool type
            parameters = parameters_entry.get()  # Get parameters

            if tool_number and tool_name:
                gcode = list_of_tools_upper_right.upper_right_gcode(tool_number, tool_name, index, parameters)
                if gcode:
                    combined_gcode_upper += gcode
            wait = f"""N{100 + 10 * (index)}\n            
            M{100 + 10 * (index)}(W)\n\n"""
            combined_gcode_upper += wait
                    
        # Generate tool G-code for lower turret
        for entry in left_lower_entries:
            tool_number_box, tool_name_box, tool_type_box, parameters_label, parameters_entry, index = entry
            tool_number = tool_number_box.get()
            tool_name = tool_name_box.get()
            tool_type = tool_type_box.get()  # Get tool type
            parameters = parameters_entry.get()  # Get parameters

            if tool_number and tool_name:
                gcode = list_of_tools_lower_left.lower_left_gcode(tool_number, tool_name, index, parameters)    
                if gcode:
                    combined_gcode_lower += gcode
            wait = f"""N{100 + 10 * (index)}\n            
            M{100 + 10 * (index)}(W)\n\n"""
            combined_gcode_lower += wait

        for entry in right_lower_entries:
            tool_number_box, tool_name_box, tool_type_box, parameters_label, parameters_entry, index = entry
            tool_number = tool_number_box.get()
            tool_name = tool_name_box.get()
            tool_type = tool_type_box.get()  # Get tool type
            parameters = parameters_entry.get()  # Get parameters

            if tool_number and tool_name:
                gcode = list_of_tools_lower_right.lower_right_gcode(tool_number, tool_name, index, parameters)
                if gcode:
                    combined_gcode_lower += gcode
            wait = f"""N{100 + 10 * (index)}           
            M{100 + 10 * (index)}(W)\n\n"""
            combined_gcode_lower += wait

        combined_gcode_lower += preparation.lower_turret_end_preparation()
        combined_gcode_upper += preparation.upper_turret_end_preparation()
        # Save the combined G-code to two separate files
        #filename_base = code_number
        filename_upper = code_number + ".txt"
        filename_lower = code_number + "-.txt"

        # Check if files exist and prompt for replacement
        if os.path.exists(filename_upper) or os.path.exists(filename_lower):
            result = messagebox.askyesno("File Exists", f"Files with the name {code_number} already exist. Do you want to replace them?")
            if not result:
                return

        with open(filename_upper, "w") as file:
            file.write(combined_gcode_upper)

        with open(filename_lower, "w") as file:
            file.write(combined_gcode_lower)

        print(f"Upper turret G-code has been saved to {filename_upper}")
        print(f"Lower turret G-code has been saved to {filename_lower}")

    # Generate G-code button
    generate_button = ttk.Button(page2_frame, text="Generate G-code", command=generate_and_save_gcode)
    generate_button.grid(row=2, column=1)
