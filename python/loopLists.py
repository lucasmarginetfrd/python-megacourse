monday_temperatures = [9.1, 8.8, 7.6, 5.5, 6.5, 4.2]

#print(round(monday_temperatures[0]))
#print(round(monday_temperatures[1]))
#print(round(monday_temperatures[2]))

for temperature in monday_temperatures:
    rounded_temperature = round(temperature)
    print(round(temperature))
    if rounded_temperature > 6:
        print("aprobado")
    else:
        print("desaprobado")

#for letter in "hello":
#    print(letter.title())
