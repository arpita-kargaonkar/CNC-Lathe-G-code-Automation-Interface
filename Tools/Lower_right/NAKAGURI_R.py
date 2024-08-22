def nakaguri_r(tool_number, tool_name, index, properties=""):
    gcode_template = ""

    if tool_name == "NAKAGURI R":
        gcode_template += (f"N{10 + index}G55M41({tool_name})\n"
                           f"G411R1.I{100 + 10 * (index)}.\n"
                           f"G0G40G97G99{tool_number}M3S2000\n"
                           "G0X[#530+2.0]Z-50.\n"
                           "G0Z-1.0\n"
                           "(APPROACH)\n\n\n\n"
                           "(RETREAT)\n"
                           "G0Z-10.\n"
                           "G0X50.\n"
                           "G0Z-50.\n\n"
                           "G28U0\n"
                           "M1\n\n"
                           )
    return gcode_template
