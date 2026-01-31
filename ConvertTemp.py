def convertTemperature(celsius):
    F = (celsius * 1.80) + 32.00
    K = celsius + 273.15
    Temps = [K,F]

    return Temps

Temps = convertTemperature(100)

for i in Temps:
    print(i)