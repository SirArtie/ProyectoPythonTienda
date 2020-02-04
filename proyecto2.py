import getpass
nombresArticulos = ('Playera color rosa','Sueter azul','Chamarra de cuero','Pantalon de Mezquilla','Tenis para correr grises','Short de playa naranja','Calcetines de cuadros rojos','Sandalias blancas')
inventario = {}
informacionArticulos = [[10,'Nike',150],[5,'Bolo',300],[3,'Cuerox',1200],[6,'Vans',200],[4,'Adidas'1200],[2,'Martí',250],[12,'Donelli',150],[1,'Havaianas', 400]]
numeroArticulos = 8
def doInventary():
    i = 0
    for i in range(len(nombresArticulos)):
        inventario[i+1] =[nombresArticulos[i],informacionArticulos[i]]

def mostrarInventario():
    for key in inventario:
        print('Articulo: '+inventario[key][0])
        print('Numero de articulos disponibles: ',inventario[key][1][0])
        print('El fabricante del articulo es: '+inventario[key][1][1])
        print('Costo: ',inventario[key][1][2])

def listarInventario():
    for key in inventario:
        print('Articulo numero: ',key)
        print('Nombre del articulo: '+inventario[key][0])
        print("")

def comprar(nkey):
    print('Has elegido el articulo: '+inventario[nkey][0])
    if inventario[nkey][1][0] > 0:
        inventario[nkey][1][0] = inventario[nkey][1][0] - 1
        print('Tu compra se ha realizado exitosamente')
    else:
        print('Lo sentimos estimado cliente, el articulo seleccionado esta fuera de stock :c')
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


articulo2 = (2,300,'Nike')
articulo3 = (3,'Chamarra de cuero',800,'CuerosPros')
doInventary()
b=False
while(b==False):#Se abren las opciones del menú
    print("\t---Bienvenido a la tienda---")
    #Menú que aparece en pantalla
    print("\n-1- Registrar")
    print("-2- Ingresar")
    print("-3- Salir")
    
    #print(inventario)
    """print(inventario['Playera color rosa'])
    print('Numero de articulos disponibles: ',inventario['Playera color rosa'][0])"""
    #mostrarInventario()
    #listarInventario()
    #comprar(8)
    #comprar(8)
    
    x=int(input("\nSeleccione una opción del menú: "))#variable que recibe el valor del menú.

    if x==1:#Si "x" es igual a 1, entra en la opción 1 del menú.
        print("\t --REGISTRO--")
        nickname=input("Ingrese el nombre de usuario: ")
        contraseña=getpass.getpass("Ingrese la contraseña: ")#posición 0 de la lista
        lista.append(contraseña)#Añadiendo la contraseña a la lista
        usuarios[nickname]=lista#Añade la lista en el valor del diccionario.

        print("\nVALIDANDO DATOS")
        a=False

        while(a==False):#Se muestran las opciones del usuario y contraseña
            check_nickname=input("\n Ingrese nuevamente el usuario: ")
            check_contraseña=input("Ingrese la contraseña: ")
            if check_nickname in usuarios:#checa si el nombre ingresado por 2da vez, se encuentra en el diccionario.
                if usuarios[nickname][0]==check_contraseña:#checa si la contraseña ingresa se encuentra en la lista, posición 0 que está en el diccionario.
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
                    a=True

                else:
                    print("Contraseña incorrecta")
            else:
                print("Nombre de usuario incorrecto")


    elif x==2:
        print("\n --INGRESAR--")
        nickname=input("Ingrese el nombre de usuario:")
        contraseña=input("Ingrese la contraseña: ")#posición 0 de la lista
        lista.append(contraseña)#Añadiendo la contraseña a la lista
        usuarios[nickname]=lista#Añade la lista en el valor del diccionario.

        print("\nVALIDANDO DATOS")

        check_nickname=input("\n Ingrese nuevamente el usuario: ")
        check_contraseña=input("Ingrese la contraseña: ")

        if check_nickname in usuarios:
            if usuarios[nickname][0]==check_contraseña:
                print("Bienvenido "+nickname)
                subOpcion2 = 0
                while subOpcion2!=4:
                    subOpcion2 = menuR('Selecciona una opcion:\n1)Ver los Articulo\n2)Ver informacion completa de todos los articulos\n3)Comprar Articulo\n4)Cerrar Sesion',4)
                    if subOpcion2 == 1:
                        listarInventario()
                    if subOpcion2 == 2:
                        mostrarInventario()
                    if subOpcion2 == 3:
                        print('Selecciona alguno del numero de los siguientes articulos')
                        listarInventario()
                        comprar(menuR('',numeroArticulos))
            else:
                print("Contraseña Invalida")
        else:
            print("Usuario no registrado")


    elif x==3:
        print("Hasta luego, esperamos que vuelva pronto")
        b=True
   
    else:# Esta opción se mostrará si el usuario ingresa otra opción que no se encuentre
        print("Opción inválida, por favor selecciona una opción correcta")
