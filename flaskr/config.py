import os

JSON_AS_ASCII = False

# https://www.jitsejan.com/setting-up-postgres-for-python
USER = os.getenv('POSTGRES_USER', 'postres') 
PASS = os.getenv('POSTGRES_PASS', 'secure') 
HOST = os.getenv('POSTGRES_HOST', 'host.docker.internal') 
PORT = os.getenv('POSTGRES_PORT', '5432') 
DB = os.getenv('POSTGRES_DB', 'postgres') 
db_string = f"postgresql://{USER}:{PASS}@{HOST}:{PORT}/{DB}"
SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', db_string)  

MQTT_BROKER_URL = os.getenv('MQTT_BROKER_URL', 'host.docker.internal') 
MQTT_BROKER_PORT = int(os.getenv('MQTT_BROKER_PORT', 1883)) 
## MQTT_REFRESH_TIME = 1.0 
## MQTT_KEEPALIVE=5