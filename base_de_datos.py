import os
import time
import winsound
from tqdm import tqdm
from pyfiglet import figlet_format

"""Programa General"""

def loading_bar(total_iterations):
    # Display a loading bar for a given number of iterations.
    for i in tqdm(range(total_iterations), desc="Loading", leave=False):
        time.sleep(0.1)  # Simulate some work being done.

def access_bar_fast(total_iterations):
   # Display a loading bar for a given number of iterations.
    for i in tqdm(range(total_iterations), desc="Accessing", leave=False):
        time.sleep(0.05)  # Simulate some work being done.

def loading_bar_light(total_iterations):
   # Display a loading bar for a given number of iterations.
    for i in tqdm(range(total_iterations), desc="Loading", leave=False):
        time.sleep(0.01)  # Simulate some work being done.

"""Programa en Español"""
def accesoesp():
    loading_bar_light(100)
    time.sleep(0.5)
    os.system('cls') 
    user = input("Cuál es su nombre de usuario? ")
    contra = input("Cuál es su contraseña? ")
    if user == "xavi":
        if contra == "boss":
            winsound.PlaySound('access.wav', winsound.SND_FILENAME)
            print ("¡Accediendo a la base de datos!")
            datosesp()
        else:
            access_bar_fast(100)
            time.sleep(0.5)
            os.system('cls')
            print ("Contraseña Incorrecta")
            accesoesp()
    else:
        access_bar_fast(100)
        time.sleep(0.5)
        os.system('cls') 
        print ("Usuario Incorrecto")
        print ("Espere 3 segundos para continuar")
        time.sleep(3)
        os.system('cls') 
        return accesoesp()
    

def datosesp():
    access_bar_fast(100)
    time.sleep(0.5)
    os.system('cls')
    print ("1. Nombre Completo")
    print ("2. Fecha de Nacimiento")
    print ("3. Ciudad de Residencia")
    print ("4. Estudios")
    print ("5. Hobbies")
    print ("6. Desconectar")
    eleccionesesp()


def eleccionesesp():
    eleccion = input("¿Cuál entrada eliges? (Si no te acuerdas de las elecciones, escribe recordatorio)")
    match eleccion:
        case '1':
            print ("Xavier Sanchez Costa")
            eleccionesesp()
        case "2":
            print ("26/03/2008")
            eleccionesesp()
        case "3":
            print ("Terrassa, Barcelona")
            eleccionesesp()
        case "4":
            print ("Educación Secundaria Obligatoria / Dual Diploma")
            eleccionesesp()
        case "5":
            print ("Conducción, Aeronáutica, Programación en Python")
            eleccionesesp()
        case "recordatorio":
            datosesp()
        case "6":
            os.system('cls')   
            international()
        case other:
            print ("Entrada no valida")
            eleccionesesp()


"""Programa en Català"""
def accesocat():
    loading_bar_light(100)
    time.sleep(0.5)
    os.system('cls') 
    user = input("Quin és el vostre nom d'usuari? ")
    contra = input("Quina és la contrasenya? ")
    if user == "xavi":
        if contra == "boss":
            winsound.PlaySound('access.wav', winsound.SND_FILENAME)
            print ("Accedint a la base de dades!")
            datoscat()
        else:
            print ("Contrasenya Incorrecta")
            accesocat()
    else:
        print ("Usuari Incorrecte")
        accesocat()


def datoscat():
    print ("1. Nom Complet")
    print ("2. Data de Naixement")
    print ("3. Ciutat de Residència")
    print ("4. Estudis")
    print ("5. Hobbies")
    print ("6. Desconectar")
    eleccionescat()


def eleccionescat():
    eleccion = input("Quina entrada tries? (Si no te'n recordes de les eleccions escriu recordatori)")
    match eleccion:
        case '1':
            print ("Xavier Sanchez Costa")
            eleccionescat()
        case "2":
            print ("26/03/2008")
            eleccionescat()
        case "3":
            print ("Terrassa, Barcelona")
            eleccionescat()
        case "4":
            print ("Educacion Secundària Obligatòria / Dual Diploma")
            eleccionescat()
        case "5":
            print ("Conducció, Aeronàutica, Programació a Python")
            eleccionescat()
        case "recordatori":
            datoscat()
        case "6":
            os.system('cls') 
            international()
        case other:
            print ("Entrada no vàlida")
            eleccionescat()


"""Program in English"""
def accesoeng():
    loading_bar_light(100)
    time.sleep(0.5)
    os.system('cls') 
    user = input("What is your username? ")
    contra = input("What is your password? ")
    if user == "xavi":
        if contra == "boss":
            winsound.PlaySound('access.wav', winsound.SND_FILENAME)
            print ("Accessing the database!")
            datoseng()
        else:
            print ("Incorrect Password")
            accesoeng()
    else:
        print ("Incorrect User")
        accesoeng()


def datoseng():
    access_bar_fast(100)
    time.sleep(0.5)
    os.system('cls') 
    print ("1. Full Name")
    print ("2. Date of Birth")
    print ("3. Residence City")
    print ("4. Studies")
    print ("5. Hobbies")
    print ("6. Disconnect")
    eleccioneseng()


def eleccioneseng():
    eleccion = input("Which entry do you choose? (If you don't remember the choices write reminder)")
    match eleccion:
        case '1':
            print ("Xavier Sanchez Costa")
            eleccioneseng()
        case "2":
            print ("26/03/2008")
            eleccioneseng()
        case "3":
            print ("Terrassa, Barcelona")
            eleccioneseng()
        case "4":
            print ("Compulsory Secondary Education (ESO) / Dual Diploma")
            eleccioneseng()
        case "5":
            print ("Driving, Aeronautics, Python programming")
            eleccioneseng()
        case "reminder":
            datoseng()
        case "6":
            os.system('cls') 
            international()
        case other:
            print ("Invalid input")
            eleccioneseng()


def international():
    print(figlet_format("Database |A|", font = "big"))
    loading_bar(100)
    winsound.PlaySound('start12345.wav', winsound.SND_FILENAME)
    time.sleep(2.5)
    os.system('cls')
    print ("Bienvenido a la base de datos! / Benvingut a la base de dades! / Welcome to the database! :)")
    idioma = input("Que idioma? (ESP)/ Quin idioma? (CAT)/ What language? (ENG)")
    match idioma:
        case "ESP":
            os.system('cls') 
            accesoesp()
        case "esp":
            os.system('cls') 
            accesoesp()
        case "CAT":
            os.system('cls') 
            accesocat()
        case "cat":
            os.system('cls') 
            accesocat()
        case "ENG":
            os.system('cls') 
            accesoeng()
        case "eng":
            os.system('cls') 
            accesoeng()
        case other:
            print ("Incorrecto / Incorrecte / Bad Input")
            international()


"""Inicio de Programa (LOOP)"""

international()
