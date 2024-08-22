def hex_milling(tool_number, tool_name, index, properties=""):
    gcode_template = ""

    if tool_name == "HEX MILLING":
        # Split the properties string into individual parameters
        params = properties.split(";")

        # Check if the required number of parameters are provided
        if len(params) != 4:
            raise ValueError("HEX MILLING requires 4 parameters: wrench flat, -Y, +Y, Count")

        wrench_flat = params[0].strip()
        y_negative = params[1].strip()
        y_positive = params[2].strip()
        count = params[3].strip()

        gcode_template += f"""M91
G0H0 
G50C0
G340T0505
G0G40G97G99M88S2500
M721 

#503={wrench_flat}(HEX)
#504={y_negative}(START)
#505={y_positive}(END) 
#506=1.0(COUNT)
#507={count}(COUNTEND) 
G0X[#530+2.0]F0.1Z-10.C0 

WHILE[#506LE#507]DO1 
G1Y[-#504]F0.1 
G1X[#503]F0.5
G1Y[#505]F0.1
G0X[#530+2.0]
H60. 
#506=#506+1
END1 
G0X250.M90 
G28U0W0
G28V0
M1 
"""

    return gcode_template