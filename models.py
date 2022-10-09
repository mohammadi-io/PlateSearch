from sqlalchemy import Column, DATETIME, Integer, String, TIMESTAMP
from database import Base


class Plate(Base):
    __tablename__ = 'plates'
    raw_plate = Column(String, primary_key=True, index=True)
    plate_without_hyphen = Column(String)
    timestamp = Column(TIMESTAMP)
