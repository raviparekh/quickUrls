import json
import os

from quickUrls.config.config_classes import _app_config, _database_config


JSON_FILE_NAME = "{}.{}".format(os.environ.get('QUICKURL_ENV', "dev"), "json")

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(CURRENT_DIR, JSON_FILE_NAME)) as json_config:
    config_data = json.load(json_config)

try:
    _db_config = _database_config.DatabaseConfig(config_data['DB_CONFIG']['DB_NAME'],
                                                 config_data['DB_CONFIG']['DB_HOST'],
                                                 config_data['DB_CONFIG']['DB_PORT'],
                                                 config_data['DB_CONFIG']['DB_USERNAME'],
                                                 config_data['DB_CONFIG']['DB_PASSWORD'])

    APP_CONFIG = _app_config.AppConfig(config_data['CONFIG_NAME'], config_data['SECRET_KEY'],
                                      config_data['DEBUG'], _db_config)
except KeyError, e:
    raise RuntimeError("An expected configuration attribute is not in the JSON. Missing {}".format(e.message))
