# ✨ Contributing to Ocoshy Bot

Thank you for your interest in contributing to **Ocoshy Bot**! Your contributions help improve our automation and AI-driven management across various social media platforms for OCOS.

This guide outlines clear instructions to contribute effectively.

---

## 🚀 **How to Contribute:**

### **1. Fork the Repository**

* Click the **Fork** button at the top right of the GitHub repository page.
* Clone your forked repository to your local machine:

```bash
git clone https://github.com/YOUR_USERNAME/ocoshy-bot.git
cd ocoshy-bot
```

### **2. Setup Your Development Environment**

* Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

* Install the required dependencies:

```bash
pip install -r requirements.txt
```

* Set up environment variables by creating a `.env` file based on the provided `.env.example`.

---

### **3. Create a Branch**

* Always create a new branch for your contributions based on the latest `main` branch:

```bash
git checkout main
git pull origin main
git checkout -b feature/your-feature-name
```

Branch naming conventions:

* `feature/<feature-name>` for new features
* `fix/<bug-name>` for bug fixes
* `docs/<document-update>` for documentation updates
* `test/<new-tests>` for tests improvements

---

### **4. Implement Your Changes**

* Make clear, structured, and readable code changes.
* Follow existing coding style (PEP 8 standards).
* Include comments where necessary.
* Ensure your code is self-explanatory and maintainable.

---

### **5. Commit Your Changes**

* Use clear, concise, and meaningful commit messages following the conventional commit format:

```bash
git commit -m "feat: add Twitter media upload support"
git commit -m "fix: resolve authentication bug on Instagram handler"
```

Common commit types:

| Type       | Description                                |
| ---------- | ------------------------------------------ |
| `feat`     | A new feature                              |
| `fix`      | A bug fix                                  |
| `docs`     | Documentation only changes                 |
| `refactor` | Code refactoring without new features      |
| `style`    | Formatting, missing semi-colons, etc.      |
| `test`     | Adding tests or updating existing tests    |
| `chore`    | Maintenance tasks (CI, dependency updates) |

---

### **6. Push Changes to GitHub**

Push your branch to GitHub:

```bash
git push origin feature/your-feature-name
```

---

### **7. Create a Pull Request (PR)**

After pushing your branch:

* Navigate to your GitHub fork.
* Click "Compare & pull request".
* Clearly describe your changes:

```markdown
## Description
Explain clearly what changes were made, why they were made, and how they improve the project.

## Related Issue(s)
Link to any issues that your PR addresses (e.g., "Fixes #24").

## Type of Change
- [ ] New Feature
- [ ] Bug Fix
- [ ] Documentation Update
- [ ] Code Refactor

## Testing Steps
Provide clear steps on how to test your feature or fix.
```

---

## ✅ **Review Process**

* Once your PR is submitted, maintainers will review your changes.
* You might receive comments or requests for changes. Promptly address these by making the required adjustments and pushing additional commits.
* After review approval, your PR will be merged into the main branch.

---

## ⚙️ **Code Style Guidelines**

* Follow **PEP 8** Python coding standards.
* Maintain consistent indentation (4 spaces, no tabs).
* Write clear and descriptive variable and function names.
* Document functions clearly with appropriate comments and docstrings.

Example:

```python
def fetch_twitter_metrics(api, account_id):
    """
    Fetches and returns recent engagement metrics from Twitter.

    Args:
        api (tweepy.Client): Initialized Tweepy client.
        account_id (str): The Twitter account ID to fetch metrics for.

    Returns:
        dict: Engagement metrics including likes, retweets, and replies.
    """
    # Implementation here
```

---

## 🧪 **Testing and Validation**

* Always test your changes locally.
* Add relevant test cases in the `tests/` directory.
* Use the following command to run all tests:

```bash
pytest tests/
```

Ensure all tests pass before pushing your changes.

---

## 💬 **Reporting Issues**

* Clearly describe the issue encountered.
* Provide steps to reproduce the issue.
* Include screenshots or log snippets when applicable.

---

## 📚 **Documentation**

* Keep documentation updated when introducing new features or changing existing functionality.
* Document your features clearly within README.md or within a separate document in `docs/`.

---

## 🙌 **Community Etiquette**

* Be respectful and kind to fellow contributors.
* Always adhere to GitHub’s Code of Conduct guidelines.
* Help newcomers by answering questions clearly.

---

## 📧 **Contact**

If you have specific questions or require additional assistance, please reach out via email:

* **OCOS Development Team:** [dev@ocos.io](mailto:dev@ocos.io)

---

Thank you again for your valuable contributions and support! Let's build together 🚀✨

**OCOS Team**
