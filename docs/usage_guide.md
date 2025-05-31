# Ocoshy Bot – Detailed Usage Guide

Welcome to the comprehensive usage guide for **Ocoshy Bot**, designed to automate and intelligently manage OCOS's presence across multiple social media platforms using advanced AI-driven technologies.

---

## 🚀 Getting Started

### Overview

**Ocoshy Bot** is a powerful automation tool designed to handle OCOS social media content across platforms such as Twitter, Instagram, Telegram, and TikTok. It automatically generates engaging, relevant, and timely posts powered by OpenAI's GPT technology.

### Prerequisites

* Python 3.10 or higher installed
* API keys/accounts for Twitter, Instagram, Telegram, and TikTok
* OpenAI GPT API key
* Basic understanding of command-line operations

---

## 🌐 Supported Platforms

**Ocoshy Bot** currently supports:

* **Twitter:** Automated tweeting and analytics.
* **Instagram:** Posting photos with AI-generated captions.
* **Telegram:** Automated group/channel messaging.
* **TikTok:** AI-generated video content and uploading.

---

## 🛠️ Configuring the Bot

### Setting Up the `.env` File

Create a `.env` file in the project's root directory and populate it with your credentials:

```env
OPENAI_API_KEY=your_openai_key
TWITTER_API_KEY=your_twitter_key
INSTAGRAM_USERNAME=your_instagram_username
INSTAGRAM_PASSWORD=your_instagram_password
TELEGRAM_BOT_TOKEN=your_telegram_token
TIKTOK_SESSION_ID=your_tiktok_session_id
```

### Environment Variables Explained

* **`OPENAI_API_KEY`:** API key from OpenAI used for content generation.
* **`TWITTER_API_KEY`:** API key obtained from Twitter Developer Portal.
* **`INSTAGRAM_USERNAME` & `INSTAGRAM_PASSWORD`:** Credentials for your OCOS Instagram account.
* **`TELEGRAM_BOT_TOKEN`:** Token for your OCOS Telegram Bot.
* **`TIKTOK_SESSION_ID`:** Session ID from your logged-in TikTok account for API access.

---

## 🖥️ Running the Bot

### Local Execution

Activate your virtual environment and run:

```bash
source venv/bin/activate  # Windows: venv\Scripts\activate
python src/main.py
```

This command triggers automated posting on all configured platforms simultaneously.

### Scheduling Posts

To run the bot periodically (e.g., every hour), use scheduling tools like `cron` (Linux/Mac) or Task Scheduler (Windows).

Example with cron:

```cron
0 * * * * /path/to/venv/bin/python /path/to/ocoshy-bot/src/main.py
```

### Logs and Outputs

All actions and errors are logged. Check your console or log files regularly to ensure smooth operation and quick debugging.

---

## 📈 Analytics and Reporting

Ocoshy Bot generates AI-driven content based on real-time social media analytics.

* **Content Analytics:** Automated measurement of engagement metrics such as likes, shares, comments, and reach.
* **Performance Tracking:** Identify successful content strategies and optimize future posts based on data insights.

---

## ⚙️ Customizing Content Generation

Modify content prompts for each platform directly in the `analytics.py` file:

Example customization:

```python
prompt = "Create a professional and engaging post about OCOS recent blockchain updates for Twitter."
response = openai.ChatCompletion.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": prompt}]
)
```

Adjust prompts to better align with your content strategy.

---

## 🧩 Advanced Usage Tips

* **Platform-specific Customization:** Enhance engagement by tailoring your content separately for each platform's audience.
* **Error Handling:** Regularly review logs for potential API limitations or credential issues and implement retry mechanisms.
* **Security:** Regularly rotate your API keys and credentials. Always secure your `.env` file appropriately.

---

## 📚 Additional Resources

* [Official OpenAI API Documentation](https://platform.openai.com/docs/api-reference)
* [Twitter Developer Portal](https://developer.twitter.com/)
* [Instagram Automation Best Practices](https://instagrambot.github.io/docs/)
* [Telegram Bot API Documentation](https://core.telegram.org/bots/api)
* [TikTok API Integration](https://github.com/davidteather/TikTok-Api)

---

This comprehensive guide ensures that you can fully leverage **Ocoshy Bot** to effectively manage and grow your OCOS social media presence professionally and efficiently.

For further support or inquiries, please contact: **[dev@ocos.io](mailto:dev@ocos.io)**
