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
    requests.post(url, json=payload)

def ejecutar_speedtest():
    try:
        resultado = subprocess.run(["speedtest-cli", "--simple"], capture_output=True, text=True)
        return resultado.stdout
    except Exception as e:
        return f"Error ejecutando speedtest: {e}"

if __name__ == "__main__":
    while True:
        print("Ejecutando test de velocidad...")
        resultado = ejecutar_speedtest()
        enviar_mensaje(f"📡 *Resultado Speedtest:*\n\n{resultado}")
        print("Resultado enviado a Telegram.")
        time.sleep(1800)  # Espera 30 minutos antes de volver a ejecutar
