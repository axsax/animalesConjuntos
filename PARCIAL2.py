def errores(codigo,texto):
    if codigo==1:
        return print("Por favor digite un número.")

def whileEnteroValidarDef(a,b,es): # permite evaluar si es entero o no
    while a and b:
        numero = input()
        try:
            if (es=="categoria"):
                if validarCategoria(int(numero)):
                    return numero
            elif (es=="opcion"):
                if validarOpcion(int(numero)):
                    return numero
        except ValueError:
            errores(1,"")

def validarCategoria(entero):
    if (entero > 0 and entero <=12):
       return  True
    else:
        print("Digite un número dentro de la categoria")
        return False

def validarOpcion(entero):
    if (entero > 0 and entero <=2):
       return  True
    else:
        print("Digite un número dentro de las opciones disponibles")
        return False

def opcion1(conjuntoA, conjuntoB, conjuntoC):
    return (conjuntoA.intersection(conjuntoB).difference(conjuntoC)) #Animales que son [Categoría A] y [Categoría B] pero no son [Categoría C].

def opcion2(conjuntoA, conjuntoB, conjuntoC):
    return  (conjuntoA.union(conjuntoC).intersection(conjuntoB)) #Animales que resultan de la intersección entre [Categoría B] y la unión de [Categoría A] y [Categoría C].

#se listan las categorias con el  fin de dar a conocer al usuario  sus posibilidades, es importannte ya que tiene claves unicas tales como 1 2 etc que permite darme a entender que escogio el usuario
animales= {1:'Acuaticos',	2:'Terrestres',	3:'Voladores',	4:'Carnivoros',	5:'Omnivoros',	6:'Herviboros',	7:'Carroñeros',	8:'Aves',	9:'Mamiferos',	10:'Peces',	11:'Vertebrados',	12:'Invertebrados'}

# hago el listado de cada categoria en cada variable
acuatico = {'pulpo', 'tiburon', 'ballena', 'estrella_de_mar', 'trucha', 'medusa', 'mojarra', 'manati', 'pez_globo'}
terrestre = {'avestruz', 'boa', 'leon', 'sapo', 'cocodrilo', 'oso', 'cabra', 'venado', 'armadillo', 'mono', 'alacran'}
volador = {'tucan', 'gaviota', 'garza', 'cisne', 'pato', 'aguila', 'flamenco', 'guacamaya', 'canario', 'buitre'}
carnivoros = {'pulpo', 'tiburon', 'boa', 'gaviota', 'leon', 'sapo', 'garza', 'cocodrilo', 'estrella_de_mar', 'trucha', 'aguila', 'medusa', 'mojarra', 'alacran', 'buitre'}
omnivoros = {'avestruz', 'pulpo', 'tucan', 'ballena', 'cisne', 'oso', 'pato', 'flamenco', 'armadillo', 'guacamaya', 'mono', 'canario', 'pez_globo'}
herviboros = {'cabra', 'venado', 'manati'}
carroñeros = {'tiburon', 'gaviota', 'cocodrilo', 'aguila', 'buitre'}
aves = {'avestruz', 'gaviota', 'garza', 'cisne', 'pato', 'aguila', 'flamenco', 'guacamaya', 'canario', 'buitre'}
mamiferos = {'leon', 'ballena', 'estrella_de_mar', 'oso', 'cabra', 'venado', 'armadillo', 'manati', 'mono'}
peces = {'trucha', 'mojarra', 'pez_globo'}
vertebrados = {'avestruz', 'tiburon', 'gaviota', 'leon', 'sapo', 'garza', 'ballena', 'cocodrilo', 'cisne', 'oso', 'pato', 'trucha', 'cabra', 'aguila', 'venado', 'flamenco', 'mojarra', 'armadillo', 'guacamaya', 'manati', 'mono', 'canario', 'pez_globo', 'buitre'}
invertebrados = {'pulpo', 'boa', 'estrella_de_mar', 'medusa', 'alacran'}

# a cada llave osea 1 o 2 o 3 etc, le asigno acada varaible como acuativo, terrestre etc, en el mismo roden en que estan en la variable animales, para que las posiciones sean iguales
lista ={1:acuatico,2:terrestre,3:volador,4:carnivoros,5:omnivoros,6:herviboros,7:carroñeros,8:aves,9:mamiferos,10:peces,11:vertebrados,12:invertebrados}
# ES MAS FACIL DEFINIR VARIABLE True , pero hay que aplicar el and
#para while
a=1
b=1
#para while de entradas de inputs
while a and b:
    # comunicacion con usuario
    print("Escoja tres categorias sabiendo que las opciónes son:")
    print("Opción 1: Animales que son [Categoría 1] y [Categoría 2] pero no son [Categoría 3].")
    print(
        "Opción 2: Animales que resultan de la intersección entre [Categoría 2] y la unión de [Categoría 1] y [Categoría 3]. \n")

    # imprimo la variable animales con su llave siendo este el numero de cada categoria
    for val in animales:
        print("CATEGORIA " + str(val) + ": " + animales[val])
    print("\n")
    # el usuario escoge
    print("Digite la opción para la Categoria 1: \n")
    uno = whileEnteroValidarDef(a,b,"categoria")
    print("Digite la opción para la Categoria 2:\n")
    dos=whileEnteroValidarDef(a,b,"categoria")
    print("Digite la opción para la Categoria 3: \n")
    tres=whileEnteroValidarDef(a,b,"categoria")

    # da a conocer las categorias escogidas al usuario
    print("Las categorias escogidas fueron: " + animales[int(uno)] + ", " + animales[int(dos)] + " y " + animales[
        int(tres)])

    # permite esocger la opcion
    print("Escoja la opción que desee:\n")
    print("Opción 1: Animales que son " + animales[int(uno)] + " y " + animales[int(dos)] + " pero no son " + animales[
        int(tres)] + ".")
    print(
        "Opción 2: Animales que resultan de la intersección entre " + animales[int(dos)] + " y la unión de " + animales[
            int(uno)] + " y " + animales[int(tres)] + ".")

    # guarda la opcion del usuario
    print("Digite su opción:")
    opcion = whileEnteroValidarDef(a,b,"opcion")

    # dependiendo de la opcion se dirige a la funcion que se creo al comienzo, utilizando las variables de las categorias para acceder como llaves en la lista
    print("El resultado es: ")
    if int(opcion) == 1:
        salida = opcion1(lista[int(uno)], lista[int(dos)], lista[int(tres)])
    else:
        salida = opcion2(lista[int(uno)], lista[int(dos)], lista[int(tres)])

    if salida:
        print(salida)
    else:
        print("No existe ningun animal que cumpla con los requerimientos.")

    print("¿Desea escoger otras categorias, digíte cualquier cosa para continuar, Enter para finalizar?")
    continuar = input()
    if continuar == "":
        b=0
