import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# DATABASE_URL = "mysql+pymysql://root:password@localhost:3306/cubo"
# DATABASE_URL = "mysql+pymysql://root:adso_2025*@172.17.0.2:3306/cubo"
# DATABASE_URL = "mysql+pymysql://root:adso_2025@192.168.1.7:3366/cubo"
# DATABASE_URL = "mysql+pymysql://root:VDxMquhRcllksfDLacoaWTRLmQxMssfD@mainline.proxy.rlwy.net:26400/cubo"

# DATABASE_URL = "mysql+pymysql://root:VDxMquhRcllksfDLacoaWTRLmQxMssfD@mysql.railway.internal:3306/cubo"

DB_USER = os.getenv("MYSQLUSER")
DB_PASSWORD = os.getenv("MYSQLPASSWORD")
DB_HOST = os.getenv("MYSQLHOST")
DB_PORT = os.getenv("MYSQLPORT")
DB_NAME = os.getenv("MYSQLDATABASE")

ENV_FLAG = os.getenv("FLAG")

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

print(f"Connecting to database at {DB_HOST}:{DB_PORT} with user {DB_USER}, {ENV_FLAG}")

engine = create_engine(DATABASE_URL, connect_args={"charset": "utf8mb4"})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
