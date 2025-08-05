def schedule_posts(posts, frequency=3, preferred_days=None):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    if preferred_days:
        # Filter to only include preferred days that exist
        available_days = [day for day in preferred_days if day in days]
        if available_days:
            days = available_days
    
    # Distribute posts evenly across available days
    scheduled = {}
    for i, post in enumerate(posts):
        day = days[i % len(days)]
        if day not in scheduled:
            scheduled[day] = []
        scheduled[day].append(post)
    
    return scheduled