import os

class Config:
    SECRET_KEY = 'thisissecret'
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://bigbaby:New Password@localhost/pitcher'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    #email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    #simple mde configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

class ProdConfig(Config):
    pass

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://bigbaby:New Password@localhost/pitcher_test'

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://bigbaby:New Password@localhost/pitcher'
    DEBUG = True


config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}