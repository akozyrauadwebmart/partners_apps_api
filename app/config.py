import os

from dotenv import load_dotenv


load_dotenv()


class PostgresDB:
    HOST = os.getenv("DB_HOST")
    PORT = os.getenv("DB_PORT")
    USER = os.getenv("DB_USER")
    PASSWORD = os.getenv("DB_PASSWORD")
    NAME = os.getenv("DB_NAME")


class ClickHouseProd:
    HOST = os.getenv("CLICKHOUSE_PROD_HOST")
    PORT = os.getenv("CLICKHOUSE_PROD_PORT")
    USER = os.getenv("CLICKHOUSE_PROD_USER")
    PASSWORD = os.getenv("CLICKHOUSE_PROD_PASSWORD")
    DB_NAME = os.getenv("CLICKHOUSE_PROD_DB")


def main() -> None:
    pass


if __name__ == "__main__":
    main()