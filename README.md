# 🐍 Noxer App

An automated backend for an online store that fetches and updates product data from external APIs. Built with Flask + SQLAlchemy. Uses PostgreSQL and runs via Docker.

## 🚀 Features

- Loads data from two APIs:
  - `https://bot-igor.ru/api/products?on_main=true`
  - `https://bot-igor.ru/api/products?on_main=false`
- Automatically creates tables on first launch
- Periodically updates data in the background (interval configurable via `.env`)
- Provides a summary at the `/info` route
- Supports multithreading and concurrent requests
- Logs all activity (console + file)
- Fully configurable via environment variables

---

## 📦 Tech Stack

- Python 3.11
- Flask
- SQLAlchemy
- PostgreSQL
- Docker + Docker Compose

---

## ⚙️ Installation & Run

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/noxer_app.git
cd noxer_app

# 2. Make sure you have Docker and Docker Compose v2+

# 3. Add you .env file to the root

# 4. Start the app
chmod +x scripts/run_app.sh
./scripts/run_app.sh

# If the table is empty reload the browser

```

***Project structure***

```
noxer_app/
├── api_server
│   ├── __init__.py
│   ├── main.py
│   ├── __pycache__
│   │   ├── __init__.cpython-311.pyc
│   │   └── main.cpython-311.pyc
│   ├── services
│   │   ├── data_view
│   │   ├── __init__.py
│   │   ├── products
│   │   └── __pycache__
│   ├── static
│   │   └── css
│   └── templates
│       └── index.html
├── data_base
│   ├── data_base.py
│   ├── __init__.py
│   ├── models.py
│   └── __pycache__
│       ├── data_base.cpython-311.pyc
│       ├── __init__.cpython-311.pyc
│       └── models.cpython-311.pyc
├── docker-compose.yaml
├── Dockerfile
├── logger.py
├── logs
│   └── main.logs
├── __pycache__
│   ├── logger.cpython-311.pyc
│   └── settings.cpython-311.pyc
├── README.md
├── requirements.txt
├── scripts
│   ├── run_app.sh
│   └── wait-for-it.sh
└── settings.py
└── .env                     # Environment config
```

