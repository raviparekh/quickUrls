
class AppConfig(object):

    def __init__(self, config_name, secret_key, debug, database_config):
        self.config_name = config_name
        self.secret_key = secret_key
        self.debug = debug
        self.db_config = database_config
