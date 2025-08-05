import requests
from bs4 import BeautifulSoup

def get_industry_news(industry):
    # Mock implementation using Google News RSS
    try:
        query = industry.replace(' ', '+')
        url = f"https://news.google.com/rss/search?q={query}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'xml')
        
        items = soup.find_all('item')[:5]  # Get top 5 news items
        headlines = [item.title.text for item in items]
        
        return headlines
    except:
        # Fallback mock data
        mock_news = {
            "Fitness": [
                "New study reveals benefits of morning workouts",
                "Top 5 fitness trends for 2023",
                "How gyms are adapting to post-pandemic needs"
            ],
            "Beauty": [
                "Latest hair color trends for summer",
                "Eco-friendly salon practices gaining popularity",
                "New skincare ingredients to watch"
            ],
            # Add more industries as needed
        }
        return mock_news.get(industry, ["Industry news 1", "Industry news 2", "Industry news 3"])