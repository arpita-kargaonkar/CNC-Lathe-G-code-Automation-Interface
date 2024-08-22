from Tools.Lower_left import CTR_DRILL, BIT_ARA_1_5, BIT_ARA_3_0, DRILL, NAKAGURI



def get_tool_name_options():
    return ["CTR DRILL", "DRILL", "3.0 BIT ARA", "1.5 BIT ARA", "NAKAGURI", "NEJI", "ER NEJI"]

neji_options = ["M24x1", "M22x1", "G1/2", "G3/8", "W22-20"]
er_neji_options = ["M24x1", "M22x1", "G1/2", "G3/8", "W22-20"]

def lower_left_gcode(tool_number, tool_name, index, parameters):
    if tool_name == "CTR DRILL":
        gcode_template = CTR_DRILL.ctr_drill(tool_number, tool_name, index, parameters)
        return gcode_template
    elif tool_name == "1.5 BIT ARA":
        gcode_template = BIT_ARA_1_5.bit_ara_15(tool_number, tool_name, index, parameters)
        return gcode_template
    elif tool_name == "3.0 BIT ARA":
        gcode_template = BIT_ARA_3_0.bit_ara_3(tool_number, tool_name, index, parameters)
        return gcode_template
    elif tool_name == "DRILL":
        gcode_template = DRILL.drill(tool_number, tool_name, index, parameters)
        return gcode_template
    elif tool_name == "NAKAGURI":
        gcode_template = NAKAGURI.nakaguri(tool_number, tool_name, index, parameters)
        return gcode_template
    
    wait = f"""N{100 + 10 * (index)}\n
           M{100 + 10 * (index)}(W)\n\n"""
    gcode_template += wait
    return gcode_template 
    