#def area(a, b = 5):   #se le puede dar valores default // LOS VALORES DEFAULT NO PUEDEN ESTAR POR DELANTE 
#    return a * b      #DE VALORES NO DEFAULT, es decir, por ej a=4, b  

#print(area(4))
#print(area(4, 5))     #se le puede cambiar el valor default
#print(area(4, 5))
#print(area(a = 4, b = 5))
#print(area(b = 4, a = 5)) #si le damos una keyword la posicion no importa

#def mean(*args):       # *significa que hay una cantidad indefinida de variables (tupla)
#    return sum(args) / len(args)

#def foo(*args):
#    args = [x.upper() for x in args]
#    return sorted(args)                    #ordena alfabeticamente y pone en mayus

def mean(**kwargs):     # *significa que hay una cantidad indefinida de variables con keywords {diccionario}
    return kwargs

print(mean(a=1,b=2,c=3))