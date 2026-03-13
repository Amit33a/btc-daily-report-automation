# BTC Daily Report Automation

This project automatically fetches the **Bitcoin (BTC) price** from the CoinGecko API, stores it in a **PostgreSQL database running inside Docker**, computes statistics from recent records, and sends a **daily email report**.

The automation runs daily using **Windows Task Scheduler**.

---

# Features

- Fetch BTC price from CoinGecko API
- Store price data in PostgreSQL
- PostgreSQL runs inside Docker
- Compute statistics from recent records
- Send automated email report
- Logging system for monitoring
- Error handling and retry logic
- Automated scheduling with Windows Task Scheduler

---

# Tech Stack

Python  
PostgreSQL  
Docker  
CoinGecko API  
SMTP (Gmail)

Python libraries used:

- requests
- psycopg[binary]
- python-dotenv
- pandas
- logging

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
- logger.py

sql/
- init.sql

logs/

docker-compose.yml  
requirements.txt  
README.md  
.env.example  

---

# Pipeline

CoinGecko API  
↓  
Fetch BTC price (requests)  
↓  
Store data in PostgreSQL (psycopg)  
↓  
Retrieve recent records  
↓  
Generate report  
↓  
Send email via SMTP  

---

# Setup

## Clone repository

```
git clone https://github.com/YOUR_USERNAME/btc-daily-report-automation.git
cd btc-daily-report-automation
```

---

## Create virtual environment

```
python -m venv .venv
```

Activate:

Windows

```
source .venv/Scripts/activate
```

---

## Install dependencies

```
python -m pip install -r requirements.txt
```

---

## Configure environment variables

Create `.env` using `.env.example`.

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

## Start PostgreSQL

```
docker compose up -d
```

Verify:

```
docker ps
```

---

## Run project

```
python -m src.main
```

---

# Logging

Application logs are stored in:

```
logs/app.log
```

Scheduler debug logs:

```
logs/scheduler_debug.log
```

---

# Automation

The script runs automatically using **Windows Task Scheduler**.

A batch script:

```
run_report.bat
```

activates the virtual environment and runs:

```
python -m src.main
```

---

# Example Email Report

BTC Daily Report

Records: 7  
Latest price: $70322  
Average price: $69800  
High price: $71000  
Low price: $68000  

Recent prices:

1. $70322  
2. $70110  
3. $69840  

---

# Error Handling

The script includes:

- try/except job wrapper
- API retry logic
- logging of exceptions
- graceful failure handling

---

# Future Improvements

Possible extensions:

- BTC price charts
- CSV export
- dashboard visualization
- deployment on cloud server
- cron scheduling on Linux

---

# Author

Amit Sharma