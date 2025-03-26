FROM python:3.13.2

WORKDIR /app

COPY . .

EXPOSE 64352

# Salvando o host em uma variável de ambiente. Este host aceita conexões de qualquer IP na rede local:
ENV CLOUD_HOST=0.0.0.0

# Salvando a porta em uma variável de ambiente:
ENV CLOUD_PORT=64352

CMD ["python", "CloudExec.py"]
