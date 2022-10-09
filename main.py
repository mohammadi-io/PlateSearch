from datetime import datetime
from typing import List

from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy import func
from sqlalchemy.exc import DatabaseError
from sqlalchemy.orm import Session

import models
import re
import schemas
from database import Base, engine, get_db

Base.metadata.create_all(bind=engine)  # creates all database tables
app = FastAPI()


def check_is_valid_plate(plate):
    pattern = re.compile("^([A-Z]){1,3}-([A-Z]){1,2}([1-9])([0-9]){0,3}$")
    if not pattern.match(plate):
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail="The plate is not a valid German plate")


@app.post(path="/plate", status_code=status.HTTP_201_CREATED, response_model=schemas.ShowPlate)
async def create_plate(request: schemas.Plate, db: Session = Depends(get_db)):
    plate = request.raw_plate.upper()
    check_is_valid_plate(plate)
    new_plate = models.Plate(raw_plate=plate, plate_without_hyphen=plate.replace('-', ''), timestamp=datetime.now())
    db.add(instance=new_plate)
    try:
        db.commit()
    except DatabaseError as err:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(err))
    db.refresh(instance=new_plate)  # refresh attributes on the given instance
    return new_plate


@app.get(path="/plate", response_model=List[schemas.ShowPlate])
def get_all_plates(db: Session = Depends(dependency=get_db)):
    return db.query(models.Plate).all()


@app.get(path="/search-plate", response_model=List[schemas.ShowSearchPlate])
def search_plates(key: str, levenshtein: int = 0, db: Session = Depends(dependency=get_db)):
    key = key.replace('-', '').upper()
    return db.query(models.Plate).filter(func.levenshtein(models.Plate.plate_without_hyphen, key) <= levenshtein).all()
