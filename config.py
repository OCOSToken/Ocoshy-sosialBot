import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
OCOS_O47_API_KEY = os.getenv('OCOS_O47_API_KEY')

TWITTER_API_KEY = os.getenv('TWITTER_API_KEY')
INSTAGRAM_USERNAME = os.getenv('INSTAGRAM_USERNAME')
INSTAGRAM_PASSWORD = os.getenv('INSTAGRAM_PASSWORD')
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TIKTOK_SESSION_ID = os.getenv('TIKTOK_SESSION_ID')

SOCIAL_MEDIA_HANDLES = {
    'twitter': 'ocos_username',
    'instagram': 'ocos_username',
    'telegram': '@ocos_username',
    'tiktok': '@ocos_username'
}
