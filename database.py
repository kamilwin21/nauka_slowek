from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# DATABASE_URL = "sqlite:///./words.db"
DATABASE_URL = "postgresql://words_9kcm_user:UdzQYKQHMaMrEAWlZM2sKmtqZN9ZMBPF@dpg-d0l0ncffte5s7393k6q0-a/words_9kcm"


engine = create_engine(
    # DATABASE_URL, connect_args={"check_same_thread": False}
        DATABASE_URL}

)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
