# data_extraction.py
import psycopg2
import pandas as pd
from sqlalchemy import create_engine

# PostgreSQL connection parameters
db_params = {
    'host': 'localhost',  
    'dbname': 'telecom_data',  
    'user': 'postgres',  
    'password': 'password'  
}

# Create the connection string
conn_str = f"postgresql+psycopg2://{db_params['user']}:{db_params['password']}@{db_params['host']}/{db_params['dbname']}"

# Establish connection using SQLAlchemy
engine = create_engine(conn_str)

# Now you can query the data using pandas
query = "SELECT * FROM your_table_name;"  # replace with actual table name
df = pd.read_sql(query, engine)

# Clean the data as shown in the original response
