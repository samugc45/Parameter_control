import random
import time
from twilio.rest import Client

#RELLENAR CREDENCIALES CON TU CUENTA DE TWILIO

#EN ESTE CASO, PARA EL ENVIO DEL AVISO SMS, USAMOS LA API DE TWILIO, PERO SE PUEDE USAR CUALQUIER OTRA

#PARÁMETROS DE SERVICIO A RELLENAR
TWILIO_SID = ''
TWILIO_AUTH_TOKEN = ''
TWILIO_TELEFONO = ''
MOVIL_TRABAJADORES = ['']  #TELÉFONOS DE AVISO DE TRABAJADORES



def enviar_sms(parametro, valor):
    """Envía un SMS a los trabajadores si hay una alerta."""
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for phone in MOVIL_TRABAJADORES:
        mensaje = f"[ALERTA] {parametro} fuera de rango: {valor:.1f}"
        client.messages.create(body=mensaje, from_=TWILIO_TELEFONO, to=phone)
        print(f"SMS enviado a {phone}: {mensaje}")



#LÍMITES DE ALERTA
TEMP_LIMITE = 30.0  # Temperatura máxima en °C
HUM_LIMITE = 70.0   # Humedad máxima en %


def registrar_datos(temp, hum):
    """Registra los datos en un archivo."""
    with open("datos_veterinario.csv", "a") as archivo:
        archivo.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')},{temp:.1f},{hum:.1f}\n")

def monitorear():
    """Simula la lectura y monitoreo de sensores."""
    while True:

        # Simular datos de sensores
        #CON ESTO GENERAMOS UNA SERIE DE DATOS DE TEMPERATRURA Y SENSORES QUE DEBERÍAN DE PROPORCIONAR SENSORES EN CASO REAL

        #temperatura = random.uniform(20.0, 40.0)
        #humedad = random.uniform(40.0, 90.0)

        temperatura = 35.7 
        humedad = 68  

        print(f"Temperatura: {temperatura:.1f}°C, Humedad: {humedad:.1f}%")
        registrar_datos(temperatura, humedad)

        #CUANDO LLAMAMOS A LA FUNCIÓN DE registrar_datos, SE ABRE EL FICHERO .CSV DONDE SE ALMACENAN ESOS DATOS

        # Verificar umbrales
        if temperatura > TEMP_LIMITE:
            enviar_sms("Temperatura", temperatura)
        if humedad > HUM_LIMITE:
            enviar_sms("Humedad", humedad)

        return 1

        time.sleep(2)  # Pausa de 5 segundos entre lecturas

if __name__ == "__main__":
    try:
        monitorear()
    except KeyboardInterrupt:
        print("\nMonitoreo detenido.")
