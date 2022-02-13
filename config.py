import os
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", os.urandom(24))
    DEBUG = False

    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY", os.urandom(24))
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=7)


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", "sqlite:///" + os.path.join(basedir, "data-dev.sqlite")
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True


config_by_name = dict(
    development=DevelopmentConfig,
    default=DevelopmentConfig,
)
