def ctr_drill_r(tool_number, tool_name, index, properties=""):
    gcode_template = ""

    if tool_name == "CTR DRILL R":
        gcode_template += (f"N{10 + index}G5M41({tool_name})\n"
                           f"G411R1.I{100 + 10 * (index)}.\n"
                           "G50S2000\n"
                           f"G0G40G97G99{tool_number}M3S1500\n"
                           "M20\n"
                           "(APPROACH)\n"
                           "G0X0.Z10.\n"
                           "Z5.\n\n\n\n\n"
                           "G4U0.1\n"
                           "(RETREAT)\n"
                           "G0Z50.\n"
                           "G28U0\n"
                           "M21\n"
                           "M1\n\n"
                           )
    return gcode_template
