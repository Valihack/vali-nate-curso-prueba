from time import sleep
import datetime

NIGHT_STARTS = 19
NIGHT_ENDS = 8
HOUR_DURATION = 1

def write_file_and_screen(text, file_name):
    with open(file_name, "a") as hours_file:
        hours_file.write(text)
        print(text)

def traduccion_dia_semana(day):
    dicc_days = { 0 : "Domingo", 1 : "Lunes", 2 : "Martes", 3 : "Miércoles", 4 : "Jueves", 5 : "Viernes", 6 : "Sábado"}
    return dicc_days[day]

def main():
    if input("Deseas configurar una alarma?:  [s/n]") == "s":
        hora = int(input("Indica una hora [0/23]: "))
        dia_semana = int(input("Introduce los dias de la semana que quieres que suene [0/6]:"))
        try:
            dia_concreto = datetime.datetime.strptime(input("Introduce una fecha con este formato dd/mm/yyyy "), "%d/%m/%Y")
        except ValueError:
            dia_concreto = None

    current_time=datetime.datetime.now()
    is_night = False
    while True:
        sleep(HOUR_DURATION)
        current_time+= datetime.timedelta(hours=1)
        light_changed = False

        if (current_time.hour >= NIGHT_STARTS or current_time.hour <= NIGHT_ENDS) and not is_night:
            light_changed = True
            is_night = True
        elif (current_time.hour > NIGHT_ENDS and current_time.hour < NIGHT_STARTS) and is_night:
            light_changed = True
            is_night = False

        if hora >= 0:
            if dia_semana >= 0:
                if dia_concreto != None:
                    if hora == current_time.hour and dia_semana == current_time.weekday() and dia_concreto.date() == current_time.date():
                        texto = "Suena la alarma a las {}, dia {}, de {}\n".format(hora, traduccion_dia_semana(dia_semana), dia_concreto)
                        write_file_and_screen(texto, "horas.txt")
                elif hora == current_time.hour and dia_semana == current_time.weekday():
                    texto = "Suena la alarma a las {}, dia {}\n".format(hora, traduccion_dia_semana(dia_semana))
                    write_file_and_screen(texto, "horas.txt")
            elif hora == current_time.hour:
                texto = "Suena la alarma a las {}\n".format(hora)
                write_file_and_screen(texto, "horas.txt")

        if light_changed == True:
            if is_night == True:
                write_file_and_screen("Se ha hecho de noche\n", "horas.txt")
            else:
                write_file_and_screen("Se ha hecho de dia\n", "horas.txt")

        write_file_and_screen("La hora actual es {}\n".format(current_time), "horas.txt")

if __name__ == "__main__":
    main()