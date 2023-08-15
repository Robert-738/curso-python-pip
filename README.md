# Proyectos del Curso

#### Proyecto de Juego 
## Método 
Para correr el juego debes seguir las siguientes intrucciones en la terminal:

```sh
git clone

cd game

python3 main.py
```





#### Proyecto de App

## Método 1
Abrir desde Entorno Virtual
```sh
git clone

cd app

apt install python3.10-venv

python3 -m venv env

source env/bin/activate

pip3 install -r requeriments.txt

mkdir images

python3 main.py
```


## Método 2
Abrir desde Servidor Local mediante Contenedor Docker

Instalamos Docker desde Terminal
```sh
sudo apt-get update

sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

sudo mkdir -p /etc/apt/keyrings

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin

sudo service docker start

sudo docker run hello-world
```

Copiamos el Repositorio y lo Ejecutamos
```sh
git clone

cd app

sudo docker compose build

sudo docker compose up -d

sudo docker compose ps

sudo docker compose exec app-csv bash

python main.py
```







#### Proyecto request con HTTP
## Método 1
Ejecutar en terminal los comandos
```sh
git clone

cd web-server/

apt install python3.10-venv

python3 -m venv env

source env/bin/activate

pip3 install -r requeriments.txt

uvicorn main:app --reload
```

Abrir el servidor en el navegador web desde el siguiente link
```sh
localhost:8000
```

## Método 2

Abrir desde Servidor Local mediante Contenedor Docker

Instalamos Docker desde Terminal
```sh
sudo apt-get update

sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

sudo mkdir -p /etc/apt/keyrings

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin

sudo service docker start

sudo docker run hello-world
```

Copiamos el Repositorio y lo Ejecutamos
```sh
git clone

cd web-server

sudo docker compose build

sudo docker compose up -d

sudo docker compose ps
```


Abrir el servidor en el navegador web desde el siguiente link
```sh
localhost
```