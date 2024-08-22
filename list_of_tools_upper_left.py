from Tools.Upper import HEX_MILLING

def get_tool_name_options():
    return ["HEX MILLING", "ABC"]

def upper_left_gcode(tool_number, tool_name, index, parameters):
    if tool_name == "HEX MILLING":
        gcode_template = HEX_MILLING.hex_milling(tool_number, tool_name, index, parameters)
        return gcode_template
    