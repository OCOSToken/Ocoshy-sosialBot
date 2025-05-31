import openai
import config

openai.api_key = config.OPENAI_API_KEY

def generate_content(platform, media=False):
    prompt = f\"\"\"Generate highly engaging and optimized content specifically for OCOS's {platform} account.\"\"\"

    if media:
        # Media file paths placeholder
        media_path = "media/sample.jpg" if platform != 'tiktok' else "media/sample.mp4"
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        caption = response.choices[0].message.content.strip()
        return caption, media_path

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()
