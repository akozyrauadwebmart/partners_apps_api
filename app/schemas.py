from pydantic import BaseModel
from datetime import datetime


class InstallEvent(BaseModel):
    ip: str
    att: str
    city: str
    idfa: str
    idfv: str
    state: str
    app_id: str
    region: str
    app_name: str
    campaign: str
    platform: str
    bundle_id: str
    event_name: str
    event_time: datetime
    event_type: str
    match_type: str
    os_version: str
    user_agent: str
    api_version: str
    app_version: str
    postal_code: str
    sdk_version: str
    appsflyer_id: str
    country_code: str
    device_model: str
    event_source: str
    install_time: datetime
    media_source: str
    is_retargeting: bool
    selected_currency: str
    attributed_touch_time: datetime