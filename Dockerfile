#1. Requisitos
FROM python:latest

#2 Copiar os arquivos
RUN mkdir /app
WORKDIR /app
COPY myapp.py ./
COPY requirements.txt ./
RUN pip install -r requirements.txt
RUN python -m pip install ngrok

#3 Execute
CMD ["python", "myapp.py"]