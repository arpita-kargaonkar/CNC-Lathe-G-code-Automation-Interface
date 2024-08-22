def bit_ara_3(tool_number, tool_name, index, properties=""):
    gcode_template = ""

    if tool_name == "3.0 BIT ARA":
        gcode_template += (f"N{10 + index}G54M41({tool_name})\n"
                           f"G411L1.I{100 + 10 * (index)}.\n"
                           f"G0G40G97G99{tool_number}M3S1800\n\n"
                           "G0X[#530+2.0]Z50.\n"
                           "G0Z1.0\n"
                           "(APPROACH)\n"
                           "G1Z0.0F0.1\n\n\n\n\n"
                           "(RETREAT)\n"
                           "G0X[#530+2.0]\n"
                           "G0X50.\n"
                           "G0Z50.\n\n"
                           "G28U0\n"
                           "M1\n\n"
                           )
    return gcode_template
