import os
from sqlalchemy import create_engine
from sqlalchemy import text
import pandas as pd
from dotenv import load_dotenv

# load the .env file variables
load_dotenv()

# 1) Connect to the database here using the SQLAlchemy's create_engine function

connection_string = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
engine = create_engine(connection_string).execution_options(autocommit=True)
engine.connect()

# 2) Execute the SQL sentences to create your tables using the SQLAlchemy's execute function

with engine.connect() as con:
    with open("/workspace/connecting-to-a-sql-database-project-tutorial/src/sql/create.sql") as file:
        query = text(file.read())
        con.execute(query)

# 3) Execute the SQL sentences to insert your data using the SQLAlchemy's execute function

with engine.connect() as con:
    with open("/workspace/connecting-to-a-sql-database-project-tutorial/src/sql/insert.sql") as file:
        query = text(file.read())
        con.execute(query)

# 4) Use pandas to print one of the tables as dataframes using read_sql function

authors = pd.read_sql_query("SELECT * FROM publishers", engine)
print(authors)