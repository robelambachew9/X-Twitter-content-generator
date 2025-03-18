import tweepy
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

# Authenticate with Twitter API (read-only)
auth = tweepy.OAuthHandler(os.getenv("API_KEY"), os.getenv("API_SECRET"))
auth.set_access_token(os.getenv("ACCESS_TOKEN"), os.getenv("ACCESS_TOKEN_SECRET"))
api = tweepy.API(auth)

def fetch_posts(accounts, days=7):
    end_date = datetime.utcnow()
    start_date = end_date - timedelta(days=days)
    posts = []

    for account in accounts:
        try:
            tweets = api.user_timeline(screen_name=account, count=100, tweet_mode="extended")
            for tweet in tweets:
                created_at = tweet.created_at
                if start_date <= created_at <= end_date:
                    posts.append({
                        "text": tweet.full_text,
                        "user": tweet.user.screen_name,
                        "date": created_at
                    })
        except Exception as e:
            print(f"Error fetching from {account}: {e}")
    
    return posts

if __name__ == "__main__":
    accounts = ["elonmusk", "wsj"]  # Example accounts
    posts = fetch_posts(accounts)
    for post in posts:
        print(f"@{post['user']}: {post['text']}")






