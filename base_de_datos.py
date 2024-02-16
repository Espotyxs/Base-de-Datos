import os
import time
from tqdm import tqdm
from pyfiglet import figlet_format
from replit import audio

use = "xavi"
passw = "boss"
main = ""

"""Programa General"""
def clear(seconds = 0):
  time.sleep(seconds)
  os.system('clear')
  
def carga():
    clear()
    loading_bar_light(100)
    time.sleep(0.5)
    clear()
    
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
    clear() 
    user = input("Cuál es su nombre de usuario? (Presione enter para volver a la seleccion de idiomas)")
    clear()
    contra = input("Cuál es su contraseña? ")
    if user == use:
        if contra == passw:
            accessaudio = audio.play_file('access.wav')
            print ("¡Accediendo a la base de datos!")
            datosesp()
        else:
            access_bar_fast(100)
            time.sleep(0.5)
            clear()
            print ("Contraseña Incorrecta")
            accesoesp()
    elif user == main:
        loading_bar_light(100)
        international()
    else:
        access_bar_fast(100)
        time.sleep(0.5)
        clear() 
        print ("Usuario Incorrecto")
        print ("Espere 3 segundos para continuar")
        time.sleep(3)
        clear() 
        return accesoesp()
    

def datosesp():
    access_bar_fast(100)
    time.sleep(0.5)
    clear()
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
            carga()
            print ("Xavier Sanchez Costa")
            salir = input("Para salir al menú principal presiona enter")
            if salir == "":
                clear() 
                datosesp()
        case "2":
            carga()
            print ("26/03/2008")
            salir = input("Para salir al menú principal presiona enter")
            if salir == "":
                clear() 
                datosesp()
        case "3":
            carga()
            print ("Terrassa, Barcelona")
            salir = input("Para salir al menú principal presiona enter")
            if salir == "":
                clear() 
                datosesp()
        case "4":
            carga()
            print ("Educación Secundaria Obligatoria / Dual Diploma")
            salir = input("Para salir al menú principal presiona enter")
            if salir == "":
                clear() 
                datosesp()
        case "5":
            carga()
            print ("Conducción, Aeronáutica, Programación en Python")
            salir = input("Para salir al menú principal presiona enter")
            if salir == "":
                clear() 
                datosesp()
        case "recordatorio":
            datosesp()
        case "6":
            clear()   
            international()
        case other:
            print ("Entrada no valida")
            eleccionesesp()


"""Programa en Català"""
def accesocat():
    loading_bar_light(100)
    time.sleep(0.5)
    clear() 
    user = input("Quin és el vostre nom d'usuari? (Presiona la tecla enter per tornar a la selecció d'idiomes)")
    clear()
    contra = input("Quina és la contrasenya? ")
    if user == use:
        if contra == passw:
            accessaudio = audio.play_file('access.wav')
            print ("Accedint a la base de dades!")
            datoscat()
        else:
            access_bar_fast(100)
            print ("Contrasenya Incorrecta")
            time.sleep(3)
            clear() 
            accesocat()
    elif user == main:
        loading_bar_light(100)
        international() 
    else:
        access_bar_fast(100)
        print ("Usuari Incorrecte")
        time.sleep(3)
        clear() 
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
            carga()
            print ("Xavier Sanchez Costa")
            eleccionescat()
            salir = input("Per sortir al menú clica la tecla enter")
            if salir == "":
                clear() 
                datoscat()
        case "2":
            carga()
            print ("26/03/2008")
            eleccionescat()
            salir = input("Per sortir al menú clica la tecla enter")
            if salir == "":
                clear() 
                datoscat()
        case "3":
            carga()
            print ("Terrassa, Barcelona")
            eleccionescat()
            salir = input("Per sortir al menú clica la tecla enter")
            if salir == "":
                clear() 
                datoscat()
        case "4":
            carga()
            print ("Educacion Secundària Obligatòria / Dual Diploma")
            eleccionescat()
            salir = input("Per sortir al menú clica la tecla enter")
            if salir == "":
                clear() 
                datoscat()
        case "5":
            carga()
            print ("Conducció, Aeronàutica, Programació a Python")
            eleccionescat()
            salir = input("Per sortir al menú clica la tecla enter")
            if salir == "":
                clear() 
                datoscat()
        case "recordatori":
            datoscat()
        case "6":
            clear() 
            international()
        case other:
            print ("Entrada no vàlida")
            eleccionescat()


"""Program in English"""
def accesoeng():
    loading_bar_light(100)
    time.sleep(0.5)
    clear() 
    user = input("What is your username? (Press enter to return to the language selection)")
    clear()
    contra = input("What is your password? ")
    if user == use:
        if contra == passw: 
            accessaudio = audio.play_file('access.wav')
            print ("Accessing the database!")
            datoseng()
        else:
            print ("Incorrect Password")
            time.sleep(3)
            clear() 
            accesoeng()
    elif user == main:
        loading_bar_light(100)
        international()
    else:
        print ("Incorrect User")
        time.sleep(3)
        clear() 
        accesoeng()


def datoseng():
    access_bar_fast(100)
    time.sleep(0.5)
    clear() 
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
            carga()
            print ("Xavier Sanchez Costa")
            salir = input("Press enter to go to the main menu")
            if salir == "":
                clear() 
                datoscat()
        case "2":
            carga()
            print ("26/03/2008")
            salir = input("Press enter to go to the main menu")
            if salir == "":
                clear() 
                datoscat()
        case "3":
            carga()
            print ("Terrassa, Barcelona")
            salir = input("Press enter to go to the main menu")
            if salir == "":
                clear() 
                datoscat()
        case "4":
            carga()
            print ("Compulsory Secondary Education (ESO) / Dual Diploma")
            salir = input("Press enter to go to the main menu")
            if salir == "":
                clear() 
                datoscat()
        case "5":
            carga()
            print ("Driving, Aeronautics, Python programming")
            salir = input("Press enter to go to the main menu")
            if salir == "":
                datoscat()
                clear()     
        case "reminder":
            datoseng()
        case "6":
            clear() 
            international()
        case other:
            print ("Invalid input")
            eleccioneseng()


def international():
    print(figlet_format("Database |A|", font = "big"))
    loading_bar(100)
    startaudio = audio.play_file('start12345.wav')
    time.sleep(2.5)
    print ("Bienvenido a la base de datos! / Benvingut a la base de dades! / Welcome to the database! :)")
    idioma = input("Que idioma? (ESP)/ Quin idioma? (CAT)/ What language? (ENG)")
    match idioma:
        case "ESP":
            clear() 
            accesoesp()
        case "esp":
            clear() 
            accesoesp()
        case "CAT":
            clear() 
            accesocat()
        case "cat":
            clear() 
            accesocat()
        case "ENG":
            clear() 
            accesoeng()
        case "eng":
            clear() 
            accesoeng()
        case other:
            print ("Incorrecto / Incorrecte / Bad Input")
            international()


"""Inicio de Programa (LOOP)"""

international()
