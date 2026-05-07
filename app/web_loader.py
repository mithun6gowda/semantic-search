import requests
from bs4 import BeautifulSoup

def fetch_text_from_url(url):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        paragraphs = soup.find_all("p")
        text = "\n".join([p.get_text().strip() for p in paragraphs if p.get_text().strip()])

        return text

    except Exception as e:
        print(f" Failed to fetch {url}: {e}")
        return ""