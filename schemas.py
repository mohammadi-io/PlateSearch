from datetime import datetime
from pydantic import BaseModel, Field


class Plate(BaseModel):
    raw_plate: str = Field(alias='plate')


class ShowPlate(BaseModel):
    raw_plate: str = Field(alias='plate')
    timestamp: datetime

    class Config:
        """"SQLAlchemy does not return a dictionary, which is what pydantic expects by default. You can configure
        your model to also support loading from standard orm parameters (i.e. attributes on the object instead of
        dictionary lookups) """
        orm_mode = True
        allow_population_by_field_name = True


class ShowSearchPlate(BaseModel):
    plate_without_hyphen: str = Field(alias='plate')
    timestamp: datetime

    class Config:
        """"SQLAlchemy does not return a dictionary, which is what pydantic expects by default. You can configure
        your model to also support loading from standard orm parameters (i.e. attributes on the object instead of
        dictionary lookups) """
        orm_mode = True
        allow_population_by_field_name = True
