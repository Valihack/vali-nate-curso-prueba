import datetime
import calendar

def traducir (dia):
    diccionario_dias={'Monday':'Lunes','Tuesday':'Martes','Wednesday':'Miércoles','Thursday':'Jueves','Friday':'Viernes', 'Saturday':'Sábado', 'Sunday':'Domingo'}
    return diccionario_dias[dia]

hoy=datetime.datetime.now()

dia=int(input("Di el dia de tu cumpleaños: "))
mes=int(input("Di el mes de tu cumpleaños (numericamente): "))
ano=hoy.year
dia_cumpleanos=datetime.datetime(day=dia, month=mes, year=ano )
if dia_cumpleanos < hoy:
    dia_cumpleanos=datetime.datetime(day=dia, month=mes, year=ano+1)


restante=dia_cumpleanos-hoy
dia_semana=str(traducir(calendar.day_name[dia_cumpleanos.weekday()]))
print("Faltan {} dias y caerá en {}".format(int(restante.total_seconds() / 86400), dia_semana))