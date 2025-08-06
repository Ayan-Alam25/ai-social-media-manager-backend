import random

TEMPLATES = {
    "Tips": ["Tip of the day: Stay ahead with {service}.", "Boost your business using {service}."],
    "Insights": ["Latest trend in {industry}: {news_title}", "Here’s what's happening in {industry}..."],
    "Offers": ["Special offer this week on {service}!", "Don't miss our {service} discount!"],
    "Greetings": ["Good morning from {name}!", "Wishing you a great day – from the {name} team!"]
}

def generate_captions(profile, news, prefs):
    captions = []
    for i in range(prefs["frequency"]):
        template = random.choice(TEMPLATES.get(prefs["type"], TEMPLATES["Tips"]))
        caption = template.format(
            name=profile["name"],
            industry=profile["industry"],
            service=random.choice(profile["services"]),
            news_title=random.choice(news)["title"] if news else "something big"
        )
        captions.append({"id": i+1, "day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"][i], "caption": caption})
    return captions
