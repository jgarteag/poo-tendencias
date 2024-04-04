import os

from modulos.validaciones import validar_celular, validar_email, validar_fecha, validar_letras, validar_numeros

class Persona:
    def __init__(self, id, tipo_id, nombres, apellidos, fecha_nacimiento, celular, correo, contacto_nombre, contacto_telefono):
        self.__id = id
        self.__tipo_id = tipo_id
        self.__nombres = nombres
        self.__apellidos = apellidos
        self.__fecha_nacimiento = fecha_nacimiento
        self.__celular = celular
        self.__correo = correo
        self.__contacto_nombre = contacto_nombre
        self.__contacto_telefono = contacto_telefono
        
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id):
        validar_numeros(id)
        self.__id = id
    
    @property
    def tipo_id(self):
        return self.__tipo_id
    
    @tipo_id.setter
    def tipo_id(self, tipo_id):
        validar_letras(tipo_id)
        self.__tipo_id = tipo_id
    
    @property
    def nombres(self):
        return self.__nombres
    
    @nombres.setter
    def nombres(self, nombres):
        validar_letras(nombres)
        self.__nombres = nombres
    
    @property
    def apellidos(self):
        return self.__apellidos
    
    @apellidos.setter
    def apellidos(self, apellidos):
        validar_letras(apellidos)
        self.__apellidos = apellidos
    
    @property
    def fecha_nacimiento(self):
        return self.__fecha_nacimiento
    
    @fecha_nacimiento.setter
    def fecha_nacimiento(self, fecha_nacimiento):
        validar_fecha(fecha_nacimiento)
        self.__fecha_nacimiento = fecha_nacimiento
    
    @property
    def celular(self):
        return self.__celular
    
    @celular.setter
    def celular(self, celular):
        validar_celular(celular)
        self.__celular = celular
    
    @property
    def correo(self):
        return self.__correo
    
    @correo.setter
    def correo(self, correo):
        validar_email(correo)
        self.__correo = correo
    
    @property
    def contacto_nombre(self):
        return self.__contacto_nombre
    
    @contacto_nombre.setter
    def contacto_nombre(self, contacto_nombre):
        validar_letras(contacto_nombre)
        self.__contacto_nombre = contacto_nombre
    
    @property
    def contacto_telefono(self):
        return self.__contacto_telefono
        
    @contacto_telefono.setter
    def contacto_telefono(self, contacto_telefono):
        validar_celular(contacto_telefono)
        self.__contacto_telefono = contacto_telefono
        
    
    
class Paciente(Persona):
    def __init__(self, id, tipo_id, nombres, apellidos, fecha_nacimiento, celular, correo, contacto_nombre, contacto_telefono, entidad_prestadora, fecha_registro):
        super().__init__(id, tipo_id, nombres, apellidos, fecha_nacimiento, celular, correo, contacto_nombre, contacto_telefono)
        self.__entidad_prestadora = entidad_prestadora
        self.__fecha_registro = fecha_registro
        
    @property
    def entidad_prestadora(self):
        return self.__entidad_prestadora
    
    @property
    def fecha_registro(self):
        return self.__fecha_registro

    def __str__(self):
        return (f"Paciente {self.nombres} {self.apellidos} \n"
                f"ID: {self.id}\n"
                f"Tipo ID: {self.tipo_id}\n"
                f"Fecha de Nacimiento: {self.fecha_nacimiento}\n"
                f"Celular: {self.celular}\n"
                f"Email: {self.correo}\n"
                f"Nombre de Contacto: {self.contacto_nombre}\n"
                f"Teléfono de Contacto: {self.contacto_telefono}\n"
                f"Entidad de Salud: {self.entidad_prestadora}\n"
                f"Fecha de Registro: {self.fecha_registro.strftime('%Y-%m-%d %H:%M:%S')}\n"
                )
        
    @entidad_prestadora.setter
    def entidad_prestadora(self, entidad_prestadora):
        self.__entidad_prestadora = entidad_prestadora
    
    @fecha_registro.setter
    def fecha_registro(self, fecha_registro):
        validar_fecha(fecha_registro)
        self.__fecha_registro = fecha_registro


class Medico(Persona):
    medicos = [
        {"id": 1, "nombres": "Carlos", "apellidos": "Perez", "celular": "1234567890", "direccion": "Calle 123", "tarjeta_profesional": "123456", "ordenes": 0},
        {"id": 2, "nombres": "Juan", "apellidos": "Gomez", "celular": "0987654321", "direccion": "Carrera 456", "tarjeta_profesional": "654321", "ordenes": 0},
        {"id": 3, "nombres": "Maria", "apellidos": "Lopez", "celular": "6789012345", "direccion": "Avenida 789", "tarjeta_profesional": "987654", "ordenes": 0},
        {"id": 4, "nombres": "Ana", "apellidos": "Rodriguez", "celular": "4567890123", "direccion": "Transversal 012", "tarjeta_profesional": "456789", "ordenes": 0},
        {"id": 5, "nombres": "Pedro", "apellidos": "Martinez", "celular": "2345678901", "direccion": "Diagonal 345", "tarjeta_profesional": "234567", "ordenes": 0}
    ]
    
    def __init__(self, id, nombres, apellidos, celular, direccion, tarjeta_profesional, ordenes=0):
        super().__init__(id, nombres, apellidos, celular)
        self.direccion = direccion
        self.tarjeta_profesional = tarjeta_profesional
        self.ordenes = ordenes
        
    @classmethod
    def listar_medicos(cls):
        return [(medico["id"], f"{medico['nombres']} {medico['apellidos']}") for medico in cls.medicos]

