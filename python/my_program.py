#student_grades = [9, "Hello", 7.5, [1, 2, 3.4]]
#student_grades = list(range(1, 11, 2))

student_grades = {"Marry": 9.1, "Lucas": 10.0, "Jhon": 7.5}

mysum = sum(student_grades.values())
length = len(student_grades)
avg = mysum /  length
print(avg)

#suma = student_grades.count(10.0)
#print(suma)

monday_temperatures = [1, 4, 5]
monday_temperatures2 = (1, 4, 5) #listas inmutables

monday_temperatures.append(6)
print(monday_temperatures)
monday_temperatures.remove(4)
print(monday_temperatures)

