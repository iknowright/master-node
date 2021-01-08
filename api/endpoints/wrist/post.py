from fastapi.responses import PlainTextResponse
from fastapi import Depends
from sqlalchemy.orm import Session

from database import SESSIONLOCAL
from .schema import Entry
from .crud import create_entry

# Document for generating custom response
# References: https://fastapi.tiangolo.com/advanced/additional-responses
DOC = {
    201: {
        "description": "Created",
        "content": {"text/plain": {"example": "OK"}},
    }
}

# Dependency
def get_db():
    database = SESSIONLOCAL()
    try:
        yield database
    finally:
        database.close()


def post(entry: Entry, database: Session = Depends(get_db)):
    create_entry(db=database, entry=entry)
    return PlainTextResponse("OK", 201)
