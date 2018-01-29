import datetime

dia=int(input("Introduce el dia: "))
mes=int(input("Introduce el dmes: "))
ano=int(input("Introduce el año: "))

hoy=datetime.datetime.now()

dia_cualquiera=datetime.datetime(day=dia, month=mes, year=ano)

if hoy<dia_cualquiera:
    print("El futuro no ha llegado!")
else:
    tiempo_total=hoy - dia_cualquiera
    print("Han pasado un total de {} horas".format(int(tiempo_total.total_seconds()/3600)))