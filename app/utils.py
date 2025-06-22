from datetime import datetime


def parse_timestamp(ts: str) -> datetime:
    return datetime.fromisoformat(ts)