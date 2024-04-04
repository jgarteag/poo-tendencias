import os

from entidades.clases import Paciente
from modulos.validaciones import validar_celular, validar_email, validar_fecha, validar_letras, validar_numeros
from datetime import datetime

ids_pacientes = []

def solicitar_datos_paciente():
    while True:
        try:
            id = input("Ingrese el número de ID del paciente: ")
            os.system('cls')
            validar_numeros(id)
            if id in ids_pacientes:
                print("Este ID ya está en uso. Por favor, intente con otro.")
            else:
                ids_pacientes.append(id)
                break
        except ValueError:
            print("El ID debe ser un número entero.")

    while True:
        try:
            print("Seleccione el tipo de ID del paciente:")
            print("1. CC")
            print("2. Tarjeta de Identidad")
            print("3. Pasaporte")
            print("4. Cedula de Extranjeria")
            print("5. Registro Civil")
            
            seleccion = int(input("Ingrese el número de su selección: "))
            os.system('cls')
            
            tipos_id = {1: "CC", 2: "Tarjeta de Identidad", 3: "Pasaporte", 4: "Cedula de Extranjeria", 5: "Registro Civil"}
            
            if seleccion in tipos_id:
                tipo_id = tipos_id[seleccion]
                break
            else:
                os.system('cls')
                print("Por favor, ingrese un número válido.")
        except ValueError:
            os.system('cls')
            print("Por favor, ingrese un número.")

    while True:
        try:
            nombres = input("Ingrese los nombres del paciente: ")
            os.system('cls')
            validar_letras(nombres)
            break
        except ValueError:
            print("Los nombres solo deben contener letras.")

    while True:
        try:
            apellidos = input("Ingrese los apellidos del paciente: ")
            os.system('cls')
            validar_letras(apellidos)
            break
        except ValueError:
            print("Los apellidos solo deben contener letras.")

    while True:
        try:
            fecha_nacimiento = input("Ingrese la fecha de nacimiento del paciente (YYYY-MM-DD): ")
            os.system('cls')
            validar_fecha(fecha_nacimiento)
            break
        except ValueError:
            print("La fecha de nacimiento debe estar en formato YYYY-MM-DD.")

    while True:
        try:
            celular = input("Ingrese el número de celular del paciente: ")
            os.system('cls')
            validar_celular(celular)
            break
        except ValueError:
            print("El número de celular debe ser válido.")

    while True:
        try:
            correo = input("Ingrese el correo electrónico del paciente: ")
            os.system('cls')
            validar_email(correo)
            break
        except ValueError:
            print("El correo electrónico debe ser válido.")

    while True:
        try:
            contacto_nombre = input("Ingrese el nombre del contacto del paciente: ")
            os.system('cls')
            validar_letras(contacto_nombre)
            break
        except ValueError:
            print("El nombre del contacto solo debe contener letras.")

    while True:
        try:
            contacto_telefono = input("Ingrese el número de teléfono del contacto del paciente: ")
            os.system('cls')
            validar_celular(contacto_telefono)
            break
        except ValueError:
            print("El número de teléfono del contacto debe ser válido.")

    while True:
        print("Ingrese la entidad prestadora de salud del paciente:")
        print("1. Poliza")
        print("2. Particular")
        opcion = input("Seleccione una opción (1, 2): ")
        os.system('cls')
        if opcion == "1":
            entidad_prestadora = "EPS"
            break
        elif opcion == "2":
            entidad_prestadora = "Particular"
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")

    fecha_registro = datetime.now()

    return (id, tipo_id, nombres, apellidos, fecha_nacimiento, celular, correo, contacto_nombre, contacto_telefono, entidad_prestadora, fecha_registro)

def registrar_paciente():
    datos_paciente = solicitar_datos_paciente()
    paciente = Paciente(*datos_paciente)
    return paciente