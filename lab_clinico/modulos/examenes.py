import os

from modulos.validaciones import validar_numeros, validar_fecha, validar_letras

def registrar_examen(pacientes, examenes):
    while True:
        try:
            id_paciente = input("Ingrese el ID del paciente: ")
            os.system('cls')
            validar_numeros(id_paciente)
            break
        except ValueError as e:
            print(e)
            continue

    paciente = next((paciente for paciente in pacientes if paciente.id == id_paciente), None)
    if paciente is None:
        print("El paciente no está registrado.")
        return None
    else:
        while True:
            try:
                tipo_examen = input("Ingrese el tipo de examen: ")
                os.system('cls')
                validar_letras(tipo_examen)
                break
            except ValueError as e:
                print(e)
                continue

        while True:
            try:
                fecha_examen = input("Ingrese la fecha de realización del examen (formato DD/MM/AAAA): ")
                os.system('cls')
                if not validar_fecha(fecha_examen):
                    raise ValueError("Fecha no válida. Por favor, ingrese la fecha en el formato DD/MM/AAAA.")
                break
            except ValueError as e:
                print(e)
                continue

        examen = {"id_paciente": id_paciente, "tipo_examen": tipo_examen, "fecha_examen": fecha_examen}
        examenes.append(examen)
        return examen
    
def informacion_examenes(pacientes, examenes):
    while True:
        try:
            id_paciente = input("Ingrese el ID del paciente: ")
            os.system('cls')
            validar_numeros(id_paciente)
            break
        except ValueError as e:
            print(e)
            continue

    paciente = next((paciente for paciente in pacientes if paciente.id == id_paciente), None)
    if paciente is None:
        print("El paciente no está registrado.")
        return None
    else:
        print(f"Información del paciente {id_paciente}:\n")
        print(f"ID: {paciente.id}")
        print(f"Tipo de identificación: {paciente.tipo_id}")
        print(f"Nombre: {paciente.nombres}")
        print(f"Apellido: {paciente.apellidos}")
        print(f"Fecha de nacimiento: {paciente.fecha_nacimiento}")
        print(f"Celular: {paciente.celular}")
        print(f"Correo: {paciente.correo}")
        print(f"EPS: {paciente.entidad_prestadora}")

        examenes_paciente = [examen for examen in examenes if examen['id_paciente'] == id_paciente]
        if not examenes_paciente:
            print("No hay exámenes registrados para este paciente.")
            return None
        else:
            print(f"\nInformación de exámenes para el paciente {id_paciente}:\n")
            for examen in examenes_paciente:
                print(f"Tipo de examen: {examen['tipo_examen']}")
                print(f"Fecha del examen: {examen['fecha_examen']}")
            return examenes_paciente