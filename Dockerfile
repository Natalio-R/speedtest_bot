FROM python:3.9

# Instalar dependencias necesarias
RUN apt-get update && apt-get install -y curl gnupg

# Agregar clave GPG de Speedtest
RUN curl -fsSL https://packagecloud.io/ookla/speedtest-cli/gpgkey | tee /usr/share/keyrings/speedtest-keyring.asc > /dev/null

# Agregar repositorio oficial
RUN echo "deb [signed-by=/usr/share/keyrings/speedtest-keyring.asc] https://packagecloud.io/ookla/speedtest-cli/debian/ bullseye main" | tee /etc/apt/sources.list.d/speedtest.list

# Instalar Speedtest CLI oficial
RUN apt-get update && apt-get install -y speedtest

# Configurar directorio de trabajo
WORKDIR /app

# Copiar archivos
COPY speedtest_bot.py .

# Instalar dependencias de Python
RUN pip install requests

# Ejecutar el script
CMD ["python", "speedtest_bot.py"]
