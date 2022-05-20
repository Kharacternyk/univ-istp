from fastapi import FastAPI
from pony.orm import db_session, select
from inspect import getmembers
import inflect
import models

app = FastAPI()
inflect_engine = inflect.engine()


def create_get_all_endpoint(model_class):
    @db_session
    def handler():
        return [
            record.to_dict(with_collections=True)
            for record in select(record for record in model_class)
        ]

    endpoint = inflect_engine.plural(model_class.__name__.lower())
    handler.__name__ = "get_all_" + endpoint
    app.get("/" + endpoint, tags=[model_class.__name__])(handler)


def create_get_endpoint(model_class):
    @db_session
    def handler(id: int):
        return model_class[id].to_dict(with_collections=True)

    endpoint = inflect_engine.plural(model_class.__name__.lower())
    handler.__name__ = "get_" + model_class.__name__.lower()
    app.get("/" + endpoint + "/{id}", tags=[model_class.__name__])(handler)


def create_post_endpoint(model_class):
    @db_session
    def handler(schema: model_class.Schema):
        model_class(**schema.dict())

    endpoint = inflect_engine.plural(model_class.__name__.lower())
    handler.__name__ = "post_" + model_class.__name__.lower()
    app.post("/" + endpoint, tags=[model_class.__name__])(handler)


def create_delete_endpoint(model_class):
    @db_session
    def handler(id: int):
        model_class[id].delete()

    endpoint = inflect_engine.plural(model_class.__name__.lower())
    handler.__name__ = "delete_" + model_class.__name__.lower()
    app.delete("/" + endpoint + "/{id}", tags=[model_class.__name__])(handler)


for name, value in getmembers(models, lambda value: hasattr(value, "Schema")):
    create_get_all_endpoint(value)
    create_get_endpoint(value)
    create_post_endpoint(value)
    create_delete_endpoint(value)
