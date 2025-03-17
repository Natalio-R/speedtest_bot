import speedtest
import requests
import time
import os

# Configuración desde variables de entorno
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def enviar_mensaje(mensaje):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": mensaje, "parse_mode": "Markdown"}
    requests.post(url, json=payload)

def ejecutar_speedtest():
    try:
        st = speedtest.Speedtest()
        st.get_best_server()
        download = st.download() / 1_000_000  # Convertir a Mbps
        upload = st.upload() / 1_000_000  # Convertir a Mbps
        ping = st.results.ping

        return f"📡 *Resultado Speedtest:*\n\n🔹 *Ping:* {ping:.2f} ms\n⬇️ *Download:* {download:.2f} Mbps\n⬆️ *Upload:* {upload:.2f} Mbps"
    except Exception as e:
        print(f"Error ejecutando speedtest: {e}")
        return "📡 *Error ejecutando Speedtest.*"

if __name__ == "__main__":
    while True:
        print("Ejecutando test de velocidad...")
        resultado = ejecutar_speedtest()
        enviar_mensaje(resultado)
        print("Esperando 30 minutos para el próximo test...")
        time.sleep(1800)  # 30 minutos
