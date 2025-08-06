from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import json
from utils.scraper import extract_business_profile, get_industry_news
from utils.generator import generate_captions
from utils.planner import load_schedule, save_schedule
import os

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/business-profile", methods=["POST"])
def business_profile():
    data = request.get_json()
    profile = extract_business_profile(data["website"])
    return jsonify(profile)

@app.route("/api/industry-news", methods=["POST"])
def industry_news():
    data = request.get_json()
    news = get_industry_news(data["keywords"])
    return jsonify(news)

@app.route("/api/generate-posts", methods=["POST"])
def generate_posts():
    data = request.get_json()
    captions = generate_captions(data["profile"], data["news"], data["preferences"])
    save_schedule(captions)
    return jsonify(captions)

@app.route("/schedule", methods=["GET"])
def get_schedule():
    return jsonify(load_schedule())

@app.route("/schedule/<int:id>", methods=["PUT"])
def update_post(id):
    posts = load_schedule()
    data = request.get_json()
    for post in posts:
        if post["id"] == id:
            post["caption"] = data["caption"]
    save_schedule(posts)
    return jsonify({"status": "updated"})

@app.route("/schedule/<int:id>", methods=["DELETE"])
def delete_post(id):
    posts = load_schedule()
    posts = [post for post in posts if post["id"] != id]
    save_schedule(posts)
    return jsonify({"status": "deleted"})

@app.route("/fb/connect", methods=["POST"])
def fb_connect():
    return jsonify({"token": "mock_fb_token_123"})

@app.route("/fb/publish", methods=["POST"])
def fb_publish():
    data = request.get_json()
    return jsonify({"url": "https://facebook.com/page/post/xyz123"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
