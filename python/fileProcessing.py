#myfile = open("fruits.txt")
#print(myfile.read())
#! al usar .read() el cursor va al final del archivo 
#! asi que no se puede usar dos veces seguidas
#content = myfile.read()

#myfile.close()

with open("epico/fruits.txt") as myfile: #? abre el archivo, hace lo de adentro y lo cierra
    content = myfile.read()

#print(content[:90])         # lee los primeros  90 caracteres

with open("epico/vegetables.txt", "w") as myfileV: #? sobreescribe el archivo, se puede usar "r" para leer
    myfileV.write("Broccoli\nEspinaca\nOnion\n")
    myfileV.write("Garlic")                        # \n es como un enter

with open("epico/fruits.txt", "a+") as myfileA: #no se puede leer en el mismo a no ser que pongamos un +
    myfileA.write("\nApple")
    myfileA.seek(0)             #!pone el cursor al principio del archivo de nuevo
    content = myfileA.read()

print(content)