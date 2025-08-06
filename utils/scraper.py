import requests
from bs4 import BeautifulSoup

def extract_business_profile(website_url):
    try:
        response = requests.get(website_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string if soup.title else "Unknown"
        paragraphs = soup.find_all('p')
        about_text = ' '.join(p.get_text() for p in paragraphs[:5])
        return {
            "name": title.strip(),
            "industry": "Tech",
            "services": ["AI Services", "Analytics"],
            "tone": "Friendly" if "welcome" in about_text.lower() else "Professional"
        }
    except:
        return {"error": "Unable to extract profile"}

def get_industry_news(keywords):
    return [
        {"title": "AI in Marketing", "url": "https://example.com/ai1"},
        {"title": "Tech News 2025", "url": "https://example.com/tech"},
        {"title": "Automation Trends", "url": "https://example.com/auto"}
    ]
