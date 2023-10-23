
"""Programa en Español"""
def accesoesp():
    user = input("Cuál es su nombre de usuario? ")
    contra = input("Cuál es su contraseña? ")
    if user == "xavi":
        if contra == "boss":
            print ("¡Accediendo a la base de datos!")
            datosesp()
        else:
            print ("Contraseña Incorrecta")
            accesoesp()
    else:
        print ("Usuario Incorrecto")
        accesoesp()
def datosesp():
    print ("1. Nombre Completo")
    print ("2. Fecha de Nacimiento")
    print ("3. Ciudad de Residencia")
    print ("4. Estudios")
    print ("5. Experiencias")
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
        case other:
            print ("Entrada no valida")
            eleccionesesp()
"""Programa en Català"""
def accesocat():
    user = input("Quin és el vostre nom d'usuari? ")
    contra = input("Quina és la contrasenya? ")
    if user == "xavi":
        if contra == "boss":
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
    print ("5. Experiències")
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
        case other:
            print ("Entrada no vàlida")
            eleccionescat()
"""Program in English"""
def accesoeng():
    user = input("What is your username? ")
    contra = input("What is your password? ")
    if user == "xavi":
        if contra == "boss":
            print ("Accessing the database!")
            datoseng()
        else:
            print ("Incorrect Password")
            accesoeng()
    else:
        print ("Incorrect User")
        accesoeng()
def datoseng():
    print ("1. Full Name")
    print ("2. Date of Birth")
    print ("3. Residence City")
    print ("4. Studies")
    print ("5. Experiences")
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
        case other:
            print ("Invalid input")
            eleccioneseng()
def international():
    idioma = input("Que idioma? (ESP)/ Quin idioma? (CAT)/ What language? (ENG)")
    match idioma:
        case "ESP":
            accesoesp()
        case "CAT":
            accesocat()
        case "ENG":
            accesoeng()
        case other:
            print ("Incorrecto / Incorrecte / Bad Input")
            international()
print ("Bienvenido a la base de datos! / Benvingut a la base de dades! / Welcome to the database! :)")
international()

    
