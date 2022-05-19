from fastapi import FastAPI
from pydantic import BaseModel
from pony import orm


DATABASE_URL = "postgresql://localhost/snookerdb"
db = orm.Database()


class Country(db.Entity):
    name = orm.Required(str)
    tournaments = orm.Set("Tournament")


class Tournament(db.Entity):
    name = orm.Required(str)
    is_ranking = orm.Required(bool)
    country = orm.Required(Country)


db.bind(provider="postgres", host="localhost", database="snookerdb")
db.generate_mapping(create_tables=True)

app = FastAPI()


class CountrySchema(BaseModel):
    name: str


class TournamentSchema(BaseModel):
    name: str
    is_ranking: bool
    country: int


@app.get("/countries")
@orm.db_session
def get_countries():
    return [
        row.to_dict(with_collections=True)
        for row in orm.select(country for country in Country)
    ]


@app.post("/countries")
@orm.db_session
def post_countries(country: CountrySchema):
    Country(**country.dict())


@app.get("/tournaments")
@orm.db_session
def get_tournaments():
    return [
        row.to_dict(with_collections=True)
        for row in orm.select(tournament for tournament in Tournament)
    ]


@app.post("/tournaments")
@orm.db_session
def post_tournaments(tournament: TournamentSchema):
    Tournament(**tournament.dict())
