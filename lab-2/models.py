from pydantic import BaseModel, validator, conint
from pony.orm import Database, Required, Optional, Set, db_session
from datetime import date


db = Database()


@db_session
def validate_foreign_key(model_class, value):
    if not model_class.get(id=value):
        raise ValueError(f"{model_class.__name__} with ID {value} does not exist")
    return value


class Country(db.Entity):
    name = Required(str)
    tournaments = Set("Tournament")
    players = Set("Player")

    class Schema(BaseModel):
        name: str


class Tournament(db.Entity):
    name = Required(str)
    is_ranking = Required(bool)
    country = Required(Country)
    games = Set("Game")

    class Schema(BaseModel):
        name: str
        is_ranking: bool
        country: int

        @validator("country")
        def country_exists(cls, value):
            return validate_foreign_key(Country, value)


class Player(db.Entity):
    name = Required(str)
    nickname = Optional(str)
    birth_date = Required(date)
    country = Required(Country)
    games_as_left_player = Set("Game", reverse="left_player")
    games_as_right_player = Set("Game", reverse="right_player")

    class Schema(BaseModel):
        name: str
        nickname: str | None
        birth_date: date
        country: int

        @validator("birth_date")
        def is_later_than_1900(cls, value):
            if value.year < 1900:
                raise ValueError("must be later than 1900")
            return value

        @validator("country")
        def country_exists(cls, value):
            return validate_foreign_key(Country, value)


class Game(db.Entity):
    date = Required(date)
    part_of_final = Required(int)
    left_player = Required(Player, reverse="games_as_left_player")
    right_player = Required(Player, reverse="games_as_right_player")
    tournament = Required(Tournament)
    frames = Set("Frame")

    class Schema(BaseModel):
        date: date
        part_of_final: int
        left_player: int
        right_player: int
        tournament: int

        @validator("date")
        def is_later_than_1980(cls, value):
            if value.year < 1980:
                raise ValueError("must be later than 1980")
            return value

        @validator("part_of_final")
        def part_of_final_is_power_of_two(cls, value):
            if (value & (value - 1) != 0) or value == 0:
                raise ValueError("must be a power of two")
            return value

        @validator("left_player")
        def left_player_exists(cls, value):
            return validate_foreign_key(Player, value)

        @validator("right_player")
        def right_player_exists_and_is_not_left(cls, value, values):
            validate_foreign_key(Player, value)
            if value == values.get("left_player"):
                raise ValueError("cannot be the same as right_player")
            return value

        @validator("tournament")
        def tournament_exists(cls, value):
            return validate_foreign_key(Tournament, value)


class Frame(db.Entity):
    left_player_score = Required(int)
    right_player_score = Required(int)
    game = Required(Game)

    class Schema(BaseModel):
        left_player_score: conint(ge=0)
        right_player_score: conint(ge=0)
        game: int

        @validator("game")
        def game_exists(cls, value):
            return validate_foreign_key(Game, value)


db.bind(provider="postgres", host="localhost", database="snookerdb")
db.generate_mapping(create_tables=True)
