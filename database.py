from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine("postgres://ldolatsggrtrwl:618ec0efdf4a1060862985938f242a7ab01af26c35def1f90ee4917f82c7f072@ec2-54-170-90-26.eu-west-1.compute.amazonaws.com:5432/d4ga7hgqbhkhrl")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
