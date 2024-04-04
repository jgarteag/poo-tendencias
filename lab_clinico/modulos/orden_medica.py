import os
import random

from datetime import datetime
from modulos.registro_pacientes import registrar_paciente
from modulos.validaciones import *
from entidades.clases import Medico, TipoExamen

def verificar_paciente(pacientes, id_paciente):
    for paciente in pacientes:
        if paciente.id == id_paciente:
            return paciente
    return None

consecutivo_orden = 0

def generar_consecutivo_orden():
    global consecutivo_orden
    consecutivo_orden += 1
    return f"OR-{consecutivo_orden:02d}"

def solicitar_fechas():
    while True:
        fecha_solicitud = input("Ingrese la fecha de solicitud de la orden (YYYY-MM-DD): ")
        os.system('cls')
        if validar_fecha(fecha_solicitud):
            break
        else:
            print("La fecha de solicitud debe estar en formato YYYY-MM-DD.")
    
    fecha_ingreso_sistema = datetime.now().strftime('%Y-%m-%d')

    return fecha_solicitud, fecha_ingreso_sistema

def seleccionar_medico():
    medicos = Medico.listar_medicos()
    for id, nombre in medicos:
        print(f"{id}: {nombre}")
    
    while True:
        id_medico = input("Ingrese el ID del médico que va en esta orden: ")
        if any(medico for medico in medicos if medico[0] == int(id_medico)):
            return id_medico
        else:
            print("El ID ingresado no corresponde a ningún médico. Por favor, intente de nuevo.")
            

def generar_numero_orden_medico():
    return random.randint(1000, 9999)

def seleccionar_tipo_examen():
    tipos_examen = TipoExamen.listar_tipos()
    for id, nombre in tipos_examen:
        print(f"{id}: {nombre}")
    
    while True:
        id_tipo_examen = input("Ingrese el ID del tipo de examen para esta orden: ")
        os.system('cls')
        if any(tipo_examen for tipo_examen in tipos_examen if tipo_examen[0] == int(id_tipo_examen)):
            return id_tipo_examen
        else:
            print("El ID ingresado no corresponde a ningún tipo de examen. Por favor, intente de nuevo.")
            
def solicitar_datos_adicionales():
    while True:
        fecha_realizacion = input("Ingrese la fecha de realización del examen (YYYY-MM-DD): ")
        os.system('cls')
        if validar_fecha(fecha_realizacion):
            break
        else:
            print("La fecha de realización debe estar en formato YYYY-MM-DD.")
    
    observaciones = input("Ingrese las observaciones adicionales (si las hay): ")
    os.system('cls')

    return fecha_realizacion, observaciones

def generar_factura(paciente, valor_examen):
    numero_factura = random.randint(1000, 9999)
    fecha_creacion = datetime.now()
    factura = {
        "numero_factura": numero_factura,
        "fecha_creacion": fecha_creacion,
        "valor_a_pagar": valor_examen
    }
    print("\nDatos de la factura:\n")
    print(factura)
    return factura

def registrar_orden_medica(pacientes, examenes):
    id_paciente = input("Ingrese el ID del paciente: ")
    paciente = verificar_paciente(pacientes, id_paciente)
    if paciente is None:
        print("Paciente no encontrado. ¿Desea registrarlo?")
        print("1. Sí")
        print("2. No")
        opcion = input("Seleccione una opción: ")
        os.system('cls')
        if opcion == "1":
            paciente = registrar_paciente()
        else:
            return

    consecutivo = generar_consecutivo_orden()
    fecha_solicitud, fecha_ingreso_sistema = solicitar_fechas()
    id_medico = seleccionar_medico()
    numero_orden_medico = generar_numero_orden_medico()
    id_tipo_examen = seleccionar_tipo_examen()
    fecha_realizacion, observaciones = solicitar_datos_adicionales()

    orden_medica = {
        "consecutivo": consecutivo,
        "fecha_solicitud": fecha_solicitud,
        "fecha_ingreso_sistema": fecha_ingreso_sistema,
        "id_medico": id_medico,
        "numero_orden_medico": numero_orden_medico,
        "id_tipo_examen": id_tipo_examen,
        "fecha_realizacion": fecha_realizacion,
        "observaciones": observaciones
    }

    Medico.medicos[int(id_medico)-1]["ordenes"] += 1
    print("\nDatos del paciente:\n")
    print(paciente)
    
    if paciente.entidad_prestadora == "Particular":
        valor_examen = TipoExamen.tipos[int(id_tipo_examen)-1]["precio"]
        generar_factura(paciente, valor_examen)
        
    return orden_medica

def medico_mas_ordenes():
    max_ordenes = max(medico['ordenes'] for medico in Medico.medicos)
    if max_ordenes == 0:
        return "Aún no se han remitido órdenes."
    else:
        medicos_max_ordenes = [medico for medico in Medico.medicos if medico['ordenes'] == max_ordenes]
        return medicos_max_ordenes