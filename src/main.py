from src.fetch_btc import fetch_btc_price
from src.db import create_table, insert_price, get_last_7_days
from src.report import build_report
from src.email_send import send_email
from src.logger import setup_logger


logger = setup_logger()


def main():
    try:
        logger.info("Starting BTC daily report job")

        create_table()
        logger.info("Table checked/created successfully")

        price = fetch_btc_price()
        logger.info(f"Fetched BTC price: {price}")

        insert_price(price)
        logger.info("Inserted BTC price into database")

        rows = get_last_7_days()
        logger.info(f"Fetched {len(rows)} recent records from database")

        report_text = build_report(rows)
        logger.info("Report built successfully")

        send_email("BTC Daily Report", report_text)
        logger.info("Email sent successfully")

        print("Report generated and email sent successfully")

    except Exception as e:
        logger.exception(f"Job failed: {e}")
        print("Job failed. Check logs/app.log for details.")


if __name__ == "__main__":
    main()