from pydantic import BaseModel
from pony import orm


db = orm.Database()


class Country(db.Entity):
    name = orm.Required(str)
    tournaments = orm.Set("Tournament")

    class Schema(BaseModel):
        name: str


class Tournament(db.Entity):
    name = orm.Required(str)
    is_ranking = orm.Required(bool)
    country = orm.Required(Country)

    class Schema(BaseModel):
        name: str
        is_ranking: bool
        country: int


db.bind(provider="postgres", host="localhost", database="snookerdb")
db.generate_mapping(create_tables=True)
