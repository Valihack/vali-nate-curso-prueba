import random
import datetime

AVERAGE_LIFESPAN = 80
SMOKER_PENALIZATION = 5
DRINKER_PENALIZATION = 5
SEDENTARY_PENALIZATION = 10
SANFERMINES_PENALIZATION = 4

base_lifespan = AVERAGE_LIFESPAN/2 * random.random() + AVERAGE_LIFESPAN/2

print(base_lifespan)

def print_with_underscores(message):
    print(message)
    print(len(message) * "_")

def ask_yes_or_not(message):
    response = None
    print("s = si, n = no, m = a veces")
    while response != "s" and response != "n" and response != "m":
        response = input(message + "[s/n/m]")
    if response == "s":
        respuesta = 1
    if response == "m":
        respuesta = 0.5
    if response == "n":
        respuesta = 0


    return respuesta

print_with_underscores("Cuanto te queda de vida?")
print("Completa esta encuesta para saber cuantos años de vida te quedan")


birthdate = datetime.datetime.strptime(input("Cual es tu fecha de nacimiento(formato:dd/mm/yyyy)?"), "%d/%m/%Y")

penalization = 0

answer_smoke = ask_yes_or_not("Fumas?")
if answer_smoke > 0:
    penalization += SMOKER_PENALIZATION * answer_smoke

answer_drink = ask_yes_or_not("Bebes?")
if answer_drink > 0:
    penalization += DRINKER_PENALIZATION * answer_drink

answer_sedentary = ask_yes_or_not("Eres sedentario?")
if answer_sedentary > 0:
    penalization += SEDENTARY_PENALIZATION * answer_sedentary

answer_sanfermines = ask_yes_or_not("Corres en los San Fermines?")
if answer_sanfermines > 0:
    penalization += SANFERMINES_PENALIZATION * answer_sanfermines



lifespan = base_lifespan - penalization

death_date= birthdate + datetime.timedelta(days=365*lifespan)

days_to_death = death_date - datetime.datetime.now()

print("Te vas a morir el {}, te quedan {} dias".format(death_date.strftime("%d/%m/%Y"), days_to_death.days))