class TipoExamen:
    tipos = [
        {"id": 1, "nombre": "Hemograma", "precio": 50000},
        {"id": 2, "nombre": "Perfil Lipídico", "precio": 20000},
        {"id": 3, "nombre": "Perfil Hepático", "precio": 30000},
        {"id": 4, "nombre": "Perfil Renal", "precio": 25000},
        {"id": 5, "nombre": "Glucosa", "precio": 80000},
        {"id": 6, "nombre": "Urea", "precio": 26000},
        {"id": 7, "nombre": "Creatinina", "precio": 70000},
        {"id": 8, "nombre": "Ácido Úrico", "precio": 10000},
        {"id": 9, "nombre": "Perfil Tiroideo", "precio": 15000},
        {"id": 10, "nombre": "Perfil de Coagulación", "precio": 90000}
    ]
    
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        
    @classmethod
    def listar_tipos(cls):
        return [(tipo["id"], tipo["nombre"]) for tipo in cls.tipos]
    
    def __str__(self):
        return f"{self.nombre}"

class Eps:
    eps = [
        {"eps" : "Caja de previsión social del Casanare", "nit" : "1234567890", "telefono" : "1234567890", "celular" : "300125965", "correo" : "casanre@eps.com", "persona_encargada" : "Departamento del Casanare", "tipo" : "Subsidiado"},
        {"eps" : "EPM", "nit" : "0987654321", "telefono" : "0987654321", "celular" : "300987654", "correo" : "epm@eps.com", "persona_encargada" : "Empresas públicas de Medellín", "tipo" : "Contributivo"},
        {"eps" : "Nueva EPS", "nit" : "6789012345", "telefono" : "6789012345", "celular" : "300678901", "correo" : "nuevaeps@neps.com", "persona_encargada" : "Ministerio de Hacienda", "tipo" : "Subsidiado"},
        {"eps" : "Saviasalud", "nit" : "4567890123", "telefono" : "4567890123", "celular" : "300456789", "correo" : "saviasalud@eps.com", "persona_encargada" : "Municipio de Medellín", "tipo" : "Prepagada"},
        {"eps" : "Mallamas", "nit" : "2345678901", "telefono" : "2345678901", "celular" : "300234567", "correo" : "mallamaseps@mallamas.com", "persona_encargada" : "Pedro Martinez", "tipo" : "Subsidiado y Contributivo"},
        {"eps" : "Sanitas", "nit" : "3456789012", "telefono" : "3456789012", "celular" : "300345678", "correo" : "sanitas@sanitaseps.com", "persona_encargada" : "Maria Lopez", "tipo" : "Subsidiado y Contributivo"},
        {"eps" : "Sura", "nit" : "4567890123", "telefono" : "4567890123", "celular" : "300456789", "correo" : "sura@suraeps.com", "persona_encargada" : "Ana Rodriguez", "tipo" : "Subsidiado y Contributivo"},
        {"eps" : "Salud Total", "nit" : "5678901234", "telefono" : "5678901234", "celular" : "300567890", "correo" : "saludtotal@saludtotaleps.com", "persona_encargada" : "Juan Gomez", "tipo" : "Subsidiado y Contributivo"}
    ]

    @staticmethod
    def consultar_eps():
        print("¿Cuál EPS deseas consultar?")
        for i, eps in enumerate(Eps.eps, start=1):
            print(f"{i}. {eps['eps']}")
        
        while True:
            try:
                seleccion = int(input("Por favor, ingrese el número de la EPS que desea consultar: "))
                os.system('cls')
                if 1 <= seleccion <= len(Eps.eps):
                    eps_seleccionada = Eps.eps[seleccion - 1]
                    print("Datos de la EPS:\n")
                    print(f"EPS: {eps_seleccionada['eps']}")
                    print(f"NIT: {eps_seleccionada['nit']}")
                    print(f"Teléfono: {eps_seleccionada['telefono']}")
                    print(f"Celular: {eps_seleccionada['celular']}")
                    print(f"Correo: {eps_seleccionada['correo']}")
                    print(f"Persona Encargada: {eps_seleccionada['persona_encargada']}")
                    print(f"Tipo: {eps_seleccionada['tipo']}\n")
                    break
                else:
                    print("Por favor, ingrese un número válido.")
            except ValueError:
                print("Por favor, ingrese un número.")