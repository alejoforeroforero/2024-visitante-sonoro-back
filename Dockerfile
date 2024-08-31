# Dockerfile
FROM python:3.9

# Establecer variables de entorno
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Establecer directorio de trabajo
WORKDIR /

# Instalar pipenv
RUN pip install pipenv

# Copiar Pipfile y Pipfile.lock
COPY Pipfile Pipfile.lock ./

# Instalar dependencias
RUN pipenv install --system --deploy --ignore-pipfile

# Copiar el proyecto
COPY . .

# Exponer el puerto 8000
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]