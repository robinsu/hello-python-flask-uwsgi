## init python logging 
import os
import logging
import logging.config

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s %(levelname)-5s [%(filename)-8s](%(lineno)s): %(message)s',
            'datefmt': '%m-%d %H:%M:%S'
        }
    },
    'handlers': {
        'stdout': {
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',  # Default is stderr
        },
        'rollingFile': {
            'formatter': 'standard',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.getenv('FLASKR_LOG', '/var/log/flaskr.log'),  # TimedRotatingFileHandler
            "when": "midnight",
            "encoding": "utf-8"
        },
    },
    'loggers': {
        '': {  # root logger
            'handlers': ['stdout', 'rollingFile'],
            'level': 'INFO',
            'propagate': True
        }
    }
}

logging.config.dictConfig(LOGGING_CONFIG)

import os
from flask import Flask

logger = logging.getLogger(__name__)

## https://flask.palletsprojects.com/en/2.0.x/tutorial/index.html
def create_app(test_config=None):
    # create and configure the app
    # app = Flask(__name__, instance_relative_config=True)
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='YOU_NEED_CHANGE_IT_TO_VERY_LONG_STRING'
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        print("begin read config from_pyfile")
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        print("instance_path: " + app.instance_path)
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # load modules
    from .api.retail import retail
    
    # register blueprints. ensure that all paths are versioned!
    app.register_blueprint(retail, url_prefix="/api/retail")

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app
