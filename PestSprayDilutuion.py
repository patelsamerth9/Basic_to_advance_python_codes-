def calculate_dilution(concentrate_ml, ratio_water):
    water_ml = concentrate_ml * ratio_water
    return water_ml

print(calculate_dilution(250, 10))