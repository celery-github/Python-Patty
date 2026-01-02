# Python Hello World Web App (Flask)

A minimal Python web app that serves a **Hello, World!** webpage using Flask.  
Includes automated checks with **GitHub Actions CI** (linting + tests).

## ✅ Features
- Flask web server serving a simple homepage
- Basic test coverage using `pytest`
- Linting with `flake8`
- CI runs on every push / pull request (Python 3.11 + 3.12)

## 🗂 Project Structure
```text
.
├── src/
│   ├── __init__.py
│   └── app.py
├── tests/
│   └── test_app.py
├── requirements.txt
├── requirements-dev.txt
├── .flake8
└── .github/workflows/ci.yml
