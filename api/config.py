import os


class Config:
    """Parent configuration class."""
    APP_TITLE = os.environ.get('APP_TITLE', 'FastAPI template')
    APP_DESCRIPTION = os.environ.get('APP_DESCRIPTION', 'A template for FastAPI.')
    VERSION = os.environ.get('VERSION', '0.0.0')
    # enable Swagger
    SWAGGER_URL = os.environ.get('SWAGGER_URL', '/docs')
    # disable Redoc
    REDOC_URL = os.environ.get('REDOC_URL', '')
