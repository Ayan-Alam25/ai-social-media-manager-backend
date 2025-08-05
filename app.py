# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from services.business_scraper import extract_business_profile
from services.news_analyzer import get_industry_news
from services.content_gen import generate_content
from services.scheduler import schedule_posts
from services.facebook import connect_facebook_page

app = Flask(__name__)
CORS(app)

# In-memory storage for demo purposes
scheduled_posts = {}
facebook_connections = {}

@app.route('/api/business', methods=['POST'])
def business_profile():
    data = request.get_json()
    url = data.get('url')
    if not url:
        return jsonify({"error": "URL is required"}), 400
    
    profile = extract_business_profile(url)
    return jsonify(profile)

@app.route('/api/news', methods=['POST'])
def industry_news():
    data = request.get_json()
    industry = data.get('industry')
    if not industry:
        return jsonify({"error": "Industry is required"}), 400
    
    news = get_industry_news(industry)
    return jsonify({"news": news})

@app.route('/api/generate-content', methods=['POST'])
def generate_posts():
    data = request.get_json()
    
    business = data.get('business_profile')
    news = data.get('industry_news', [])
    preferences = data.get('preferences', {})
    
    posts = generate_content(business, news, preferences)
    return jsonify({"posts": posts})

@app.route('/api/schedule', methods=['POST'])
def schedule_content():
    data = request.get_json()
    
    posts = data.get('posts', [])
    frequency = data.get('frequency', 3)
    preferred_days = data.get('preferred_days')
    
    schedule = schedule_posts(posts, frequency, preferred_days)
    
    # Store in memory (in production, use a database)
    user_id = data.get('user_id', 'default_user')
    scheduled_posts[user_id] = schedule
    
    return jsonify({"schedule": schedule})

@app.route('/api/schedule/<user_id>', methods=['GET', 'PUT', 'DELETE'])
def manage_schedule(user_id):
    if user_id not in scheduled_posts:
        return jsonify({"error": "User not found"}), 404
    
    if request.method == 'GET':
        return jsonify({"schedule": scheduled_posts[user_id]})
    
    elif request.method == 'PUT':
        data = request.get_json()
        day = data.get('day')
        post_index = data.get('post_index')
        new_content = data.get('content')
        
        if day in scheduled_posts[user_id] and post_index < len(scheduled_posts[user_id][day]):
            scheduled_posts[user_id][day][post_index]['content'] = new_content
            return jsonify({"status": "updated"})
        return jsonify({"error": "Invalid day or index"}), 400
    
    elif request.method == 'DELETE':
        data = request.get_json()
        day = data.get('day')
        post_index = data.get('post_index')
        
        if day in scheduled_posts[user_id] and post_index < len(scheduled_posts[user_id][day]):
            del scheduled_posts[user_id][day][post_index]
            return jsonify({"status": "deleted"})
        return jsonify({"error": "Invalid day or index"}), 400

@app.route('/api/connect-facebook', methods=['POST'])
def connect_facebook():
    data = request.get_json()
    page_id = data.get('page_id')
    token = data.get('access_token')
    
    if not page_id or not token:
        return jsonify({"error": "Page ID and access token are required"}), 400
    
    result = connect_facebook_page(page_id, token)
    
    # Store connection (in production, use a database)
    user_id = data.get('user_id', 'default_user')
    facebook_connections[user_id] = result
    
    return jsonify(result)

@app.route('/api/publish', methods=['POST'])
def publish_posts():
    data = request.get_json()
    user_id = data.get('user_id', 'default_user')
    
    if user_id not in scheduled_posts:
        return jsonify({"error": "No posts scheduled"}), 400
    
    # In a real implementation, this would use Facebook's API to publish
    
    published = []
    for day, posts in scheduled_posts[user_id].items():
        for post in posts:
            published.append({
                "content": post['content'],
                "status": "published",
                "mock_link": f"https://facebook.com/mock_post/{hash(post['content'])}"
            })
    
    return jsonify({"published_posts": published})

if __name__ == '__main__':
    app.run(debug=True)