FROM python:3.9

# Instalar cliente oficial de Speedtest
RUN apt-get update && apt-get install -y curl && \
    curl -s https://install.speedtest.net/app/cli/install.deb.sh | bash && \
    apt-get install -y speedtest

# Configurar el directorio de trabajo
WORKDIR /app

# Copiar archivos
COPY speedtest_bot.py .

# Instalar dependencias
RUN pip install requests

# Ejecutar script
CMD ["python", "speedtest_bot.py"]
