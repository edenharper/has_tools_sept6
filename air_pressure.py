import math

def air_pressure_at_height(h):
    p0 = 101325      # reference pressure in pascals
    M  = 0.02896968  # molar mass of air in kg/mol
    g  = 9.80665     # gravity in m/s^2
    R0 = 8.314462618 # Gas constant J/(mol*K)
    T  = 273         # temp in kelvin

    ratio = -(g*h*M)/(R0*T)
    p_h = p0*math.exp(ratio)
    return p_h


# list of elevations to run
h_list = range(0,1000,100)
for height in h_list:
    p_h = air_pressure_at_height(height)
     print(height,'   ', p_h)