
import datetime

AVERAGE_LIFESPAN = 80
SMOKER_PENALIZATION = 10
DRINKER_PENALIZATION = 10
SEDENTARY_PENALIZATION = 20


def print_with_underscores(message):
    print(message)
    print(len(message) * "_")

def ask_yes_or_not(message):
    response = None
    while response != "s" and response != "n":
        response = input(message + "[s/n]")
    return response == "s"

print_with_underscores("Cuanto te queda de vida?")
print("Completa esta encuesta para saber cuantos años de vida te quedan")


birthdate = datetime.datetime.strptime(input("Cual es tu fecha de nacimiento(formato:dd/mm/yyyy)?"), "%d/%m/%Y")


penalization = 0

if ask_yes_or_not("Fumas?"):
    penalization += SMOKER_PENALIZATION
if ask_yes_or_not("Bebes?"):
    penalization += DRINKER_PENALIZATION
if not ask_yes_or_not("Haces deporte?"):
    penalization += SEDENTARY_PENALIZATION


lifespan = AVERAGE_LIFESPAN - penalization

death_date= birthdate + datetime.timedelta(days=365*lifespan)

days_to_death = death_date - datetime.datetime.now()

print("Te vas a morir el {}, te quedan {} dias".format(death_date.strftime("%d/%m/%Y"), days_to_death.days))
