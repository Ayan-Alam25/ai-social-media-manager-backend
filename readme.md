# AI Social Media Manager Backend

A Flask-based backend system for an AI agent that creates and manages Facebook content for businesses. The system scrapes business websites, analyzes industry trends, generates engaging posts, and schedules them for publication.

## Features

1. **Business Understanding API** - Extracts business profile from a website URL
2. **Industry News Analyzer** - Fetches relevant industry news
3. **Content Generator** - Creates social media posts in different tones/styles
4. **Weekly Planner** - Schedules posts based on preferred frequency
5. **Preview & Edit** - Allows reviewing and modifying scheduled posts
6. **Facebook Integration** - Simulates connection and publishing to FB pages

## Tech Stack

- Python 3.7+
- Flask (Backend framework)
- BeautifulSoup4 (Web scraping)
- Flask-CORS (Cross-origin support)
- Requests (HTTP calls)

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Ayan-Alam25/ai-social-media-manager-backend.git
   cd ai-social-media-manager-backend
   ```

2. **Create and activate virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install requirements**:
    ```bash
    pip install -r requirements.txt
    ```
4. **Run the app**
    ```bash
    python app.py
    ```

The server will start at http://localhost:5000