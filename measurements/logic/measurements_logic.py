from ..models import Measurement

#Consultar la lista de todas las medidas
def get_measurements():
    measurements= Measurement.objects.all()
    return measurements

#Consultar una medida dado su identificador
def get_measurement(mes_pk):
    measurement=Measurement.objects.get(pk=mes_pk)
    return measurement

#Crear una medida
def create_measurement(mes):
    measurement=Measurement(variable=mes["variable"],value=mes["value"],unit=mes["unit"],place=mes["place"],dateTime=mes["dateTime"])
    measurement.save()
    return measurement

#Cambiar una medida dado su identificador
def update_measurement(mes_pk,new_mes):
    measurement=get_measurement(mes_pk)
    measurement.variable= new_mes["variable"]
    measurement.value= new_mes["value"]
    measurement.unit= new_mes["unit"]
    measurement.dateTime= new_mes["dateTime"]
    measurement.place= new_mes["place"]
    measurement.save()
    return measurement

#Borrar una medida dado su identificador
def delete_measurement(mes_pk):
    measurement=Measurement.objects.get(pk=mes_pk)
    measurement.delete()