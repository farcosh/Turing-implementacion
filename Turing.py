import sys

#Hacemos esto por si una recursión es mayor a 999 el programa no truene
sys.setrecursionlimit(10000)

# Funcion para crear la cinta
# Crearemos una lista de longitud 1000, funcionara como la cinta
# la cual llenaremos de 0's.
def crea_cinta():
    l = []    #Creamos la lista que simulara la cinta

    #for-Para llenar la lista de 0's
    for i in range(0, 1000):
        l.append(0)

    return l    #Regresamos la cinta

#Funcion para contar el numero de unos que tiene la cinta
#Recorreremos la cinta buscando los unos que tiene verificando
#que sean la cantidad deseada.
#var "cinta"= La cinta a evaluar
#var "unos"= La cantidad de unos que deberia tener la cinta
def contar(
        cinta, unos):
    i = 0  #Contador de unos

    #Recorremos la cinta
    for x in range(0, len(cinta) - 1):
        if cinta[x] == 1:
        #Si en la posicion x hay un 1 entonces aumentamos
        #el contador i en uno.
            i += 1

    if i == unos:
        #Si el numero de unos que se encontro en la cinta es igual
        #a los esperados indicamos que el programa termino bien y
        #el resultado es correcto
        print("AC Felicidades, que bien la pases, vamos a bailar...")
    else:
        #En caso de que el programa termine pero no sea
        #el numero de unos esperados indicamos que hubo un error
        print("Error WA")

#Funcion recursiva que lee la cinta en una de las
#evaluaciones deseadas, regresa el resultado de la evaluacion
#var "estado"= El estado actual de la maquina
#var "lugar"= Lugar actual de la maquina
#var "dic"= Diccionario que contine las reglas de la maquina
#var "cinta"= Cinta en la que actualmente nos movemos
#var "contador"= Contador del numero de veces
#                 que se a llamado a la funcion.
#var "unos"= La cantidad de unos que deberia de tener la cinta al final
def leer(
        estado, lugar, dic,
        cinta, contador, unos):

    #Clausula de escape
    if (lugar < 0
            or lugar >= 1000):
        #Si en algun momento el lugar se sale de la cinta
        #Regresamos el error "MLE"
        print("Error MLE")
        return

    #Clausula de escape
    if contador > 10000:
        #Si el numero de iteraciones supera
        #10000 enviamos el error "TLE".
        print("Error TLE por gato =('w')=")
        return

    contador += 1    #Aumentamos en 1 el contador
    valor = cinta[lugar]    #El valor en el lugar actual de la cinta
    llave = str(estado) + str(valor)   #Llave para el diccionario

    #Clausula de escape
    if not llave in dic:
        #Si la llave no se encuntra en el diccionario
        #procedemos a verificar si la cantidad de unos es correcta.
        contar(cinta, unos)
        return

    rules = dic[llave] #Obtenemos las reglas de la cinta
    cinta[lugar] = int(rules[1]) #Actualizamos el valor
    estado = rules[0] #Actualizamos el estado

    #Verificaremos hacia que direccion se movera lugar
    if rules[2] == "R":
        #Movemos a la derecha el lugar
        lugar += 1
    else:
        #Movemos a la izquierda el lugar
        lugar -= 1

    #Hacemos la llamada recursivo de la funcion
    leer(estado, lugar, dic,
         cinta, contador, unos)

#Funcion que ya teniendo las reglas y evalucaciones
#procede a emular la maquina de Turing
#var "dic"= Diccionario que contiene las reglas
#var "list"= Lista que contiene las evaluaciones
def turing(
        dic, list):

    cinta = crea_cinta() #Abusando de la ambigüedad "Creamos la cinta" XD

    #Obtenemos las evaluaciónes y las emulamos
    for a in range(0, int(len(list) / 2)):
        unos = list.pop(0) #Obtenemos el numero de 1's para la cinta
        resultado = list.pop(0) #Obtenemos el resultado deseado

        #Actualizamos la cinta con la cantidad de unos dada
        for x in range(0, int(unos)):
            cinta[x] = 1

        #Llamamos al metodo recursivo leer que emulara la maquina
        leer(0, 0, dic,
             cinta, 0, int(resultado))


#Le solitamos al usuario la cantidad de reglas y evaluaciones a recibir
n = input("Cual es N?(numero de reglas)\n")
m = input("Cual es M?(numero de evaluaciones)\n")

reglas = {} #Creamos el diccionario donde guardaremos las reglas
evaluaciones = [] #Creamos la lista donde guardaremos las evaluaciones

#El usuario ingresa las reglas y procedemos a guardarlas
#ya sabemos la cantidad de reglas asi que usaremos un for para
#para preguntar esa cantidad de veces
print("Ingresa las reglas separadas con espacio")
for a in range(0, int(n)):
    #Solicitamos la entrada
    instruccion = input("Regla numero " + str(a + 1) + ": ")
    ins = instruccion.split(" ") #Preparamos la entrada para se guardada
    #Guardamos las reglas en el diccionario
    reglas[ins[0] + ins[1]] = ins[2:5]

#Analogo a lo anterior el usuario ingresara las evaluaciones
#en esta ocasion las guardaremos una lista
print("Ingresa las evaluaciones separadas con espacio")
for b in range(0, int(m)):
    #Solicitamos la entrada
    evaluacion = input("evaluacion numero " + str(b + 1) + ": ")
    e = evaluacion.split(" ") #Preparamos la entrada para se guardada
    #Guardamos las evaluaciones en la lista
    evaluaciones.append(e[0])
    evaluaciones.append(e[1])

#It's a kind of magic ( ^-^)
#https://youtu.be/cIZFq3VDeUY
turing(reglas, evaluaciones)
	
