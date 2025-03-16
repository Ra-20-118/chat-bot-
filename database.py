from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

Azure PostgreSQL
DATABASE_URL = "postgresql://stage6postgres:Raghad123@stage6-postgres.postgres.database.azure.com:5432/postgres"

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()