from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = 'sqlite+pysqlite:///./mini.db'

# engine = create_engine(url=SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}, echo=True)
engine = create_engine("postgresql://postgres:Openpostgres@localhost/test")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
