class Config:
    """Common configurations"""
    APP_NAME = 'app'

class DevelopmentConfig(Config):
    """
    Development configurations
    """
    DEBUG = True
    TESTING = True

    # Config for MongoEngine
    MONGODB_SETTINGS = {
      'db': 'sample',
      'host': 'mongo',
      'username': 'root',
      'password': 'root',
    }

class ProductionConfig(Config):
    """
    Production configurations
    """
    DEBUG = False

app_config = {
    'default': Config,
    'development': DevelopmentConfig,
    'production': ProductionConfig
}