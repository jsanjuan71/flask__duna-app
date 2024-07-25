FROM python:3.7

# Establece el directorio de trabajo en el directorio raíz de tu aplicación
WORKDIR /usr/src/app

# Clona el repositorio
RUN git clone https://github.com/jsanjuan71/flask__duna-app.git && \
    mv flask__duna-app/* ./ && \
    rm -rf flask__duna-app

# Instala las dependencias
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Ejecuta tu aplicación
CMD [ "python", "./web/app.py" ]

