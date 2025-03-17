import subprocess
import requests
import time
import os
import json

# Configuración desde variables de entorno
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def enviar_mensaje(mensaje):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": mensaje, "parse_mode": "Markdown"}
    response = requests.post(url, json=payload)
    print(f"Mensaje enviado: {response.status_code}")  # LOG para Render

def ejecutar_speedtest():
    try:
        resultado = subprocess.run(["speedtest", "--format", "json"], capture_output=True, text=True)
        datos = json.loads(resultado.stdout)
        ping = datos["ping"]["latency"]
        download = datos["download"]["bandwidth"] / 125000  # Convertir a Mbps
        upload = datos["upload"]["bandwidth"] / 125000  # Convertir a Mbps

        return f"📡 *Resultado Speedtest:*\n\n🔹 *Ping:* {ping} ms\n⬇️ *Download:* {download:.2f} Mbps\n⬆️ *Upload:* {upload:.2f} Mbps"
    except Exception as e:
        print(f"Error ejecutando speedtest: {e}")  # LOG para Render
        return "📡 *Error ejecutando Speedtest.*"

if __name__ == "__main__":
    while True:
        print("Ejecutando test de velocidad...")  # LOG para Render
        resultado = ejecutar_speedtest()
        enviar_mensaje(resultado)
        print("Esperando 30 minutos para el próximo test...")
        time.sleep(1800)  # 30 minutos
