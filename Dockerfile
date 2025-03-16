FROM python:3.9

# Instalar Speedtest CLI
RUN apt-get update && apt-get install -y speedtest-cli

# Configurar el directorio de trabajo
WORKDIR /app

# Copiar archivos
COPY speedtest_bot.py .

# Instalar dependencias
RUN pip install requests

# Ejecutar script
CMD ["python", "speedtest_bot.py"]
