from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = 'sqlite+pysqlite:///./mini.db'

# engine = create_engine(url=SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}, echo=True)
engine = create_engine("postgres://pvbusnkywcezmi:3e618d6e6af05d7244bea222fc636ed750af73135a948721221299ee5c7999be@ec2-34-249-236-155.eu-west-1.compute.amazonaws.com:5432/d1h13q7tq4spr")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
