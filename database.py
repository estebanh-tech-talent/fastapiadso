from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# DATABASE_URL = "mysql+pymysql://root:password@localhost:3306/cubo"
# DATABASE_URL = "mysql+pymysql://root:adso_2025*@172.17.0.2:3306/cubo"
# DATABASE_URL = "mysql+pymysql://root:adso_2025@192.168.1.7:3366/cubo"
DATABASE_URL = "mysql+pymysql://root:adso_2025@192.168.1.7:3307/cubo"

engine = create_engine(DATABASE_URL, connect_args={"charset": "utf8mb4"})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
