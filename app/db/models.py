from sqlalchemy import Column, String, Boolean, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
import uuid

Base = declarative_base()

class InstallEvent(Base):
    __tablename__ = "install_events"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    ip = Column(String(255))
    att = Column(String(255))
    city = Column(String(255))
    idfa = Column(String(255))
    idfv = Column(String(255))
    state = Column(String(255))
    app_id = Column(String(255))
    region = Column(String(255))
    app_name = Column(String(255))
    campaign = Column(String(255))
    platform = Column(String(255))
    bundle_id = Column(String(255))
    event_name = Column(String(255))
    event_time = Column(TIMESTAMP(timezone=True))
    event_type = Column(String(255))
    match_type = Column(String(255))
    os_version = Column(String(255))
    user_agent = Column(String(255))
    api_version = Column(String(255))
    app_version = Column(String(255))
    postal_code = Column(String(255))
    sdk_version = Column(String(255))
    appsflyer_id = Column(String(255))
    country_code = Column(String(255))
    device_model = Column(String(255))
    event_source = Column(String(255))
    install_time = Column(TIMESTAMP(timezone=True))
    media_source = Column(String(255))
    is_retargeting = Column(Boolean)
    selected_currency = Column(String(255))
    attributed_touch_time = Column(TIMESTAMP(timezone=True))
