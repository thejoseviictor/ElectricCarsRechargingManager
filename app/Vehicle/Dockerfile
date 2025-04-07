# Repositório: macedoxx2000/vehicle:lastest

# Imagem base para a "build" da imagem atual
FROM python:3.13.2 

# Define o diretório principal
WORKDIR /app

# Copia o projeto inteiro, respeitando o .dockerignore
COPY . .

# Instala dependências (se houver um requirements.txt)
# RUN pip install --no-cache-dir -r requirements.txt

# Define a porta que o container deve expor
# EXPOSE 64352

# Define os comandos e parâmetros
CMD ["python", "app/main.py"]