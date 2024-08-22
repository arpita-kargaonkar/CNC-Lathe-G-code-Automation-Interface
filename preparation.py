def lower_turret_start_preparation(code_number, code_name, nagasa, tukidasi, zairyou):
    gcode = f"""
{code_number}({code_name}) 
#510={nagasa}(L-NAGASA)
#520={tukidasi}(TUKIDASI) 
#530={zairyou}(ZAIRYOU)

G354Z[-466.0+#510]A54. 
G354Z[440.6-#520]A55.
M1 

G28U0W0
G28B0
G333 

G411F12. 

N100G54M41(BAR CHANGE) 
G411B1.I102. 

M100(W)
G28U0
G0G40G97G99T1212M5 
G53Z-395.0 
G0U-100. 
M904 
G4U0.5 
/M11 
/G4U1. 
/M61 
G4U0.5 
/M11 
G4U0.5 
G28U0
G53Z-380.0 
G367T0909A1.F5000. 
G4U1.0 

G56
G0T0101
G0Z2.0 
X0 
/M61 
G4U0.5 
M10
G4U1.0 
G0W10. 
X160.0Z65.0(X160.0 Z10.) 
G28U0M5
M1 

N101G56M41(TOP CUT)
G0G40G97G99T0505 
Z-1. 
X[#530+1.0]S1800M3 
G1X1.5F0.1 
X-1.0F0.05 
G0X50.0
X160.0Z105.0 
G28U0M5
M101(W)
M1 

N102G54M41(BAR STOP) 
G411D1.I1. 
G28U0M05 
G0G40G97G98T0101 
X50.Z50.0
Z10.0
G1G98Z1.5F1000 

/M11 
G4U1.0 

/M61 
M10
G4U1.0 
G0Z99.0
M705(BAR FIN)
M1 

N1M41(START) 
M102(W)
M1 

"""

    return gcode


# gcode_generator.py
def lower_turret_end_preparation():
    gcode_end= """G53X-16.Z-380.M5 
G367T900A1.F5000.(F15000)
M903 
G4U1.
 
(G0X50.) 
G28U0
M5 
 
 
 
M797 
(W)
N200(1 CYCLE STOP) 
G411C1.I500. 
M103(W)
M1 
 
 
 
N300M441(PARTS CATCHER G)
G411U1.I1000.
M104(W)
G55
G1998S2. 
G28U0
G53Z0
M55
M368B-95.
M735(CONFIRMING COMPLETION OF PC-G)
M69
M1 
 
 
 
N1000G54M41(CUT OFF) 
G411T1.I400. 
M105(W)
M902 
M106(W)
 
M405(CUT OFF)
M107(W)
G28W0
M1 
M69
G411C1.I500. 
 
 
N400M427(RESTART)
G28U0
G28W0
T0100
M191 
M30
 
N500M427(1 CYCLE STOP) 
G28U0
G28W0
M192 
M2 
 
%
"""
    return gcode_end

def upper_turret_start_preparation(code_number, code_name, nagasa, tukidasi, zairyou):
    gcode=f"""{code_number}({code_name}) 
#510={nagasa}(L-NAGASA)
#520={tukidasi}(TUKIDASI) 
#530={zairyou}(ZAIRYOU)

G28U0V0W0
G28B0
G333 
 
G411F12. 
 
N100M41(BAR CHANGE)
G411B1.I102. 
M100(W)
M101(W)
M1 
 
N102M41(BAR STOP)
G411D1.I1. 
M1 
 
N1M41(STRAT) 
M102(W)
M1
"""
    return gcode

def upper_turret_end_preparation():
    gcode_end="""(W)
N200(1 CYCLE STOP) 
G411C1.I500. 
M103(W)
M1 
 
 
N300M428(UN LOADING) 
G411U1.I1000.
M104(W)
G28U0V0
G28W0
M1 
 
N1000G54M41(CUTOFF)
G411T1.I400. 
M105(W)
G28U0V0
G28W0
M106(W)
M107(W)
G28W0M5
M1 
G411C1.I500. 
 
N400M428(RESTART)
G28U0V0
G28W0
M191 
M30
 
N500M428(1 CYCLE STOP) 
G28U0V0
G28W0
M192 
M2 
 
%


"""
    return gcode_end

