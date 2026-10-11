"""
Scraper del laboratorio Week 1 Day 1.

Basato su scraper.py del corso di Ed Donner:
https://github.com/ed-donner/llm_engineering/blob/main/week1/scraper.py
"""

from bs4 import BeautifulSoup
import requests


# Header che fa sembrare la richiesta quella di un browser Chrome:
# alcuni siti rifiutano le richieste che non arrivano da un browser.
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}


def fetch_website_contents(url):
    """
    Restituisce titolo e testo leggibile della pagina all'indirizzo url,
    tagliati a 2.000 caratteri per contenere tempi e costi.
    """
    # 1. Scarica la pagina
    response = requests.get(url, headers=headers)

    # 2. Trasforma l'HTML in una struttura esplorabile
    soup = BeautifulSoup(response.content, "html.parser")

    # 3. Prende il titolo, se c'è
    title = soup.title.string if soup.title else "No title found"

    if soup.body:
        # 4. Cancella le parti inutili per un riassunto
        for irrelevant in soup.body(["script", "style", "img", "input"]):
            irrelevant.decompose()
        # 5. Estrae solo il testo, una riga per elemento
        text = soup.body.get_text(separator="\n", strip=True)
    else:
        text = ""

    # 6. Taglia a 2.000 caratteri
    return (title + "\n\n" + text)[:2_000]


def fetch_website_links(url):
    """
    Restituisce i link presenti nella pagina (non usato nel Day 1).
    """
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    links = [link.get("href") for link in soup.find_all("a")]
    return [link for link in links if link]
