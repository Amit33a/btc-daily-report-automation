from src.fetch_btc import fetch_btc_price
from src.db import create_table, insert_price, get_last_7_days
from src.report import build_report
from src.email_send import send_email


def main():

    # Ensure table exists
    create_table()

    # Fetch latest BTC price
    price = fetch_btc_price()

    # Insert price into database
    insert_price(price)

    # Read last 7 records
    rows = get_last_7_days()

    # Build report text
    report_text = build_report(rows)

    # Send email
    send_email("BTC Daily Report", report_text)

    print("Report generated and email sent successfully")


if __name__ == "__main__":
    main()