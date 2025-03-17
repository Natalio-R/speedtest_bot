import subprocess
import requests
import time
import os

# Configuración desde variables de entorno
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def enviar_mensaje(mensaje):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": mensaje}
    response = requests.post(url, json=payload)
    print(f"Mensaje enviado: {response.status_code}")  # LOG para evitar inactividad

def ejecutar_speedtest():
    try:
        resultado = subprocess.run(["speedtest", "--format", "json"], capture_output=True, text=True)
        print(f"Resultado Speedtest:\n{resultado.stdout}")  # LOG para Render
        return resultado.stdout
    except Exception as e:
        print(f"Error ejecutando speedtest: {e}")  # LOG para Render
        return f"Error ejecutando speedtest: {e}"

if __name__ == "__main__":
    while True:
        print("Ejecutando test de velocidad...")  # LOG para Render
        resultado = ejecutar_speedtest()
        if resultado.strip():  # Solo envía si hay resultado
            enviar_mensaje(f"📡 *Resultado Speedtest:*\n\n{resultado}")
        else:
            enviar_mensaje("📡 *Resultado Speedtest:*\n\n⚠️ No se pudo obtener un resultado.")
        print("Esperando 30 minutos para el próximo test...")
        time.sleep(1800)  # 30 minutos