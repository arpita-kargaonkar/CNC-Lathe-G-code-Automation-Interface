from Tools.Lower_right import CTR_DRILL_R, BIT_ARA_1_5_R, BIT_ARA_3_0_R, DRILL_R, NAKAGURI_R

def get_tool_name_options():
    return ["CTR DRILL R", "DRILL R", "3.0 BIT ARA R", "1.5 BIT ARA", "NAKAGURI R", "NEJI R", "ER NEJI R"]

neji_options = ["M24x1", "M22x1", "G1/2", "G3/8", "W22-20"]
er_neji_options = ["M24x1", "M22x1", "G1/2", "G3/8", "W22-20"]

def lower_right_gcode(tool_number, tool_name, index, parameters):
    if tool_name == "CTR DRILL_R":
        gcode_template = CTR_DRILL_R.ctr_drill_r(tool_number, tool_name, index, parameters)
        return gcode_template
    if tool_name == "1.5 BIT ARA":
        gcode_template = BIT_ARA_1_5_R.bit_ara_15_r(tool_number, tool_name, index, parameters)
        return gcode_template
    if tool_name == "3.0 BIT ARA":
        gcode_template = BIT_ARA_3_0_R.bit_ara_3_r(tool_number, tool_name, index, parameters)
        return gcode_template
    if tool_name == "DRILL":
        gcode_template = DRILL_R.drill_r(tool_number, tool_name, index, parameters)
        return gcode_template
    if tool_name == "NAKAGURI":
        gcode_template = NAKAGURI_R.nakaguri_r(tool_number, tool_name, index, parameters)
        return gcode_template
    