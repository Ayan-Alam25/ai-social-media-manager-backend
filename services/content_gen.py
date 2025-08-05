import random

CONTENT_TEMPLATES = {
    "promo": {
        "professional": "We're excited to offer our valued customers [offer]. Available until [date]!",
        "witty": "Guess what? [offer] is happening! Your [body part] will thank you later.",
        "friendly": "Hey there! We've got something special for you - [offer]!"
    },
    "tip": {
        "professional": "Professional tip: [tip]. Implement this for better results.",
        "witty": "Here's a secret [industry] pros don't want you to know: [tip]",
        "friendly": "Quick tip from us to you: [tip]"
    },
    # Add more templates
}

def generate_content(business_profile, industry_news, preferences):
    posts = []
    tone = preferences.get('tone', 'professional')
    post_types = preferences.get('post_types', ['promo', 'tip', 'update'])
    num_posts = preferences.get('frequency', 3)
    
    for _ in range(num_posts):
        post_type = random.choice(post_types)
        template = CONTENT_TEMPLATES[post_type][tone]
        
        # Fill template with appropriate content
        if post_type == 'promo':
            content = template.replace('[offer]', f"20% off on {random.choice(business_profile['services'])}")
        elif post_type == 'tip':
            content = template.replace('[tip]', f"Always {random.choice(['book early', 'ask for recommendations', 'check reviews'])}")
        else:
            content = f"Industry update: {random.choice(industry_news)}"
            
        posts.append({
            "type": post_type,
            "content": content,
            "tone": tone
        })
    
    return posts