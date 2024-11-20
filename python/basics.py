def mean(value):
    if type(value) == dict:
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) / len(value)
    return the_mean

print(mean([1,4,7]))

student_grades = {"Marry":9.1, "Juan":8.8, "Lucas":10.0}
print(mean(student_grades))

#def mean(value):
#    if isinstance(value, dict):   #!ES LO MISMO QUE LO DE ARRIBA, DE HECHO SE PREFIERE
#        the_mean = sum(value.values()) / len(value)
#    else:
#        the_mean = sum(value) / len(value)
#    return the_mean

x=3
y=1
if x > y:
    print("x is greater than y")
elif x==y:
    print("x is equal to y")
else:
    print("x is less to y")