"""
Pendiente de si se usa
https://fastapi.tiangolo.com/tutorial/sql-databases/
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./src/db.sqlite3"


# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

# Create the engine. We will later use this engine in other places.
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False} 
)#connect_args is needed only for SQLite. It's not needed for other databases.

# Create a session. 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the base class for our ORM classes.
Base = declarative_base()