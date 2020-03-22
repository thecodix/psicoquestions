import os


class BaseConfig(object):
    DEBUG = False
    TESTING = False
    REDIS_URL = "redis://@localhost:6379/0"


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = True


class TestingConfig(BaseConfig):
    DEBUG = False
    TESTING = True


config = {
    "dev": "questions.config.DevelopmentConfig",
    "testing": "questions.config.TestingConfig",
    "default": "questions.config.DevelopmentConfig",
}


def configure_app(app):
    config_name = os.getenv("FLASK_CONFIGURATION", "default")
    app.config.from_object(config[config_name])
    #TODO load configuration from file
