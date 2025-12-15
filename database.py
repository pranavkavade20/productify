from sqlalchemy import create_engine
from sqlalchemy.orm  import sessionmaker

db_url ="postgresql://postgres:p2002@localhost:5432/crud_product"
engine = create_engine(db_url)
session = sessionmaker(autocommit=False, autoflush=False,bind=engine)