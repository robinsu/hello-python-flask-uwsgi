# import click
import logging
from flask import current_app, g
from flask.cli import with_appcontext
from sqlalchemy import create_engine
#from sqlalchemy.ext.declarative import declarative_base
#from sqlalchemy.orm import sessionmaker

logger = logging.getLogger(__name__)

def get_db_engine():
    if 'db_engine' not in g:
        db_string = current_app.config['SQLALCHEMY_DATABASE_URI']
        logging.debug(f"SQLALCHEMY_DATABASE_URI = {db_string}")
        engine = create_engine( db_string ## , connect_args={"check_same_thread": False}
                                , pool_pre_ping=True)
        g.db_engine = engine

    return g.db_engine


def close_db(e=None):
    engine = g.pop('db_engine', None)

    if engine is not None:
        engine.close()