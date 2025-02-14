import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Load the correct environment file
if os.getenv("ENV") == "production":
    load_dotenv(".env")  # Load production settings
else:
    load_dotenv(".env.local")  # Load local development settings

# Get the database URL
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./dev.db")

# Create database engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {})

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()

# Dependency to get the DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()