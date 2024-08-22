def drill_r(tool_number, tool_name, index, properties=""):
    gcode_template = ""

    if tool_name == "DRILL R":
        gcode_template += (f"N{10 + index}G55M441({properties}D/L)\n"
                           f"G411L1.I{100 + 10 * (index)}.\n"
                           f"G0G40G97G99{tool_number}M3S1300\n"
                           "M20\n"
                           "(APPROACH)\n"
                           "G0X0.Z-10.\n"
                           "Z-5.\n\n\n\n\n"
                           "G4U0.1\n"
                           "(RETREAT)\n"
                           "G0Z-50.\n"
                           "G28U0\n"
                           "M21\n"
                           "M1\n\n"
                           )
    return gcode_template
