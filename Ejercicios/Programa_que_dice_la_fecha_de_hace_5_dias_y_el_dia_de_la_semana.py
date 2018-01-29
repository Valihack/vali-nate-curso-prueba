import datetime
import calendar

def traducir (dia):
    diccionario_dias={'Monday':'Lunes','Tuesday':'Martes','Wednesday':'Miércoles','Thursday':'Jueves','Friday':'Viernes', 'Saturday':'Sábado', 'Sunday':'Domingo'}
    return diccionario_dias[dia]

hoy=datetime.datetime.now()
dias_retroceden=datetime.timedelta(days=5)
hace_5_dias=hoy-dias_retroceden
dia_semana=str(traducir(calendar.day_name[hace_5_dias.weekday()]))


print("Hace 5 dias fue {}, cayó en {} ".format(hace_5_dias.day, dia_semana))
