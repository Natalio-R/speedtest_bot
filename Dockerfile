FROM python:3.9

# Configurar directorio de trabajo
WORKDIR /app

# Copiar archivos
COPY speedtest_bot.py .

# Instalar dependencias
RUN pip install requests speedtest-cli

# Ejecutar el script
CMD ["python", "speedtest_bot.py"]