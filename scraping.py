import requests
from bs4 import BeautifulSoup
from datetime import date

def scraping_novas():
    url = "https://praza.gal"
    paxina = requests.get(url)
    soup = BeautifulSoup(paxina.content, 'html.parser')
    novas = soup.find_all('h2')
    response = ""
    for nova in novas:
        nova_text = nova.a.text.replace("\n","")
        nova_text = nova_text.replace("  ","")
        posible_response = response + f"[{nova_text}]({url + nova.a['href']})\n\n"
        if len(posible_response) > 4096: break
        response = posible_response
    return response

def scraping_carteleira():
    url = "https://www.cantonescines.com/"
    paxina = requests.get(url)
    soup = BeautifulSoup(paxina.content, 'html.parser')
    pelis = soup.findAll(class_="swiper-slide")
    response = ""
    promos = [h3s.text for promosliders in soup.findAll(class_="promoslider") for swiperslides in promosliders.findAll(class_="swiper-slide") for h3s in swiperslides.findAll("h3")]
    for peli in pelis:
        nombre = peli.find('h3').text
        if nombre in promos: continue
        nombre_enlace = f"[{nombre}]({peli.find('a')['href']})\n"
        if nombre_enlace in response: continue
        posible_response = response + nombre_enlace
        if len(posible_response) > 4096: break
        response = posible_response
    return response

def scraping_misterios():
    url = "https://www.vatican.va/special/rosary/documents/"

    weekday = date.today().weekday()
    if weekday in [0, 5]:
        url += "misteri_gaudiosi_sp.html"
    elif weekday == 3:
        url += "misteri_luminosi_sp.html"
    elif weekday in [1, 4]:
        url += "misteri_dolorosi_sp.html"
    elif weekday in [2, 6]:
        url += "misteri_gloriosi_sp.html"
    else:
        return False

    paxina = requests.get(url)
    soup = BeautifulSoup(paxina.content, 'html.parser')
    response = ""
    for misterio in soup.find("table").findAll("tr")[1].find("table").findAll("table")[1].findAll("tr"):
        for texto in misterio.findAll("td")[-1].findAll("font")[:2]:
            response += texto.text + "\n"
        response += "\n"
    return response
