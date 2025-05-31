import asyncio
import config
from analytics import generate_content

class SocialMediaHandler:
    def __init__(self):
        self.handles = config.SOCIAL_MEDIA_HANDLES

    async def twitter_post(self):
        from tweepy import Client
        client = Client(config.TWITTER_API_KEY)
        tweet = generate_content('twitter')
        client.create_tweet(text=tweet)
        print("✅ Tweet posted.")

    async def instagram_post(self):
        from instabot import Bot
        bot = Bot()
        bot.login(username=config.INSTAGRAM_USERNAME, password=config.INSTAGRAM_PASSWORD)
        caption, image = generate_content('instagram', media=True)
        bot.upload_photo(image, caption=caption)
        print("✅ Instagram photo posted.")

    async def telegram_post(self):
        import telebot
        bot = telebot.TeleBot(config.TELEGRAM_BOT_TOKEN)
        message = generate_content('telegram')
        bot.send_message(self.handles['telegram'], message)
        print("✅ Telegram message sent.")

    async def tiktok_post(self):
        from tiktokapi import TikTokApi
        api = TikTokApi(session_id=config.TIKTOK_SESSION_ID)
        caption, video = generate_content('tiktok', media=True)
        api.upload_video(video, caption)
        print("✅ TikTok video posted.")

    async def post_all(self):
        await asyncio.gather(
            self.twitter_post(),
            self.instagram_post(),
            self.telegram_post(),
            self.tiktok_post()
        )
