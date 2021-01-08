from sqlalchemy import Boolean, Column, Integer, String, DateTime

from database import BASE


class Entry(BASE):
    __tablename__ = "entries"

    id = Column(String, primary_key=True, index=True)
    created = Column(DateTime, primary_key=True)
    heartrate = Column(Integer(), nullable=False)
    temperature = Column(Integer(), nullable=False)
    activity = Column(Integer(), nullable=False)
    rssi = Column(Integer(), nullable=False)
    is_sent = Column(Boolean(), default=False)
