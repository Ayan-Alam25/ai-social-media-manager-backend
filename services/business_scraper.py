import requests
from bs4 import BeautifulSoup

def extract_business_profile(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract basic information
        name = soup.find('title').text if soup.find('title') else "Business Name"
        
        # Simple industry detection (you can expand this)
        industry = "General"
        if 'gym' in name.lower() or 'fitness' in name.lower():
            industry = "Fitness"
        elif 'salon' in name.lower() or 'hair' in name.lower():
            industry = "Beauty"
        elif 'cafe' in name.lower() or 'coffee' in name.lower():
            industry = "Food & Beverage"
            
        return {
            "name": name,
            "industry": industry,
            "services": ["Main Service 1", "Main Service 2"],  # Mock for now
            "tone": "professional"  # Default tone
        }
    except Exception as e:
        return {"error": str(e)}