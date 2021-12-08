from os import getenv

from dotenv.main import load_dotenv

load_dotenv()

DB_DATABASE = getenv('DB_DATABASE')
DB_USERNAME = getenv('DB_USERNAME')
DB_PASSWORD = getenv('DB_PASSWORD')
DB_HOST = getenv('DB_HOST')
DB_PORT = getenv('DB_PORT')


def get_database_url():
    """
    Generate sqlalchemy database url from env vars.
    """
    return 'postgresql://{}:{}@{}:{}/{}'.format(
        DB_USERNAME,
        DB_PASSWORD,
        DB_HOST,
        DB_PORT,
        DB_DATABASE
    )
