from os import environ

# default: use sqlite file for dev/testing when DATABASE_URL not set
DATABASE_URL = environ.get(
    'DATABASE_URL',
    'sqlite:///./dev.db'
)
