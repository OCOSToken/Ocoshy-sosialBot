# 🛠️ Ocoshy Bot – Troubleshooting Guide

Welcome to the Ocoshy Bot troubleshooting guide. This document provides detailed solutions for resolving common issues encountered during bot setup and operation.

---

## 🔴 **General Troubleshooting Steps**

Before diving into specific errors, follow these initial diagnostic steps:

* Ensure all dependencies are correctly installed.

  ```bash
  pip install -r requirements.txt
  ```
* Verify your `.env` file contains accurate credentials.
* Ensure that your internet connection is stable.
* Check your firewall settings to avoid network blockage.

---

## 🚨 **Common Errors & Detailed Solutions**

### **1. Environment Variable Issues**

**Problem:**
The bot fails to load credentials or produces authentication errors.

**Solution:**

* Verify `.env` file formatting (no spaces around `=` sign).
* Ensure the `.env` file is in the root project directory.
* Reload environment variables:

  ```bash
  source venv/bin/activate
  ```
* Print environment variables for debugging:

  ```python
  import os
  print(os.getenv("OPENAI_API_KEY"))
  ```

---

### **2. Dependency Installation Errors**

**Problem:**
Errors occur while installing packages with pip.

**Solution:**

* Upgrade `pip` and setuptools:

  ```bash
  pip install --upgrade pip setuptools
  ```
* If using Python virtual environments, activate before installation:

  ```bash
  source venv/bin/activate
  ```
* Clear cache if persistent errors occur:

  ```bash
  pip cache purge
  ```

---

### **3. OpenAI API Issues**

**Problem:**
OpenAI API fails or returns authentication errors.

**Solution:**

* Confirm that the API key is valid and properly set in `.env`.
* Check API quota limits in your OpenAI account.
* Test OpenAI API directly via curl or Postman:

  ```bash
  curl https://api.openai.com/v1/models \
    -H "Authorization: Bearer YOUR_API_KEY"
  ```

---

## 📱 **Platform-Specific Troubleshooting**

### ✅ **Twitter API Issues (Tweepy)**

**Problem:**
Bot fails to post tweets or authenticate.

**Solution:**

* Ensure API keys have correct permissions (`Read/Write` access).
* Re-create API credentials from Twitter Developer Portal.
* Debug using Tweepy API client directly:

  ```python
  import tweepy
  client = tweepy.Client("YOUR_API_KEY")
  response = client.create_tweet(text="Test tweet")
  print(response)
  ```

---

### ✅ **Instagram Authentication Issues (Instabot)**

**Problem:**
Login failures or account blocking warnings.

**Solution:**

* Confirm credentials in `.env` file are correct.
* Instagram may block frequent logins; wait and retry after a cooldown period.
* Use a fresh cookie or session file:

  ```bash
  rm -rf config
  ```
* Avoid rapid or frequent postings (maintain intervals).

---

### ✅ **Telegram Bot Connectivity**

**Problem:**
Telegram messages are not being sent or received.

**Solution:**

* Verify your bot token in the `.env` file.
* Test bot manually using Telegram Bot API:

  ```bash
  curl https://api.telegram.org/bot<token>/getMe
  ```
* Ensure the bot is properly added to the intended group/channel with admin rights if required.

---

### ✅ **TikTok Video Upload Issues**

**Problem:**
Uploading videos to TikTok fails repeatedly.

**Solution:**

* Ensure your TikTok session ID is valid and up-to-date.
* Confirm video file format is supported (`mp4`, under 60 seconds recommended).
* Manually test TikTok API calls and verify session:

  ```python
  from TikTokApi import TikTokApi
  api = TikTokApi(session_id='your_session_id')
  user = api.user(username='ocos_official')
  print(user.info())
  ```

---

## 📄 **Log Management & Debugging Practices**

To effectively track and debug your bot's activity, follow these best practices:

### 📌 **Enable Detailed Logging**

Use `loguru` for structured logging:

```python
from loguru import logger

logger.add("ocoshy_bot.log", rotation="10 MB", retention="7 days")

logger.info("Bot started successfully.")
logger.error("An error occurred: {}", error_detail)
```

### 📌 **Log File Locations**

* Default log file: `ocoshy_bot.log` (root directory)
* Rotate logs regularly to maintain manageable size.

---

## 🐞 **How to Report Bugs**

When reporting issues, include detailed information:

* **Short summary of the problem**
* **Detailed steps to reproduce the issue**
* **Error logs or screenshots**
* **Operating system and Python version**
* **Dependency versions (`pip freeze`)**

Example issue report format:

```markdown
### Summary:
Unable to authenticate Twitter API using Tweepy.

### Steps to Reproduce:
1. Configure `.env` file with Twitter API credentials.
2. Run `python src/main.py`.

### Expected Result:
Successful tweet posted to the OCOS Twitter account.

### Actual Result:
Authentication error: "Invalid or expired token."

### Logs:
[Paste logs here]

### Environment:
- Python 3.12
- Tweepy 4.14.0
- Ubuntu 22.04 LTS
```

---

## 🔒 **Security & Best Practices**

### 📍 **Securely Managing Credentials**

* **Never commit `.env` or sensitive data** to GitHub. Use `.gitignore` explicitly.
* Rotate API keys periodically.
* Use environment-specific keys (development vs. production).

---

## ❓ **Additional Resources**

* Official OpenAI documentation: [OpenAI API Docs](https://platform.openai.com/docs/)
* Tweepy documentation: [Tweepy Docs](https://docs.tweepy.org/)
* Instabot guidelines: [Instabot GitHub](https://github.com/instabot-py/instabot.py)
* Telegram Bot API docs: [Telegram Bot API](https://core.telegram.org/bots/api)
* TikTok API Documentation: [TikTok API](https://github.com/davidteather/TikTok-Api)

---

## 📬 **Further Support**

If you continue experiencing issues after following this guide, please reach out to our support team via email:

📧 **Support Email:** [support@ocos.io](mailto:support@ocos.io)

---

Thank you for using Ocoshy Bot! Your feedback helps us improve continuously.

**– OCOS Development Team** 🚀
