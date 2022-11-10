import praw
import os
from dotenv import load_dotenv

load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv('API_CLIENT'),
    client_secret=os.getenv('API_SECRET'),
    password=os.getenv('REDDIT_PASSWORD'),
    user_agent="Winamp Music Bot for Reddit",
    username=os.getenv('REDDIT_USERNAME'),
)

target_sub = "artofml"
subreddit = reddit.subreddit(target_sub)
trigger_phrase = "!flair"

for comment in subreddit.stream.comments():  
    if trigger_phrase in comment.body:  
        word = comment.body.replace(trigger_phrase,"")
        author = comment.author
        subreddit.flair.set(author,text=word)
