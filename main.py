import asyncio
from social_media_handler import SocialMediaHandler

if __name__ == "__main__":
    handler = SocialMediaHandler()
    asyncio.run(handler.post_all())
