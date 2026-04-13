# config.py

class Config:
    SECRET_KEY = 'your_secret_key'
    SESSION_COOKIE_NAME = 'your_cookie_name'

    # Database settings
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///development.db'
    SCRAPER_URL = 'http://localhost:5000/scrape'

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql://user:password@localhost/prod_db'
    SCRAPER_URL = 'https://example.com/scrape'

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///testing.db'
    SCRAPER_URL = 'http://localhost:5000/scrape'
