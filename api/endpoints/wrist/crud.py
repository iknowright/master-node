from sqlalchemy.orm import Session

from . import model, schema


def create_entry(db: Session, entry: schema.Entry):
    data = {
        "id": entry.id,
        "created": entry.created,
        "temperature": entry.temperature,
        "heartrate": entry.heartrate,
        "activity": entry.activity,
        "rssi": entry.rssi,
    }
    db_entry = model.Entry(**data)
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return db_entry
