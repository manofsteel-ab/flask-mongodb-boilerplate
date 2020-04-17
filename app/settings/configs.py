class Config:
    """Common configurations"""
    APP_NAME = 'app'
    DEBUG = True
    TESTING = True


class DevelopmentConfig(Config):
    """
    Development configurations
    """
    TESTING = False
    # Config for MongoEngine
    MONGODB_SETTINGS = {
      'db': 'sample',
      'host': 'mongo',
      'port': 27017,
      'username': 'samples',
      'password': 'sample',
    }


class ProductionConfig(Config):
    """
    Production configurations
    """
    DEBUG = False
    TESTING = False
    # Config for MongoEngine
    MONGODB_SETTINGS = {
      'db': '"Your prod database"',
      'host': 'mongo',
      'port': 27017,
      'username': 'Your prod database username',
      'password': 'Your prod database password',
    }


class TestConfig(Config):
    MONGODB_SETTINGS = {
        'db': 'testdb',
        'host': 'mongo',
        'port': 27017,
        'username': 'testdb',
        'password': 'testdb',
    }


app_config = {
    'default': Config,
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'test': TestConfig
}
