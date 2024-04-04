import os
from modulos.registro_pacientes import registrar_paciente
from modulos.orden_medica import registrar_orden_medica, medico_mas_ordenes
from modulos.examenes import registrar_examen, informacion_examenes
from entidades.clases import Eps


def menu_principal(pacientes, examenes):
    while True:
        print("1. Ingresar paciente")
        print("2. Registrar Orden Médica")
        print("3. Médico que mas pacientes remitió")
        print("4. Ingresar Examenes")
        print("5. Información Examenes")
        print("6. EPS")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")
        
        os.system('cls')
        if opcion == "1":
            nuevo_paciente = registrar_paciente()
            pacientes.append(nuevo_paciente)
            os.system('cls')
            print(f"Paciente {nuevo_paciente.nombres} registrado exitosamente!".upper())
            print("\nDatos del paciente:\n".upper())
            print(nuevo_paciente, "\n")
        elif opcion == "2":
            orden_medica = registrar_orden_medica(pacientes, examenes)
            if orden_medica is not None:
                print("Orden médica registrada exitosamente!")
                print("\nDatos de la orden médica:\n")
                print(orden_medica, "\n")
            else:
                continue
        elif opcion == "3":
            medico = medico_mas_ordenes()
            print(medico)
        elif opcion == "4":
            examen = registrar_examen(pacientes, examenes)
            if examen is not None:
                print("Examen registrado exitosamente!")
                print("\nDatos del examen:\n")
                print(examen, "\n")
            else:
                continue
        elif opcion == "5":
            informacion_examenes(pacientes, examenes)
            print("\n")
        elif opcion == "6":
            Eps.consultar_eps()
        elif opcion == "7":
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")
            
def main():
    pacientes = []
    examenes = []
    print("*" * 41)
    print("*" * 10, "Laboratorio Clínico", "*" * 10)
    print("*" * 15 , "Konoha SAS","*" * 14)
    print("*" * 41)
    menu_principal(pacientes, examenes)


if __name__ == "__main__":
    main()