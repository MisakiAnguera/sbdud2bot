import requests
import os

def api_tempo():
    endpoint = "https://servizos.meteogalicia.gal/mgrss/predicion/jsonPredConcellos.action"
    response = requests.get(endpoint, params={"idConc":"15030"})
    hoxe = response.json()["predConcello"]["listaPredDiaConcello"][0]
    ceos = {"-9999":"Non dispoñible",
            "101":"Despexado",
            "102":"Nubes altas",
            "103":"Nubes e claros",
            "104":"Anubrado 75%",
            "105":"Cuberto",
            "106":"Néboas",
            "107":"Chuvasco",
            "108":"Chuvasco (75%)",
            "109":"Chuvasco neve",
            "110":"Orballo",
            "111":"Choiva",
            "112":"Neve",
            "113":"Treboada",
            "114":"Brétema",
            "115":"Bancos de néboa",
            "116":"Nubes medias",
            "117":"Choiva débil",
            "118":"Chuvascos débiles",
            "119":"Treboada con poucas nubes",
            "120":"Auga neve",
            "121":"Sarabia"}
    return f"Predición meteorolóxica de hoxe do municipio da Coruña. Temperatura mínima: {hoxe['tMin']}ºC. Temperatura máxima: {hoxe['tMax']}ºC. {ceos[str(hoxe['ceo']['tarde'])]}."

def api_imaxe():
    endpoint = "https://api.nasa.gov/planetary/apod"
    API_KEY = os.getenv('API_KEY')
    if API_KEY == None:
        print('Lembra indicar a variable API_KEY.')
        print('p. ex.: docker run --rm -e TOKEN=o_teu_token -e API_KEY=a_túa_API_KEY nomebot')
        exit(1)
    image_url = requests.get(endpoint, params={"api_key":API_KEY}).json()["url"]
    img_data = requests.get(image_url).content
    with open('imaxedodia.jpg', 'wb') as handler:
        handler.write(img_data)

def api_joke():
    endpoint = "https://v2.jokeapi.dev/joke/Any"
    return requests.get(endpoint, params={"type":"single"}).json()["joke"]

def api_calendar():
    endpoint = "http://calapi.inadiutorium.cz/api/v0/en/calendars/general-en/today"
    today = requests.get(endpoint).json()
    day = today["date"]
    season = today["season"]
    response = "Date: " + day + "\n"
    response += season.capitalize()+" season\nCelebrations:\n"
    celebrations = today["celebrations"]
    for celebration in celebrations:
        response += "* " + celebration["title"] + ".\n"
        response += "    - " + celebration["colour"].capitalize() + " colour\n"
        response += "    - " + celebration["rank"].capitalize() + " rank\n"
    return response