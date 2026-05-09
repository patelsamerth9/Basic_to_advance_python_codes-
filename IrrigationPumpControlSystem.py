def check_irrigation(moisture_percent):
    if moisture_percent < 30:
        return "Turn on water pump"
    elif moisture_percent > 70:
        return "Soil is too wet, stop watering"
    else:
        return "Moisture is optimal"
print(check_irrigation(25))