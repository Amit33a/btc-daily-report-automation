# BTC Daily Report Automation

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Docker](https://img.shields.io/badge/Docker-PostgreSQL-blue)
![PostgreSQL](https://img.shields.io/badge/Database-PostgreSQL-blue)
![Automation](https://img.shields.io/badge/Automation-TaskScheduler-green)
![Status](https://img.shields.io/badge/Status-Completed-success)

This project automatically fetches the **Bitcoin (BTC) price** from the CoinGecko API, stores it in a **PostgreSQL database running inside Docker**, computes statistics from recent records, and sends a **daily email report**.

It demonstrates a simple **data automation pipeline** using Python, APIs, Docker, PostgreSQL, and SMTP email.

---

# Project Features

- Fetch BTC price from CoinGecko API
- Store price data in PostgreSQL
- Run PostgreSQL inside Docker
- Compute statistics from recent records
- Send formatted email report
- Logging system for monitoring execution
- Error handling to prevent script crashes
- API retry logic for unstable requests
- Automated daily execution using Windows Task Scheduler

---

# Tech Stack

- Python
- PostgreSQL
- Docker
- CoinGecko API
- Gmail SMTP

Python libraries used:

- requests
- psycopg[binary]
- python-dotenv
- pandas

---

# Project Structure

```
btc-daily-report-automation
│
├── src
│   ├── main.py
│   ├── config.py
│   ├── db.py
│   ├── fetch_btc.py
│   ├── report.py
│   ├── email_send.py
│   └── logger.py
│
├── logs
│   ├── app.log
│   └── scheduler_debug.log
│
├── sql
│   └── init.sql
│
├── tests
│
├── docker-compose.yml
├── requirements.txt
├── README.md
├── .gitignore
├── .env.example
├── run_report.bat
```

---

# How the Project Works

The script runs the following pipeline:

```
CoinGecko API
      ↓
fetch_btc.py
      ↓
db.py (PostgreSQL via psycopg)
      ↓
report.py (compute statistics)
      ↓
email_send.py (SMTP email)
      ↓
Windows Task Scheduler automation
```

---

# System Architecture

The project follows a simple data pipeline architecture.

CoinGecko API  
↓  
fetch_btc.py  
↓  
db.py (PostgreSQL via psycopg)  
↓  
report.py (compute statistics)  
↓  
email_send.py (SMTP email)  
↓  
Task Scheduler automation  

---

# Setup Instructions

## 1 Clone the Repository

```
git clone https://github.com/YOUR_USERNAME/btc-daily-report-automation.git
cd btc-daily-report-automation
```

---

## 2 Create Virtual Environment

```
python -m venv .venv
```

Activate it (Windows):

```
source .venv/Scripts/activate
```

---

## 3 Install Dependencies

```
python -m pip install -r requirements.txt
```

---

## 4 Configure Environment Variables

Create a `.env` file based on `.env.example`.

Example:

```
DB_HOST=localhost
DB_PORT=5434
DB_USER=btc_user
DB_PASSWORD=btc_password
DB_NAME=btc_db

EMAIL_FROM=your_email@gmail.com
EMAIL_TO=receiver@gmail.com
EMAIL_APP_PASSWORD=your_app_password

SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
```

---

## 5 Start PostgreSQL with Docker

```
docker compose up -d
```

Verify container:

```
docker ps
```

---

## 6 Run the Project

```
python -m src.main
```

The script will:

1. Fetch BTC price  
2. Store it in PostgreSQL  
3. Generate statistics  
4. Send the report via email  

---

# Example Email Report

```
BTC Daily Report

Records: 7
Latest price: $70322
Average price: $69500
High price: $71000
Low price: $68000
Change: $2322
Percent change: 3.4%

Recent prices

1. $70322
2. $69900
3. $69200
```

---

# Logging

Execution logs are saved in:

```
logs/app.log
```

Scheduler debug logs are saved in:

```
logs/scheduler_debug.log
```

These logs help diagnose errors and monitor automation runs.

---

# Example Log Output

```
2026-03-12 19:12:48 | INFO | Starting BTC daily report job
2026-03-12 19:12:49 | INFO | Table checked/created successfully
2026-03-12 19:12:52 | INFO | Fetched BTC price: 70322.0
2026-03-12 19:12:52 | INFO | Inserted BTC price into database
2026-03-12 19:12:52 | INFO | Report built successfully
2026-03-12 19:12:56 | INFO | Email sent successfully
```

---

# Automation with Windows Task Scheduler

The project includes a batch script:

```
run_report.bat
```

This script:

1. Navigates to the project directory
2. Activates the virtual environment
3. Runs the Python automation script

Task Scheduler runs this script daily to automate the pipeline.

---

# Security Notes

`.env` is excluded from GitHub using `.gitignore`.

Never commit:

- passwords
- email credentials
- API keys

Use Gmail **App Password**, not your real Gmail password.

---

# Key Concepts Learned

This project helped me understand:

- Python project structure
- Environment variable management
- PostgreSQL integration with psycopg
- Docker containerized databases
- API integration using requests
- Logging and error handling
- Retry logic for unstable APIs
- Email automation using SMTP
- Task Scheduler automation

---

# Future Improvements

Possible enhancements:

- Add BTC price charts
- Export historical data to CSV
- Build a small dashboard
- Deploy automation to a cloud server

---

# Author

Amit Sharma
