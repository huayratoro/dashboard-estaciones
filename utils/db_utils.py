from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Cargo variables de entorno
load_dotenv()

def get_db_connection():
    db_url = f"postgresql://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    engine = create_engine(db_url)
    return engine.connect()
