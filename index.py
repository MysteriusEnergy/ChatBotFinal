#Crear un chatbot

"""
  ____ _           _   ____        _
 / ___| |__   __ _| |_| __ )  ___ | |_
| |   | '_ \ / _` | __|  _ \ / _ \| __|
| |___| | | | (_| | |_| |_) | (_) | |_
 \____|_| |_|\__,_|\__|____/ \___/ \__|


"""

# Importamos el modulo ramdom para generar números aleatorios
import random
# Datetime para manejar fechas
from datetime import datetime , timedelta

#Configuramos el locale a español
# import locale
# locale.setlocale(locale.LC_TIME, 'es_MX)

def generar_fecha_azar(inicio, fin):
  delta = fin - inicio
  dias_azar = random.randint(0, delta.days)
  fecha_azar = inicio + timedelta(days=dias_azar)
  return fecha_azar

# Definimos el rango de fechas

fecha_inicio = datetime(2024 , 11 , 1)

# El rango lo configuramos como queramos que se muestre

fecha_fin = datetime(2024 , 11 , 30)



bienvenida = print("¡Hola Bienvenid@ a SaludBuena, estoy aquí para ayudarte a lo que necesites!")

nombre = input("¿Cual es tú nombre?\n")

print(f"Hola {nombre}")

print("¿Tienes cita médica?")

# Pasamos a mayúsculas lo escrito
pregunta_cita = input("")
cita = pregunta_cita.upper()


# Evaluamos si tiene cita médica
if cita == "SI":
    print(f"{nombre}! Encantado de ayudarte!")
    print("¿Qué edad tienes?")
    edad = int(input(""))

    # Si es mayor de 14 y menor de 18, se termina el proceso y sale el mensaje
    if edad > 14 and edad < 18:
        print("¡Tienes que esperar un acompañante por ser menor de edad!")

    # Si es mayor de 18 y menor de 100, entra en el condicional y empieza a evaluar
    elif edad >=18 and edad <= 100:
        print(f"{nombre} ¿Con qué especialista tienes la cita, digita sólo el número?")
        print(" 1. Médico general \n 2. Pediatria \n 3. Cirugía")

        # Creamos una variable vacía para que el usuario escriba el número del especialista
        especialista = int(input(" "))

        # Entra al condicional para evaluar que número puso y depende del número entra.
        if especialista == 1:
            nombre_completo = input("Digita tu nombre completo: ")
            cedula = int(input("Digita tu cedula sin puntos ni espacios: "))
            fecha_generada = generar_fecha_azar(fecha_inicio , fecha_fin)

            # Breviatura "strftime" significa "string format time" (formatear tiempo como cadena).
            print(f"{nombre_completo} ¡Tu cita quedó agendada para el {fecha_generada.strftime('%d de %B de %Y')}") # (%d Representa el día) (%B Nombre completo del mes) (#%Y Representa el año)

        elif especialista == 2:
            nombre_completo = input("Digita tu nombre completo: ")
            cedula = int(input("Digita tu cedula sin puntos ni espacios: "))
            fecha_generada = generar_fecha_azar(fecha_inicio , fecha_fin)
            print(f"{nombre_completo} ¡Tu cita quedó agendada para el {fecha_generada.strftime('%d de %B de %Y')}")

        elif especialista == 3:
            nombre_completo = input("Digita tu nombre completo: ")
            cedula = int(input("Digita tu cedula sin puntos ni espacios: "))
            fecha_generada = generar_fecha_azar(fecha_inicio , fecha_fin)
            print(f"{nombre_completo} ¡Tu cita quedó agendada para el {fecha_generada.strftime('%d de %B de %Y')}")

        else:
          while especialista != especialista:
            print("¡El especialista no existe!")
            especialista = int(input(""))

elif cita == "NO":
    print(f"{nombre} ¿Deseas agendar cita?")
    pregunta_cita = input("")
    cita = pregunta_cita.upper()

    if cita == "NO":
        print("¡Que tengas un buen día!")

    elif cita == "SI":
        print(f"{nombre} ¿Con qué especialista deseas la cita, digita solo el número?")
        print(" 1. Médico general \n 2. Pediatria \n 3. Cirugía")

        especialista = int(input(" "))

        if especialista == 1:
            nombre_completo = input("Digita tu nombre completo: ")
            cedula = int(input("Digita tu cedula sin puntos ni espacios: "))
            fecha_generada = generar_fecha_azar(fecha_inicio , fecha_fin)
            print(f"{nombre_completo} ¡Tu cita quedó agendada para el {fecha_generada.strftime('%d de %B de %Y')}")

        elif especialista == 2:
            nombre_completo = input("Digita tu nombre completo: ")
            cedula = int(input("Digita tu cedula sin puntos ni espacios: "))
            fecha_generada = generar_fecha_azar(fecha_inicio , fecha_fin)
            print(f"{nombre_completo} ¡Tu cita quedó agendada para el {fecha_generada.strftime('%d de %B de %Y')}")

        elif especialista == 3:
            nombre_completo = input("Digita tu nombre completo: ")
            cedula = int(input("Digita tu cedula sin puntos ni espacios: "))
            fecha_generada = generar_fecha_azar(fecha_inicio , fecha_fin)
            print(f"{nombre_completo} ¡Tu cita quedó agendada para el {fecha_generada.strftime('%d de %B de %Y')}")

        else:
            print("El especialista no existe")

else:
    print(f"{nombre} ¡Recuerda cancelar la cita con 12 horas de anticipación, gracias!")

















