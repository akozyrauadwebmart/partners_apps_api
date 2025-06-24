import pytz
from uuid import uuid4
from datetime import datetime
import logging

from fastapi import FastAPI, Depends, HTTPException, status
from clickhouse_connect.driver.client import Client
from db.clickhouse.client_init import create_client

import app.schemas as schemas


logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

app = FastAPI()
logger = logging.getLogger(__name__)


@app.post("/create-event")
async def create_event(
        event: schemas.InstallEvent,
        ch_client: Client = Depends(create_client)
) -> None:
    try:
        event.event_time = event.event_time.replace(tzinfo=pytz.timezone('UTC'))
        event.install_time = event.install_time.replace(tzinfo=pytz.timezone('UTC'))
        event.attributed_touch_time = event.attributed_touch_time.replace(tzinfo=pytz.timezone('UTC'))

        now = datetime.now(tz=pytz.timezone("UTC"))
        json_data = event.model_dump()
        insert_data = {
            "id": uuid4(),
            **json_data,
            "created": now,
            "updated": now
        }

        columns = list(insert_data.keys())
        data = [tuple(insert_data.values())]

        ch_client.insert(database="partners_apps_db", table="app_events", data=data, column_names=columns)
        erro = 1 / 0
        logger.info("Event successfully inserted: %s", insert_data["id"])
        return {"message": "Event successfully inserted."}
    except Exception as ex:
        logger.exception("Failed to insert event into ClickHouse")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to insert event: {str(ex)}"
        )