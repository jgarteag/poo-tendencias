import re
from datetime import datetime

def validar_celular(celular):
    if not re.fullmatch(r'\d{10}', celular):
        raise ValueError("El número de celular debe tener 10 dígitos.")
    
def validar_email(email):
    if not re.fullmatch(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.(com|co)', email):
        raise ValueError("El email debe tener un '@' y terminar en '.com' o '.co'.")
    
def validar_letras(cadena):
    if not re.fullmatch(r'[A-Za-z]+', cadena):
        raise ValueError("La entrada solo debe contener letras.")
    return cadena

def validar_numeros(valor):
    if not valor.isdigit():
        raise ValueError(f"{valor} no es un número válido")

def validar_fecha(fecha):
    try:
        datetime.strptime(fecha, '%Y-%m-%d')
        return True
    except ValueError:
        return False