from psycopg import connect
from psycopg.rows import dict_row
from src.config import get_settings


def get_connection():
    settings = get_settings()

    conn = connect(
        host=settings.db_host,
        port=settings.db_port,
        user=settings.db_user,
        password=settings.db_password,
        dbname=settings.db_name,
        row_factory=dict_row
    )

    return conn


def create_table():

    create_table_sql = """
    CREATE TABLE IF NOT EXISTS btc_prices (
        id SERIAL PRIMARY KEY,
        price_usd NUMERIC NOT NULL,
        recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """

    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(create_table_sql)
            conn.commit()





   
def insert_price(price: float):
    insert_sql = """
    INSERT INTO btc_prices (price_usd)
    VALUES (%s);
    """

    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(insert_sql, (price,))
            conn.commit()


def get_last_7_days():
    query_sql = """
    SELECT *
    FROM btc_prices
    ORDER BY recorded_at DESC
    LIMIT 7;
    """

    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query_sql)
            rows = cursor.fetchall()
            return rows
