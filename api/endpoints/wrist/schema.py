from datetime import datetime

from pydantic import BaseModel


class Entry(BaseModel):
    id: str
    created: datetime
    temperature: int
    heartrate: int
    activity: int
    rssi: int
    is_send: bool

    class Config:
        orm_mode = True
