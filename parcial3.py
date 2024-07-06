#Reservas de Clases de Baile
import os
import csv
os.system("cls")

reservas = []
data = {
  'clases': ["Clase de Salsa - Academia Ritmo", "Clase de Bachata - Academia Ritmo", "Clase de Tango - Academia Pasión", "Clase de Hip Hop - Academia Movimiento", "Clase de Ballet - Academia Clásica"],
   'valor': [20000, 18000, 16000, 14000, 12000],
   'horas':  ['08:00 A.M', '09:00 A.M','10:00 A.M','11:00 A.M', '12:00 P.M']
  }

def reservaCSV():
  with open('reserva_inicial.csv', 'r') as archivo_csv:
    lector_csv = csv.reader(archivo_csv)
    for fila in lector_csv:
      nombre = fila [0]
      contacto = fila [0]
      clase = fila [0]
      hora = fila [0]
      fecha = fila [0]
      total = fila [0]

      reserva = {
      'nombre': nombre,
      'contacto': contacto,
      'clase': clase,
      'hora': hora,
      'fecha': fecha,
      'total': contacto
      }
      reservas.append(reserva)
    print("El archivo ha sido creado exitosamente")

def validarString():
    while True:
        cadena = input()
        if cadena.strip():
            break
        else: 
            print("El campo no debe estar vacío")
    return cadena

def validarNumero():
  while True:
    try:
      number = int(input())
    except ValueError:
      print("El numero ingresado no es valido")
    else:
      break
    return number

def disponibilidad(clases=None,fecha=None):
    if clases == None and fecha == None:    
        #Seleccionar una clases de una lista
        while True:
            print("Seleccionar Sala")
            i =1
            for clases in data['clases']:
                print(f"{i} - {clases}")
                i = i+1
            op = validarNumero()
            if (op > 0 and op < 6):
                clases = data['salas'][op-1]
                print("Se ha seleccionado la clases ", clases)
                break
            else:
                print("La opción debe ser entre 1 y 5")

        #Seleccionar fecha
        print("Seleccione la fecha")
        fecha = validarString()
        print("Se ha ingresado la fecha: ",fecha)

    horas_reservadas =[]
    reservado = False
    for reserva in reservas:
        if clases.upper() == reserva['clases'].upper() and fecha.upper() == reserva['fecha'].upper():
            hora = reserva['hora']
            horas_reservadas.append(hora)
            reservado = True

    if reservado == True:
        for hora in data['horas']:
            if hora in horas_reservadas:
                estado = 'RESERVADO'
            else:
                estado = 'DISPONIBLE'
            print(f"{hora} - {estado}")
    elif reservado == False:
        print(f"No hay reservas realizadas para la {clases} en la fecha: {fecha}")
        for hora in data['horas']:
            print(f"{hora} - DISPONIBLE")
    
def reservarClase():
  while True: 
    print("Seleccionar clase")
    i = 1
    for clase in data['clases']:
      print (f"{i} - {clase}")
      i = i+1
      op = validarNumero()
      if op > 0 and op < 6:
        clase = data['clases'][op-1]
        valor = data['valor'][op-1]
        print("Se ha seleccionado la clase ", clase, " y su valor es: ", valor)
        break
      else:
        print("La opción debe ser entre 1 y 5")

    print("Seleccione la fecha")
    fecha = validarString()
    print("Se ha ingresado la fecha: ",fecha)

    while True:
            print("Seleccionar Hora")
            i =1
            for hora in data['horas']:
                print(f"{i} - {hora}")
                i = i+1
            op = validarNumero()
            if op > 0 and op <6:
                hora = data['horas'][op-1]
                print("Se ha seleccionado la hora ", hora)
                break
            else:
                print("La opción debe ser entre 1 y 5")

    reservado = False
    for reserva in reservas:
            if clase.upper() == reserva['clase'].upper() and fecha.upper() == reserva['fecha'].upper() and hora.upper() == reserva['hora'].upper():
                reservado = True
    if reservado == True:
            print("Clase, fecha y hora se encuentra reservada...")
            print("Horarios Disponibles: ")
            disponibilidad(clase,fecha)
            print("\n")
            continue
    elif reservado == False:
            print("Clase, fecha y hora disponible...")

            

    print("Ingrese su nombre:")
    nombre = validarString()
    print(f"{nombre}, su reserva esta en proceso")

        #Ingresar contacto
    print("Ingrese su contacto: ")
    contacto = validarString()
    print(f"{contacto}, registrado")

        #crear el diccionario con los data registrado y validados
    reserva ={
        'clases':clase,
        'fecha':fecha,
        'hora':hora,
        'nombre':nombre,
        'contacto': contacto,
        'costo': valor
        }
        #Se agrega diccionario a la lista de reservas
    reservas.append(reserva)

        #Imprimit detalle de la reserva
    print(f"""
          Resumen de la reserva
          ------------------------------
          Nombre: {reserva['nombre']}
          Clase: {reserva['clase']}
          Fecha: {reserva['fecha']}
          Hora: {reserva['hora']}
          Contacto: {reserva['contacto']}
          Total: {reserva['valor']}
              """)
        
        #Preguntar si desea otra reserva o volver al menú principal
    print("S- Realizar otra reserva\n X- Volver al menú principal")
    op = validarString()
    if op.upper() =='S':
         reservarClase()
    elif op.upper() =='X':
            menu()
    else:
            print("Opción incorrecta")

def guardarReservas():
    with open('reservas.txt', 'w') as archivo:
        archivo.write("RESERVAS REALIZADAS\n")
        i=1
        for reserva in reservas:
            if reserva['clases']=="clases":
                print("")
            else:
                archivo.write(f"""
Detalle Reserva: {i}
------------------------------
Nombre: {reserva['nombre']}
Clase: {reserva['clase']}
Fecha: {reserva['fecha']}
Hora: {reserva['hora']}
Contacto: {reserva['contacto']}
Total: {reserva['costo']}
              """)
                i=i+1
        print("Archivo generado exitosamente")

def administrarReservas():
    print("Ingrese el nombre para consultar las reservas")
    nombre = validarString()
    #recorremos la lista de reservas y validamos si el nombre que estamos consultando está en la llave nombre de alguna reserva
    i=0
    existe = False
    print(f"Consultando reservas de: {nombre}...")
    for reserva in reservas:
        if nombre.upper() == reserva['nombre']:
            existe = True
            i=i+1
            print(f"""
------------------------------
RESERVA {i}: 
Sala: {reserva['clases']}
Fecha: {reserva['fecha']}
Hora: {reserva['hora']}
Total: {reserva['costo']}
              """)
    if existe == False:
        print(f"No existen reservas con el nombre: {nombre}")

def salir():
    print("mueranse todos")
    exit()        

def menu():
 while True:
  print("""\n ------------Menu------------"
  1.Reservar Clase de baile
  2. Consultar disponibilidad
  3. Administrar Reservas
  4. Reserva en archivo CSV
  5. Reserva en archivo TXT
  6. Salir """)

  op = input("\n Seleccione una opcion (1-6): ")

  if op == '1':
    reservarClase()
  elif op == '2':
    disponibilidad()
  elif op == '3':
    administrarReservas
  elif op == '4':
    reservaCSV()
  elif op == '5':
    guardarReservas
  elif op == '6':
    salir()
  else:
    print("Opción incorrecta")

menu()

