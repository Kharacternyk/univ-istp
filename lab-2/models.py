from pydantic import BaseModel, validator
from pony.orm import Database, Required, Set, db_session


db = Database()


class Country(db.Entity):
    name = Required(str)
    tournaments = Set("Tournament")

    class Schema(BaseModel):
        name: str


class Tournament(db.Entity):
    name = Required(str)
    is_ranking = Required(bool)
    country = Required(Country)

    class Schema(BaseModel):
        name: str
        is_ranking: bool
        country: int

        @validator("country")
        @db_session
        def country_exists(cls, value):
            if not Country.get(id=value):
                raise ValueError(f"country with ID {value} does not exist")
            return value


db.bind(provider="postgres", host="localhost", database="snookerdb")
db.generate_mapping(create_tables=True)
