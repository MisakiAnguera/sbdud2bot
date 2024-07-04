# SBD-UD2-bot
Ejercicio de evaluación unidad 2. Bot de acceso a datos (obligatorio).

## Descripción del proyecto.
Código en Python3 de un bot de Telegram que consume algunas APIs, convierte archivos CSV en JSON y viceversa, practica *web scraping* y consulta una base de datos MySQL.

## Instrucciones para la ejecución de un contenedor de esta imagen.
* Generar en [{ NASA APIs }](https://api.nasa.gov/) un *API KEY* y guardarlo.
* Registrar un nuevo bot con @BotFather en Telegram cuyo *username*, que no *name*, debe terminar en «bot». Guardar el *token* generado durante el proceso.
* Ejecutar un contenedor con esta imagen. El parámetro `--rm` hará que se elimine el contenedor al acabar la ejecución. El *token* y el *api key* son los generados previamente. No se le está asignando ningún nombre al contenedor.
```
docker run --rm -e TOKEN=token_de_Telegram -e API_KEY=api_key_de_nasa misakirelo/sbdud2bot
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
* `/inferno` - Nivel de inferno e pecado cometido.
### Enlaces a los recursos elegidos.
* (1) Predición meteorolóxica diaria: https://meteo-estaticos.xunta.gal/datosred/infoweb/meteo/docs/rss/JSON_Pred_Concello_gl.pdf
* (3) Chistes: https://v2.jokeapi.dev/#getting-started
* (4) Proposta persoal: http://calapi.inadiutorium.cz/api-doc
* (7) Titulares dun diario electrónico: https://praza.gal
* (8) Carteleira: https://www.cantonescines.com/
* (9) Proposta persoal: https://www.vatican.va/special/rosary/documents/misteri_gaudiosi_sp.html, https://www.vatican.va/special/rosary/documents/misteri_luminosi_sp.html, https://www.vatican.va/special/rosary/documents/misteri_dolorosi_sp.html y https://www.vatican.va/special/rosary/documents/misteri_gloriosi_sp.html