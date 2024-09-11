FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install gunicorn

COPY . .

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "api.wsgi:application"]