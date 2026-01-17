from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
url = "https://en.wikipedia.org/wiki/"
def web_search(topic: str) -> str:
    """Perform a web search for the given topic on Wikipedia."""
    try:
        url= "https://en.wikipedia.org/wiki/"
        req= Request(
            url + topic.replace(' ', '_'), 
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
            )
        html=urlopen(req, timeout=10).read()
        soup =BeautifulSoup(html, 'html.parser')
        paragraphs= soup.find_all('p')
        content= ' '.join([para.get_text() for para in paragraphs[:3]])
        return f"Search results for {topic}: {content}"
    except Exception as e:
        return f"An error occurred while fetching the search results: {e}"