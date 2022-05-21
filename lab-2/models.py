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


db.bind(provider="postgres", host="localhost", database="snookerdb")
db.generate_mapping(create_tables=True)
