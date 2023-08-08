import requests
from bs4 import BeautifulSoup

url = "https://www.idealista.com/en/buscar/venta-viviendas/con-publicado_ultima-semana/Benidorm/?ordenado-por=precios-asc"

try:
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, "html.parser")
    links = soup.find_all("a", class_="item-link")


    for i in range(min(3, len(links))):
        print(links[i]['href'])

except requests.exceptions.RequestException as e:
    print(f"Error: {e}")