# sbdud2bot
Ejercicio de clase de un bot de acceso a datos.

## Descripción del proyecto.
Código en Python3 de un bot de Telegram que consume algunas APIs, convierte archivos CSV en JSON y viceversa, practica *web scraping* y consulta una base de datos MySQL.

### Enlaces a los recursos elegidos.
* (1) Predición meteorolóxica diaria: https://meteo-estaticos.xunta.gal/datosred/infoweb/meteo/docs/rss/JSON_Pred_Concello_gl.pdf
* (3) Chistes: https://v2.jokeapi.dev/#getting-started
* (4) Proposta persoal: http://calapi.inadiutorium.cz/api-doc
* (7) Titulares dun diario electrónico: https://praza.gal
* (8) Carteleira: https://www.cantonescines.com/
* (9) Proposta persoal: https://www.vatican.va/special/rosary/documents/misteri_gaudiosi_sp.html, https://www.vatican.va/special/rosary/documents/misteri_luminosi_sp.html, https://www.vatican.va/special/rosary/documents/misteri_dolorosi_sp.html y https://www.vatican.va/special/rosary/documents/misteri_gloriosi_sp.html


## Instrucciones para la ejecución del código.
* Crear un *environment* de Conda con versión de Python 3.9:
```
conda create -n nombre-environment python=3.9
```
* Activar el *environment*:
```
conda activate nombre-environment
```
* Instalar los paquetes del archivo `requirements.txt` (este comando debe ser ejecutado desde donde al ejectuar `ls` aparezca dicho archivo):
```
pip install -r requirements.txt
```
* Generar en [{ NASA APIs }](https://api.nasa.gov/) un *API KEY* y guardarlo.
* Registrar un nuevo bot con @BotFather en Telegram cuyo *username*, que no *name*, debe terminar en «bot». Guardar el *token* generado durante el proceso.
* Teniendo el *environment* activado, ejecutar el archivo `bot.py` (este comando debe ser ejecutado desde donde al ejecutar `ls` aparezca dicho archivo):
```
python3 bot.py
```
* Se puede, aunque no es necesario, editar los comandos del bot en Telegram para que este muestre un menú con los comandos disponibles. En BotFather: `/mybots`, se elige el bot en cuestión, `Edit Bot`, `Edit Commands` y se pega y envía el texto a continuación:
```
start - Command list.
tempo - Predición meteorolóxica do día.
imaxe - Imaxe do día.
joke - A joke.
calendar - Today.
novas - Novas de praza.gal.
carteleira - Carteleira de cantonescines.com.
misterios - Misterios de hoy.
inferno - Nivel de inferno e pecado cometido.
```
Para parar el bot, `Ctrl + C` donde se ejecuta.

Para desactivar el *environment* de conda, `conda deactivate`.

## Comandos disponibles.
* `/start` - Command list.
* `/tempo` - Predición meteorolóxica do día.
* `/imaxe` - Imaxe do día.
* `/joke` - A joke.
* `/calendar` - Today.
* Se puede enviar archivos CSV y JSON.
* `/novas` - Novas de praza.gal.
* `/carteleira` - Carteleira de cantonescines.com.
* `/misterios` - Misterios de hoy.
* `/inferno` - Nivel de inferno e pecado cometido. <mark>Ya no está disponible porque leía una base de datos levantada en una máquina en la nube de mi profesor temporal que ya no existe.</mark>

## *Dockerización* del proyecto.
* Poseer el archivo `Dockerfile` tal y como figura en este repositorio.
* Crear la imagen. En mi caso, le di por nombre `sbdud2bot`. Mi nombre de usuario es `misakirelo` y la etiqueta es `latest`. El comando se ejecuta donde sea que `ls` muestre el archivo `Dockerfile` junto con el resto de archivos (no ocultos) del repositorio.
```
docker build -t misakirelo/sbdud2bot:latest .
```
* El comando anterior habrá guardado la imagen en local. Crear y ejecutar un contenedor con dicha imagen:
```
docker run --rm -e TOKEN=token_de_Telegram -e API_KEY=api_key_de_NASA misakirelo/sbdud2bot
```
El *token* de Telegram y el *api key* de la NASA son personales. Fueron generados durante la ejecución del código.
* Se inicia sesión en [dockerhub](https://hub.docker.com/). Es necesario tener cuenta creada. Pedirá la contraseña, la cual hay que dar. Mi usuario es `misakirelo`.
```
docker login -u misakirelo
```
* Se publica la imagen en [dockerhub](https://hub.docker.com/). Al igual que antes, `misakirelo` se corresponde con mi nombre de usuario; `sbdud2bot`, con el nombre de mi imagen; y `latest`, con la etiqueta de la imagen.
```
docker image push misakirelo/sbdud2bot:latest
```
Ahora cualquier persona podrá crear un contenedor con mi imagen. Solo necesita un *token* de un bot de Telegram y un *api key* de la NASA.
```
docker run --rm -e TOKEN=token_de_Telegram -e API_KEY=api_key_de_NASA misakirelo/sbdud2bot
```
En [dockerhub](https://hub.docker.com/) se puede completar información sobre la imagen, en su *description* y *overview*.

### Mi imagen en Docker
[Enlace a la imagen de mi contenedor](https://hub.docker.com/r/misakirelo/sbdud2bot).