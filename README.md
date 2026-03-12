# BTC Daily Report Automation

This project automatically fetches the **Bitcoin (BTC) price** from the CoinGecko API, stores it in a **PostgreSQL database running inside Docker**, computes statistics from the most recent records, and sends a **daily email report**.

It demonstrates a simple **data automation pipeline** using Python, APIs, Docker, PostgreSQL, and SMTP email.

---

# Project Features

- Fetch BTC price from CoinGecko API
- Store price data in PostgreSQL
- Run PostgreSQL inside Docker
- Compute statistics from the latest records
- Send formatted email report

---

# Tech Stack

- Python
- PostgreSQL
- Docker
- CoinGecko API
- SMTP (Gmail)

Python libraries used:

- requests
- psycopg[binary]
- python-dotenv
- pandas

---

# Project Structure

btc-daily-report-automation

src/
- main.py
- config.py
- db.py
- fetch_btc.py
- report.py
- email_send.py

sql/
- init.sql

tests/

docker-compose.yml  
requirements.txt  
README.md  
.env.example  

---

# How the Project Works

The script runs this pipeline:

CoinGecko API  
↓  
Fetch BTC price (requests)  
↓  
Store data in PostgreSQL (psycopg)  
↓  
Retrieve last records  
↓  
Generate report  
↓  
Send email via SMTP  

---

# Setup Instructions

## 1 Clone the Repository

git clone https://github.com/YOUR_USERNAME/btc-daily-report-automation.git

cd btc-daily-report-automation

---

## 2 Create Virtual Environment

python -m venv .venv

Activate it (Windows):

source .venv/Scripts/activate

---

## 3 Install Dependencies

python -m pip install -r requirements.txt

---

## 4 Configure Environment Variables

Create a `.env` file based on `.env.example`.

Example:

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

---

## 5 Start PostgreSQL with Docker

docker compose up -d

Verify container:

docker ps

---

## 6 Run the Project

python -m src.main

The script will:

1 Fetch BTC price  
2 Store it in the database  
3 Generate report  
4 Send email  

---

# Example Email Report

BTC Daily Report

Records: 7  
Latest price: $68044  
Average price: $67500  
High price: $69200  
Low price: $65300  
Change: $2744  
Percent change: 4.2%

Recent prices

1. $68044  
2. $67900  
3. $67100  

---

# Security Notes

`.env` is excluded from GitHub using `.gitignore`.

Do not commit secrets or passwords.

Use Gmail **App Password**, not your real Gmail password.

---

# Future Improvements

Possible improvements:

- Schedule script daily using Windows Task Scheduler
- Add error handling
- Add logging
- Create dashboard for price history
- Deploy on a cloud server

---

# Author

Amit Sharma

