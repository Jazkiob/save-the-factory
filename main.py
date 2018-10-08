import random


   
# Definition der Anzahl der Startfelder
machinen_feld_anzahl = 2
glueck_feld_anzahl = 1
nachhaltigkeit_feld_anzahl = 1
rohstoffe_feld_anzahl = 1
forschung_feld_anzahl = 1

nachhaltigkeit_ressourcen = 0
glueck_ressourcen = 1


# Globale Variablen
personal_total = 5
geld_total = 10
rohstoffe_total = 10


def maschinen(geld, personal, felder_kaufen):
    global machinen_feld_anzahl
    verfuegbarkeit_matrix = [0.6, 0.8, 0.9, 0.95, 0.975, 1]
    
    while felder_kaufen > 0:
        geld = geld - 5
        machinen_feld_anzahl += 1
        felder_kaufen -= 1
    
    verfuegbarkeit = verfuegbarkeit_matrix[personal]
    i = 0
    zerstoerte_maschinen_anzahl = 0
    while i <= machinen_feld_anzahl:
        if (random.randint(0,100) > verfuegbarkeit*100):
            zerstoerte_maschinen_anzahl += 1
        i += 1

    machinen_feld_anzahl -= zerstoerte_maschinen_anzahl
    print("-- Maschinen --")
    print("Personal investiert: " + str(personal) + "\n" +
        "Gesamtverfügbarkeit: " + str(verfuegbarkeit) + "\n" +
        "Defekte Maschinen: " + str(zerstoerte_maschinen_anzahl) + "\n" +
        "Gesamtzahl an Maschinen " + str(machinen_feld_anzahl) + "\n")

    return


def produktion(personal):
    global rohstoffe_total

    restrohstoffe = rohstoffe_total - machinen_feld_anzahl
    if restrohstoffe < 0:
        restrohstoffe = 0
    produkte = rohstoffe_total - restrohstoffe
    einnahmen = produkte * 7 #TODO: Verbesserung hier einfügen
    
    print("-- Produktion --")
    print("Produkte erzeugt: " + str(produkte) + "\n" +
        "Restrohstoffe im Lager: " + str(restrohstoffe) + "\n" +
        "Einnahmen: " + str(einnahmen) + " Geld" "\n")
    return einnahmen

def rohstoffe(geld, personal, felder_kaufen):
    global rohstoffe_feld_anzahl
    global rohstoffe_total
    while felder_kaufen > 0:
        geld = geld - 5
        rohstoffe_feld_anzahl += 1
        felder_kaufen -= 1
    rohstoffe_total += personal

    print("-- Rohstoffe --")
    print("Personal investiert: " + str(personal) + "\n" +
        "Anzahl an Lagern: " + str(rohstoffe_feld_anzahl) + "\n" +
        "Rohstoffe vor Produktion: " + str(nachhaltigkeit_ressourcen) + "\n")

    return

def glueck(geld, personal, felder_kaufen):
    global glueck_feld_anzahl
    global glueck_ressourcen

    glueck_matrix = [-1, 0, 1, 2, 3, 4, 5]
    while felder_kaufen > 0:
        geld = geld - 5
        glueck_feld_anzahl += 1
        felder_kaufen -= 1
    
    glueck_ressourcen += glueck_matrix[personal]

    verlorenes_personal = 0
    if personal_total > glueck_ressourcen:
        if random.randint(0, 100) < (5 * (personal_total-glueck_ressourcen)):
            verlorenes_Personal = 1
    print("-- Glueck --")
    print("Personal investiert: " + str(personal) + "\n" +
        "Anzahl an Gluecksfelder: " + str(glueck_feld_anzahl) + "\n" +
        "Anzahl an Gluecksressource: " + str(glueck_ressourcen) + "\n" +
        "Verlorenes Personal: " + str(verlorenes_personal) + "\n")

    return

def nachhaltigkeit(geld, personal, felder_kaufen):
    global nachhaltigkeit_feld_anzahl
    global nachhaltigkeit_ressourcen
    global glueck_feld_anzahl
    global personal_total

    while felder_kaufen > 0:
        geld = geld - 5
        nachhaltigkeit_feld_anzahl += 1
        felder_kaufen -= 1
    
    nachhaltigkeit_matrix = [-1, 1, 2, 3, 4, 5, 6, 7]

    nachhaltigkeit_ressourcen += nachhaltigkeit_matrix[personal]

    bonus_worker = 0
    # Bonus workers
    if random.randint(0,100) < (nachhaltigkeit_ressourcen * 5):
        personal_total += 1
        bonus_worker += 1
    
    # Bonus Gluecksfelder
    bonus_gluecksfeld = 0
    if random.randint(0,100) < (nachhaltigkeit_ressourcen * 2):
        glueck_feld_anzahl += 1
        bonus_gluecksfeld += 1
   
    print("-- Nachhaltigkeit --")
    print("Personal investiert: " + str(personal) + "\n" +
        "Anzahl an Feldern: " + str(nachhaltigkeit_feld_anzahl) + "\n" +
        "Ressourcezahl: " + str(nachhaltigkeit_ressourcen) + "\n" +
        "Bonusglücksfeld: " + str(bonus_gluecksfeld) + "\n" +
        "Bonusworker: " + str(bonus_worker) + "\n")
    return

def forschung(geld, personal, felder_kaufen):
    global forschung_feld_anzahl 
    while geld > 5: 
        forschung_feld_anzahl += 1
        geld -= 5
    if personal == 0: 
        forschung = 0
    if personal == 1: 
        forschung = 0.25
    if personal == 2: 
        forschung = 0.4
    if personal == 3: 
        forschung = 0.5
    if personal == 4: 
        forschung = 0.55
    
    #################
    if (random.randint(0, 100) < forschung):
        switch_var = random.randint(0, 5)
        global glueck_verbesserung
        if switch_var == 1: 
            glueck_verbesserung = 1
        verbesserung = "Glueck + 5 Prozent"
        #if switch_var == 2: 

    print("-- Forschung und Entwicklung --")
    print("Personal investiert: " + str(personal) + "\n" +
        "Geld investiert: " + str(geld) + "\n" +
        "Erfolgswahrscheinlichkeit: " + str(forschung) + "\n" +
        "Verbesserung erhalten: " + "Glueck + 5 Prozent" + "\n")
    return



print("== DAY 1 ===\n")
maschinen(5,3,0)
glueck(5, 1, 1)
nachhaltigkeit(6, 3, 1)
rohstoffe(12,1,0)
forschung(9, 3, 1)
geld = produktion(1)

