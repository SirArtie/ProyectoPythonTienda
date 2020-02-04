import getpass
"""Normalmente para evitar problemas podemos hacer un inventario que puede ser un diccionario y cada uno de los productos tendria un
id diferente, lo cual esta bien, y ademas agregarle la lista de toda su informacion, desde su nombre hasta su talla, estas inicializaciones, son con el fin, de
solo tener que hacer pequeñas modificaciones al codigo como agregar mas para no tener que modificarlo"""
nombresArticulos = ('Playera color rosa','Sueter azul','Chamarra de cuero','Pantalon de Mezquilla','Pantalon Negro','Sueter blanco','Gorro','Ropa interior')
inventario = {}
informacionArticulos = [[10,'Nike',150,'M'],[5,'Bolo',300,'G'],[3,'Cuerox',1200,'G'],[6,'Vans',200,'C'],[4,'Old Navy',500,'M'],[2,'Zara',1000,'M'],[12,'Dockeres',670,'C'],[1,'CK',230,'C']]
#Una constante para poder controlar/modificar cuando sea conveniente
numeroArticulos = 8
#Esta funcion arma el diccionario inventario con los datos previos
def doInventary():
    i = 0
    for i in range(len(nombresArticulos)):
        inventario[i+1] =[nombresArticulos[i],informacionArticulos[i]]
#Funcion que muestra la informacion de todos los articulos
def mostrarInventario():
    for key in inventario:
        print('Articulo: '+inventario[key][0])
        print('Numero de articulos disponibles: ',inventario[key][1][0])
        print('El fabricante del articulo es: '+inventario[key][1][1])
        print('Costo: ',inventario[key][1][2])
        print('Talla: ',inventario[key][1][3])
#Esta funcion muestra solo los nombres de los articulos
def listarInventario():
    for key in inventario:
        print('Articulo numero: ',key)
        print('Nombre del articulo: '+inventario[key][0])
        print("")
#Esta implementa la funcionalidad de las compras
def comprar(nkey):

	if nkey<=numeroArticulos:

		print('Has elegido el articulo: '+inventario[nkey][0])
		if inventario[nkey][1][0] > 0:
			#print("Ingresa tu correo paypal(El mismo que registraste)")
			inventario[nkey][1][0] = inventario[nkey][1][0] - 1
			print('Tu compra se ha realizado exitosamente')
		else:
			print('Lo sentimos estimado cliente, el articulo seleccionado esta fuera de stock :c')
#Funcion para no tener que colocar prints.
def menuR(cadena,nOpciones):
    print(cadena)
    n = int(input('Opcion: '))
    while n>nOpciones or n<1:
        print('Esa opcion no es valida')
        print(cadena)
        n = int(input('Opcion: '))
    return n





usuarios={}
informacion={}
lista_informacion=[]
lista=[]
doInventary()
b=False
while(b==False):
    print("\t---Bienvenido a la tienda---")
    #Menú que aparece en pantalla
    print("\n-1- Registrar")
    print("-2- Ingresar")
    print("-3- Salir")
    x=int(input("\nSeleccione una opción del menú: "))#variable que recibe el valor del menú.
    if x==1:#Si "x" es igual a 1, entra en la opción 1 del menú.
        print("\t --REGISTRO--")
        nickname=input("Ingrese el nombre de usuario: ")
        contraseña=getpass.getpass("Ingrese la contraseña: ")#posición 0 de la lista
        lista.append(contraseña)#Añadiendo la contraseña a la lista
        usuarios[nickname]=lista#Añade la lista en el valor del diccionario.

        print("\nVALIDANDO DATOS")

        check_nickname=input("\n Ingrese nuevamente el usuario: ")
        check_nickname2=check_nickname.isalnum() #Validando datos alfanumericos
        check_contraseña=input("Ingrese la contraseña: ")
        check_contraseña2=check_contraseña.isalnum() #validando datos alfanumericos.
        if len(check_nickname) >= 6 and len(check_nickname) <=12: #Verificando el número de carácteres en el nombre de usuario.
            if check_nickname in usuarios and check_nickname2 == True:#checa si el nombre ingresado por 2da vez, se encuentra en el diccionario.
                if usuarios[nickname][0]==check_contraseña and check_contraseña2 == True:#checa si la contraseña ingresa se encuentra en la lista, posición 0 que está en el diccionario.
                    print("Los datos son correctos, por favor de ingresar lo que se pide")
                    nombre=input("\nNombre:")#llave del diccionario
                    apellido=input("Apellido: ")#0
                    edad=int(input("Edad: "))#1
                    correo=input("Correo: ")#2
                    tarjeta=int(input("No. Tarjeta: "))#3
                    paypal=input("PayPal: ")#4
                    contra_pay=input("Contraseña de PayPal: ")#5
                    #Guardando datos personales en la lista
                    lista_informacion.append(apellido)
                    lista_informacion.append(edad)
                    lista_informacion.append(correo)
                    lista_informacion.append(tarjeta)
                    lista_informacion.append(paypal)
                    lista_informacion.append(contra_pay)
                    #Asignando la lista en la llave del diccionario.
                    informacion[nombre]=lista


                else:
                    print("Contraseña incorrecta")
            else:
                print("Nombre de usuario incorrecto")
        else:
            print("El nombre de usuario debe contener un mínimo de 6 carácteres y un máximo de 12")


    elif x==2:
        print("\n --INGRESAR--")
        nickname=input("Ingrese el nombre de usuario:")
        contraseña=input("Ingrese la contraseña: ")#posición 0 de la lista
        lista.append(contraseña)#Añadiendo la contraseña a la lista
        usuarios[nickname]=lista#Añade la lista en el valor del diccionario.

        print("\nVALIDANDO DATOS")

        check_nickname=input("\n Ingrese nuevamente el usuario: ")
        check_nickname2=check_nickname.isalnum()
        check_contraseña=input("Ingrese la contraseña: ")
        check_contraseña2=check_contraseña.isalnum()

        if len(check_nickname) >= 6 and len(check_nickname) <=12:
            if check_nickname in usuarios and check_nickname2 == True:
                if usuarios[nickname][0]==check_contraseña and check_contraseña2==True:
                    print("Bienvenido "+nickname)
                    subOpcion2 = 0
                    while subOpcion2!=4:
                        subOpcion2 = menuR('Selecciona una opcion:\n1)Ver los Articulo\n2)Ver informacion completa de todos los articulos\n3)Comprar Articulo\n4)Cerrar Sesion',4)
                        if subOpcion2 == 1:
                            listarInventario()
                        if subOpcion2 == 2:
                            mostrarInventario()
                        if subOpcion2 == 3:
                            print('Selecciona alguno del numero de los siguientes articulos, si al final no deseas ninguno solo ingresa un numero mayor al del ultimo articulo')
                            listarInventario()
                            comprar(menuR('',numeroArticulos+1))
                else:
                    print("Contraseña Invalida")
            else:
                print("Usuario no registrado")
        else:
            print("El nombre de usuario debe contener un mínimo de 6 carácteres y un máximo de 12")


    elif x==3:
        print("Hasta luego, esperamos que vuelva pronto")
        b=True
else: # Esta opción se mostrará si el usuario ingresa otra opción que no se encuentra
    print("Opción inválida, por favor ingresa una opción que esté en el menú")
